from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Completion Schemas
class CompletionCreate(BaseModel):
    prompt: str = Field(..., min_length=1)
    user_ip: Optional[str] = None
    user_device: Optional[str] = None

class CompletionResponse(BaseModel):
    id: str
    prompt: str
    completion: str

class CompletionUpdate(BaseModel):
    rating: int = Field(..., ge=1, le=5)

class CompletionList(BaseModel):
    total: int
    completions: List[CompletionResponse]

# Error Schemas
class HTTPError(BaseModel):
    detail: str