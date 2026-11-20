import os
from fastapi import FastAPI
from app.api.urls import router
from app.core.config import settings
from app.core.constants import APP_TITLE, APP_DESCRIPTION, APP_SUMMARY, APP_VERSION, ENDPOINT_PREFIX, CHAT_HISTORY_DIR


# Validate settings and ensure required environment variables are set
settings.validate()

# Ensure output directory exists for chat history
os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)

# Initialize FastAPI application
application = FastAPI(
    title=APP_TITLE,
    summary=APP_SUMMARY,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

# Include the API router with a versioned prefix
application.include_router(router, prefix=ENDPOINT_PREFIX)
