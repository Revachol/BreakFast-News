# config.py
import secrets


class Settings:
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Генерация случайного ключа
    ALGORITHM: str = "HS256"  # Алгоритм для кодирования JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Время жизни токена в минутах


settings = Settings()
