from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig:
    port: int = 8000
    host: str = "0.0.0.0"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()


settings = Settings()
