import os
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.database import Base, get_db
from app.core.security import hash_password
from app.main import app
from app.models import Category, Product, User

# ฐานข้อมูลสำหรับเทสโดยเฉพาะ ห้ามชี้ไปที่ฐานข้อมูลจริงเด็ดขาด
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql+psycopg://shopmini:shopmini_pass@localhost:5434/shopmini_test",
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
def create_schema():
    """สร้างตารางครั้งเดียวตอนเริ่มรันเทส และลบทิ้งเมื่อจบ"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(autouse=True)
def clean_tables():
    """ล้างข้อมูลหลังจบแต่ละเทส ทำให้ทุกเทสเป็นอิสระต่อกัน"""
    yield
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE order_items, orders, products, categories, users RESTART IDENTITY CASCADE"))


@pytest.fixture
def db():
    with TestingSessionLocal() as session:
        yield session


@pytest.fixture
def client():
    def override_get_db():
        with TestingSessionLocal() as session:
            yield session

    # สลับ Dependency get_db ของจริงให้ชี้ไปที่ฐานข้อมูลเทส
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def products(db):
    audio = Category(name="เครื่องเสียง", slug="audio")
    mobile = Category(name="อุปกรณ์มือถือ", slug="mobile")
    items = [
        Product(name="หูฟังบลูทูธ ANC", price=Decimal("2490"), stock=10, category=audio),
        Product(name="ลำโพงพกพา", price=Decimal("1590"), stock=5, category=audio),
        Product(name="สายชาร์จ USB-C", price=Decimal("250"), stock=60, category=mobile),
    ]
    db.add_all(items)
    db.commit()
    return items


def _create_user(db, email: str, role: str) -> User:
    user = User(email=email, full_name="ผู้ใช้ทดสอบ", hashed_password=hash_password("Passw0rd!"), role=role)
    db.add(user)
    db.commit()
    return user


def _auth_headers(client, email: str) -> dict:
    res = client.post("/api/auth/login", data={"username": email, "password": "Passw0rd!"})
    return {"Authorization": f"Bearer {res.json()['access_token']}"}


@pytest.fixture
def customer_headers(client, db):
    _create_user(db, "customer@example.com", "customer")
    return _auth_headers(client, "customer@example.com")


@pytest.fixture
def admin_headers(client, db):
    _create_user(db, "admin@example.com", "admin")
    return _auth_headers(client, "admin@example.com")