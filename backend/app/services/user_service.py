from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError
from app.core.security import hash_password, verify_password
from app.models import User
from app.schemas.user import UserCreate

# ใช้ตรวจรหัสผ่านหลอกเมื่อไม่พบอีเมล เพื่อให้เวลาตอบสนองใกล้เคียงกัน (ลดการเดาว่าอีเมลใดมีในระบบ)
DUMMY_HASH = hash_password("dummy-password")


def get_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email.lower()))


def register(db: Session, data: UserCreate, role: str = "customer") -> User:
    if get_by_email(db, data.email):
        raise ConflictError("อีเมลนี้ถูกใช้สมัครสมาชิกแล้ว")
    user = User(
        email=data.email.lower(),
        full_name=data.full_name,
        hashed_password=hash_password(data.password),
        role=role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate(db: Session, email: str, password: str) -> User | None:
    user = get_by_email(db, email)
    if user is None:
        verify_password(password, DUMMY_HASH)
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user