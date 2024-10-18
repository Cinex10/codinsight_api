from pydantic import BaseModel, BeforeValidator, Field, EmailStr, GetJsonSchemaHandler, ConfigDict
from typing import Any, Callable,  Optional, Annotated
from datetime import datetime
from bson import ObjectId
from pydantic_core import core_schema



PyObjectId = Annotated[str, BeforeValidator(str)]


class UserModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed = True,
        json_encoders = {ObjectId: str}
        )
    
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    email: EmailStr = Field(...)
    password: str = Field(...)

class CompletionModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed = True,
        json_encoders = {ObjectId: str}
        )
    
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    prompt: str = Field(...)
    completion: str = Field(...)
    inference_duration_in_ms: float = Field(gt=0)
    user_ip: str = Field(...)
    user_device: str = Field(...)
    user_id: Optional[PyObjectId] = Field(None)
    timestamp: datetime = Field(default_factory=lambda: datetime.now())
    rating: Optional[int] = Field(None, ge=1, le=5)
    
    def __eq__(self, other):
        if isinstance(other, CompletionModel):
            return (
                self.prompt == other.prompt and
                self.completion == other.completion and
                self.user_ip == other.user_ip and
                self.user_device == other.user_device and
                self.user_id == other.user_id and
                self.rating == other.rating and
                self.inference_duration_in_ms == other.inference_duration_in_ms
            )
        return False