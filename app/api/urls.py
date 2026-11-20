from fastapi import APIRouter, HTTPException, Depends
from app.models.models import ChatRequest, ChatResponse, SessionEndRequest, SessionEndResponse
from app.services.chat_service import ChatService, get_chat_service
from app.core.config import settings
from app.utils.logger import logger
from app.api.router import ROUTES, Slugs


router = APIRouter()


#============================
# Health Check Endpoint
#============================
@router.post(path=ROUTES[Slugs.HEALTH].slug, tags=[ROUTES[Slugs.HEALTH].tag])
def health_check():
    if not settings.OPENROUTER_API_KEY or not settings.OPENROUTER_BASE_URL:
        raise HTTPException(status_code=500, detail="API key or base URL not configured.")
    
    return {"status": "ok"}


# ============================
# Chatbot Endpoints
# ============================

@router.post(
    path=ROUTES[Slugs.MESSAGE].slug, 
    response_model=ChatResponse, 
    tags=[ROUTES[Slugs.MESSAGE].tag]
)
def send_message(body: ChatRequest, service: ChatService = Depends(get_chat_service)):
    """
    API: Send Message
    Usage: POST /api/v1/message
    Description: Send a user message and receive an AI reply with mood metadata.
    Raises: HTTPException if the session does not exist or if an error occurs during processing.
    """
    try:
        result = service.chat(
            session_id=body.session_id,
            user_message=body.message,
        )
        return ChatResponse(session_id=body.session_id, **result)
    except Exception as e:
        logger.error(f"Chat error [{body.session_id}]: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    path=ROUTES[Slugs.END_SESSION].slug, 
    response_model=SessionEndResponse, 
    tags=[ROUTES[Slugs.END_SESSION].tag]
)
def end_session(body: SessionEndRequest, service: ChatService = Depends(get_chat_service)):
    """
    API: End Session
    Usage: POST /api/v1/end-session
    Description: Gracefully end a chat session and optionally persist history.
    Raises: HTTPException if the session does not exist or if an error occurs during processing.
    """
    if not service.session_exists(body.session_id):
        raise HTTPException(status_code=404, detail="Session not found.")
    try:
        result = service.end_session(
            session_id=body.session_id,
            store_history=settings.STORE_HISTORY,
        )
        return SessionEndResponse(
            session_id=body.session_id,
            farewell=result["reply"],
            mood=result["mood"],
            face=result["face"],
        )
    except Exception as e:
        logger.error(f"End session error [{body.session_id}]: {e}")
        raise HTTPException(status_code=500, detail=str(e))
