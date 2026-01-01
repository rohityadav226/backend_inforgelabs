from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Zerodha
    KITE_API_KEY: str
    KITE_API_SECRET: str
    KITE_REDIRECT_URL: str

    # App
    JWT_SECRET: str = "change-me"
    ENV: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
