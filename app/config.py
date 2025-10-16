from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    ENVIRONMENT: str

    CAT_API_URL: str
    REQUEST_TIMEOUT: int

    USER_EMAIL: str
    USER_NAME: str
    USER_STACK: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
