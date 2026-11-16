import math
from typing import Literal

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import AppError, ConflictError, NotFoundError
from app.models import Category, Product
from app.schemas.product import ProductCreate, ProductUpdate

SortOption = Literal["newest", "price_asc", "price_desc", "name"]

# Whitelist: ผู้ใช้เลือกได้เฉพาะค่าที่กำหนด ไม่ได้ส่งชื่อคอลัมน์เข้ามาใน SQL ตรง ๆ
SORT_COLUMNS = {
    "newest": Product.id.desc(),
    "price_asc": Product.price.asc(),
    "price_desc": Product.price.desc(),
    "name": Product.name.asc(),
}


def list_products(
    db: Session,
    *,
    page: int,
    size: int,
    search: str | None = None,
    category: str | None = None,
    sort: SortOption = "newest",
) -> dict:
    stmt = select(Product)
    if search:
        stmt = stmt.where(Product.name.ilike(f"%{search}%"))
    if category:
        stmt = stmt.join(Product.category).where(Category.slug == category)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(
        stmt.order_by(SORT_COLUMNS[sort], Product.id).offset((page - 1) * size).limit(size)
    ).all()

    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size,
        "pages": math.ceil(total / size) if total else 0,
    }


def get_product(db: Session, product_id: int) -> Product:
    product = db.get(Product, product_id)
    if product is None:
        raise NotFoundError("ไม่พบสินค้า", {"product_id": product_id})
    return product


def _ensure_category(db: Session, category_id: int) -> None:
    if db.get(Category, category_id) is None:
        raise AppError("ไม่พบหมวดหมู่ที่ระบุ", {"category_id": category_id})


def create_product(db: Session, data: ProductCreate) -> Product:
    _ensure_category(db, data.category_id)
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: int, data: ProductUpdate) -> Product:
    product = get_product(db, product_id)
    changes = data.model_dump(exclude_unset=True)
    if "category_id" in changes:
        _ensure_category(db, changes["category_id"])
    for field, value in changes.items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> None:
    product = get_product(db, product_id)
    db.delete(product)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ConflictError("ลบไม่ได้ เพราะสินค้านี้มีอยู่ในคำสั่งซื้อแล้ว", {"product_id": product_id})