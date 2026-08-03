from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application
    app_name = "Inventory Management API"
    app_version = "1.0.0"
    debug: bool = True

    # Database
    database_url: str = "sqlite:///./data/app.db"

    model_config = SettingsConfigDict(
            env_file=".env", 
            env_file_encoding="utf-8",
            extra="ignore",
        )

settings: Settings = Settings()
