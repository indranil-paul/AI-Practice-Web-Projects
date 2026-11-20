from pydantic import BaseModel, Field


# =================
# Chat API Schemas 
# =================

class ChatRequest(BaseModel):
    session_id: str = Field(..., description="Unique session identifier per user/conversation")
    message: str = Field(..., description="User message to the chatbot")


class ChatResponse(BaseModel):
    session_id: str
    reply: str
    mood: str
    face: str


class SessionEndRequest(BaseModel):
    session_id: str = Field(..., description="Session to terminate")


class SessionEndResponse(BaseModel):
    session_id: str
    farewell: str
    mood: str
    face: str
    message: str = "Session ended successfully."