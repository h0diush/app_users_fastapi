from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    port: int = 8000
    host: str = "0.0.0.0"


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    auth: str = "/auth"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class SuperUserConfig(BaseModel):
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class AccessToken(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    db: DataBaseConfig
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    access_token: AccessToken
    superuser: SuperUserConfig


settings = Settings()
