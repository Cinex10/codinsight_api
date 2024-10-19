from pydantic import BaseModel, Field
from typing import List

# Completion Schemas
class CompletionCreate(BaseModel):
    prompt: str = Field(..., min_length=1)

class CompletionResponse(BaseModel):
    prompt: str
    completion: str

class CompletionRate(BaseModel):
    rating: int = Field(..., ge=1, le=5)

class CompletionList(BaseModel):
    total: int
    completions: List[CompletionResponse]

# Error Schemas
class HTTPError(BaseModel):
    detail: str