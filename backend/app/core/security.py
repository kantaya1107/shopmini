from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

from app.core.config import settings

# ใช้ bcrypt ผ่าน pwdlib (passlib เดิมใช้กับ bcrypt 5.x ไม่ได้แล้ว)
password_hash = PasswordHash((BcryptHasher(),))


def hash_password(plain_password: str) -> str:
    return password_hash.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(subject: str, extra_claims: dict | None = None) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject,  # PyJWT กำหนดให้ sub เป็น string
        "iat": now,
        "exp": now + timedelta(minutes=settings.access_token_expire_minutes),
        **(extra_claims or {}),
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> dict:
    """คืน payload ถ้า Token ถูกต้อง และโยน jwt.InvalidTokenError ถ้าลายเซ็นผิดหรือหมดอายุ"""
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])