from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field

class Settings(BaseSettings): 
    DB_URL: Optional[str] = None
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        from_attributes = True

settings = Settings()
