from datetime import datetime
from typing import Dict, List, cast
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from app.core.constants import (
    AI_MODEL, ROLE, SYSTEM_PROMPT,
    CHAT_HISTORY_DIR_FILENAME
)
from app.services.mood_engine.mood_engine_models import Mood
from app.services.mood_engine.mood_engine import MoodClassifier
from app.utils.logger import logger
from app.core.config import settings


__chat_service: ChatService | None = None


def get_chat_service() -> ChatService:
    """Singleton pattern for ChatService instance."""
    global __chat_service

    if __chat_service is None:
        __chat_service = ChatService(
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_BASE_URL,
            temperature=settings.BOT_TEMPERATURE,
        )
        logger.info("ChatService has been initialized!")
    return __chat_service


class ChatSession:
    """Holds conversation history for a single session."""

    def __init__(self):
        self.messages: List[ChatCompletionMessageParam] = []
        self.__add_message(ROLE.SYSTEM, SYSTEM_PROMPT)

    def __add_message(self, role: ROLE, content: str):
        self.messages.append(
            cast(ChatCompletionMessageParam, {"role": role, "content": content})
        )

    def add_user(self, content: str):
        self.__add_message(ROLE.USER, content)

    def add_assistant(self, content: str):
        self.__add_message(ROLE.ASSISTANT, content)


class ChatService:
    """
    Stateful chat service that manages multiple user sessions.
    One ChatService instance is shared across the FastAPI app lifetime (singleton).
    """

    def __init__(self, api_key: str, base_url: str, temperature: float = 0.7):
        self.__client = OpenAI(api_key=api_key, base_url=base_url)
        self.__temperature = temperature
        self.mood_classifier = MoodClassifier(client=self.__client, model=AI_MODEL.GPT_4O_MINI)
        self.__sessions: Dict[str, ChatSession] = {}

    def __del__(self):
        """Clean up resources if needed."""
        self.__sessions.clear()
        self.__client = None
        logger.info("ChatService instance destroyed and sessions cleared.")

    def __get_or_create_session(self, session_id: str) -> ChatSession:
        """Retrieve an existing session or create a new one."""
        if session_id not in self.__sessions:
            self.__sessions[session_id] = ChatSession()
            logger.info(f"New session created: {session_id}")
        return self.__sessions[session_id]
    
    def __store_chat_history(self, session_id: str):
        """Persist the chat history of a session to a file."""
        session = self.__sessions.get(session_id)
        if not session:
            return
        try:
            with open(CHAT_HISTORY_DIR_FILENAME, "a", encoding="utf-8") as f:
                f.write("=" * 100 + "\n")
                f.write(f"Session [{session_id}] | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 100 + "\n")
                for msg in session.messages:
                    f.write(f"\n[{str(msg.get('role')).upper()}]: {msg.get('content')}\n")
                f.write("\n")
        except Exception as e:
            logger.error(f"Failed to save chat history for session {session_id}: {e}")

    @property
    def active_sessions(self) -> List[str]:
        return list(self.__sessions.keys())
    
    # =========================
    # Public API methods 
    # =========================

    def chat(self, session_id: str, user_message: str) -> dict[str, str]:
        """Process a user message and return AI reply with mood metadata."""

        if self.__client is None:
            raise RuntimeError("Client is not initialized!")
        
        session = self.__get_or_create_session(session_id)
        session.add_user(user_message)

        response = {
            "reply": "No response received.",
            "mood":  Mood.CONFUSED.value,
            "face":  Mood.CONFUSED.face,
        }

        chat_completion = self.__client.chat.completions.create(
            model=AI_MODEL.GPT_4O_MINI,
            messages=session.messages,
            temperature=self.__temperature,
        )

        ai_message = (
            chat_completion.choices[0].message.content
            if chat_completion.choices
            else None
        )

        if not ai_message:
            return response

        session.add_assistant(ai_message)
        mood = self.mood_classifier.get_mood(ai_message)

        response["face"] = mood.face
        response["mood"] = mood.value
        response["reply"] = ai_message
        return response

    def end_session(self, session_id: str, store_history: bool = True) -> dict[str, str]:
        """Send goodbye, optionally persist history, and clean up session."""
        if not self.session_exists(session_id):
            return {
                "farewell": "Session not found.",
                "mood": Mood.CONFUSED.value,
                "face": Mood.CONFUSED.face,
            }

        result = self.chat(session_id, "Goodbye!")

        if store_history:
            self.__store_chat_history(session_id)

        del self.__sessions[session_id]
        logger.info(f"Session ended: {session_id}")
        return result
    
    def session_exists(self, session_id: str) -> bool:
        return session_id in self.__sessions