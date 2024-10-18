import time
from typing import Dict, Any
from src.code_explainer.models import CompletionModel
from src.config import settings
from groq import Groq

from src.database import get_db
from src.exceptions import ExternalServiceError

class CodeExplainService:
    def __init__(self):
        self.api_key = settings.LLM_API_KEY
        self.model = settings.MODEL
        self.db = get_db()
        
    
    def save_completion(self, completion: CompletionModel):
        completion_dict = completion.model_dump(by_alias=True)
        self.db.completions.insert_one(completion_dict)

    async def get_code_explanation(self, code: str, user_ip: str, user_device: str) -> Dict[str, Any]:
        start_time = time.time()
        
        client = Groq(api_key= self.api_key)

        try:
            chat_completion = client.chat.completions.create(
                messages=
                [
                    {
                        "role": "user",
                        "content": code
                    }
                ],
                model=self.model,)
        except:
            raise ExternalServiceError(service='groq', detail='')

        end_time = time.time()
        duration = end_time - start_time
        
        explanation = chat_completion.choices[0].message.content

        completion = CompletionModel(
            prompt=code,
            completion=explanation,
            user_ip= user_ip,
            user_device=user_device,
            inference_duration_in_ms=duration,
            user_id= None,
            rating=None
        )
        
        self.save_completion(completion)
        
        return explanation, duration

code_explain_service = CodeExplainService()