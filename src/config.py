# src/config/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class ProjectSettings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "Agentic ML Platform"
    
    # Cohere API Configuration
    COHERE_API_KEY: str
    
    # Qdrant Vector DB Configuration
    QDRANT_URL: str
    QDRANT_API_KEY: str = "" # Default to empty for local docker setup

    # Load configuration from the root .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = ProjectSettings()
