from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Database settings
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Codinsight"
    
    # Security settings
    SECRET_KEY: str = "YOUR_SECRET_KEY_HERE"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # AWS settings
    AWS_ACCESS_KEY_ID: str = "YOUR_AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY: str = "YOUR_AWS_SECRET_ACCESS_KEY"
    AWS_REGION: str = "us-west-2"

    LLM_API_KEY: str = "YOUR_LLM_API_KEY"
    MODEL: str = "YOUR_MODEL"
    
@lru_cache()
def get_settings():
    return Settings()

# Usage
settings = get_settings()
print(settings.DATABASE_URL)