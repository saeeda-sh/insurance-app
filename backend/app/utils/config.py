from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    CLIENT_ORIGIN: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


settings = Settings()
