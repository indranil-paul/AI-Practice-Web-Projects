from enum import StrEnum
from pathlib import Path


# ============================ 
# APP
# ============================ 
APP_VERSION = "1.0.0"
APP_TITLE = "SimpleChatbot API"
APP_SUMMARY = "A simple chatbot API with mood detection"
APP_DESCRIPTION = "OpenRouter-backed chatbot with mood detection"
ENV_VAR_APIKEY = "OPENROUTER_API_KEY"
ENV_VAR_BASEURL = "OPENROUTER_BASE_URL"
ENDPOINT_PREFIX = f"/api/v{APP_VERSION.split('.')[0]}"

# ============================ 
# CHAT
# ============================ 
CHAT_HISTORY_DIR = "output"
CHAT_HISTORY_DIR_FILENAME = "output/chat_history.txt"
NO_RESPONSE_MESSAGE = "No response received!"
USER_PROMPT = "('!') You: "
SYSTEM_PROMPT = "You are a helpful and friendly assistant."
EXIT_COMMANDS = [
    "exit", "quit", "bye", "goodbye",
    "stop", "end", "terminate", "close",
    "finish", "cancel", "abort",
]

# ============================ 
# LOGGING
# ============================ 
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = "DEBUG"


# ============================ 
# AI models and roles
# ============================ 
class AI_MODEL(StrEnum):
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"


class ROLE(StrEnum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
