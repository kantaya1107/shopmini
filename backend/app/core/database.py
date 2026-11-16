from collections.abc import Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# ตั้งชื่อ Constraint ให้เป็นระบบ เพื่อให้ Alembic สร้าง/ลบ Constraint ได้ถูกต้องเสมอ
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)


engine = create_engine(settings.database_url, echo=settings.sql_echo, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    """Dependency: เปิด Session 1 ตัวต่อ 1 Request และปิดเสมอเมื่อจบ Request"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
# ส่วนประกอบ	หน้าที่
# postgresql+psycopg://	บอก SQLAlchemy ให้ใช้ Driver psycopg รุ่น 3
# pool_pre_ping=True	ตรวจว่า Connection ยังใช้ได้ก่อนนำมาใช้ (ป้องกัน Error หลังฐานข้อมูลรีสตาร์ต)
# expire_on_commit=False	Object ยังอ่านค่าได้หลัง commit() โดยไม่ต้อง Query ใหม่
# NAMING_CONVENTION	ตั้งชื่อ Constraint/Index แบบคาดเดาได้ ทำให้ Alembic สร้างและลบได้ถูกต้อง
# get_db() + yield	Dependency ของ FastAPI: เปิด Session ก่อนเข้า Endpoint และปิดใน finally เสมอแม้เกิด Error