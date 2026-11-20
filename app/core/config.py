import os
from dotenv import load_dotenv
from app.core.constants import ENV_VAR_APIKEY, ENV_VAR_BASEURL


load_dotenv()


class Settings:
    OPENROUTER_API_KEY: str = os.environ.get(ENV_VAR_APIKEY, "")
    OPENROUTER_BASE_URL: str = os.environ.get(ENV_VAR_BASEURL, "")
    BOT_TEMPERATURE: float = float(os.environ.get("BOT_TEMPERATURE", "0.7"))
    STORE_HISTORY: bool = os.environ.get("STORE_HISTORY", "true").lower() == "true"

    def validate(self):
        if not self.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY is missing!")
        if not self.OPENROUTER_BASE_URL:
            raise ValueError("OPENROUTER_BASE_URL is missing!")


settings = Settings()
