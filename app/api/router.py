from enum import StrEnum
from pydantic import BaseModel


# The Slugs enum defines the API endpoint slugs for the chatbot application.
class Slugs(StrEnum):
    HEALTH = "/health"
    MESSAGE = "/message"
    END_SESSION = "/end-session"


# The RouteInfo dataclass holds metadata for each API route, including the slug, summary, description, and tag.
class RouteInfo(BaseModel):
    slug: str
    summary: str
    description: str
    tag: str


# Routes dictionary mapping Slugs to RouteInfo
ROUTES: dict[Slugs, RouteInfo] = {
    Slugs.HEALTH: RouteInfo(
        slug=Slugs.HEALTH, summary="Health Check", description="Health check endpoint to verify API status.", tag="Health"
    ),
    Slugs.MESSAGE: RouteInfo(
        slug=Slugs.MESSAGE, summary="Send Message", description="Endpoint to send a message and receive a response.", tag="Chat"
    ),
    Slugs.END_SESSION: RouteInfo(
        slug=Slugs.END_SESSION, summary="End Session", description="Endpoint to gracefully end a chat session and optionally persist history.", tag="Chat"
    )
}
