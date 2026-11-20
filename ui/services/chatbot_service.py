from .api_client import APIClient


BASE_URL = "http://0.0.0.0:8000/api/v1"
TIMEOUT = 30  # seconds


class ChatBotService:
    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT):
        self.__api_client = APIClient(base_url=base_url, timeout=timeout)

    def send_message(self, message: str, session_id: str) -> str:
        try:
            payload = {
                "message": str(message), 
                "session_id": session_id
            }
            response = self.__api_client.post("message", json=payload)
            ai_reply = response.get("reply", "")
            ai_mood = response.get("mood", "")
            ai_face = response.get("face", "")

            ai_reply_with_mood = f"{ai_face} [{ai_mood}]: {ai_reply}"
            return ai_reply_with_mood
        except Exception:
            raise
    