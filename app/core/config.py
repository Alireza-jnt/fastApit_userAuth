from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """project setup using Pydantic"""

    # Database
    MONGODB_URL: str = "mongodb://root:password@localhost:27017"
    DATABASE_NAME: str = "auth_db"

    # Security
    SECRET_KEY: str = "change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Auth System"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()