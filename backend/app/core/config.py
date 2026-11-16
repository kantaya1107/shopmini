from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_SECRET = "change-this-to-a-long-random-string"


class Settings(BaseSettings):
    """อ่านค่าจาก Environment Variable ก่อน ถ้าไม่มีจึงอ่านจากไฟล์ .env และสุดท้ายใช้ค่า Default"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "ShopMini API"
    environment: str = "development"  # development | production
    database_url: str = ""
    cors_origins: list[str] = ["http://localhost:5173"]
    docs_enabled: bool = True
    sql_echo: bool = False
    log_level: str = "INFO"

    # JWT
    secret_key: str = DEFAULT_SECRET
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    @field_validator("database_url")
    @classmethod
    def use_psycopg_driver(cls, value: str) -> str:
        # ผู้ให้บริการ Cloud (เช่น Render) ให้ URL แบบ postgresql:// หรือ postgres://
        # ต้องระบุ Driver psycopg (v3) ให้ SQLAlchemy เอง
        for prefix in ("postgres://", "postgresql://"):
            if value.startswith(prefix):
                return "postgresql+psycopg://" + value[len(prefix):]
        return value

    @model_validator(mode="after")
    def check_production_secret(self):
        if self.environment == "production" and (self.secret_key == DEFAULT_SECRET or len(self.secret_key) < 32):
            raise ValueError("Production ต้องกำหนด SECRET_KEY ที่สุ่มขึ้นใหม่ และยาวอย่างน้อย 32 ตัวอักษร")
        return self


settings = Settings()