from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GOOGLE_API_KEY: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings() # type: ignore[call-arg]