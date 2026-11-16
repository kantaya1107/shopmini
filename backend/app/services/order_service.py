import logging
from collections import Counter
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session, lazyload

from app.core.exceptions import AppError, InsufficientStockError, NotFoundError
from app.models import Order, OrderItem, Product, User
from app.schemas.order import OrderCreate

logger = logging.getLogger("shopmini")


def create_order(db: Session, user: User, data: OrderCreate) -> Order:
    # รวมสินค้าที่ส่งมาซ้ำกันให้เป็นบรรทัดเดียว เช่น [1 x 2, 1 x 1] -> {1: 3}
    wanted = Counter()
    for item in data.items:
        wanted[item.product_id] += item.quantity

    try:
        # SELECT ... FOR UPDATE: ล็อกแถวสินค้าไว้จนจบ Transaction ป้องกันการขายเกินสต็อก
        # เมื่อมีผู้ใช้หลายคนสั่งสินค้าชิ้นเดียวกันพร้อมกัน
        # (lazyload ปิดการ JOIN หมวดหมู่ใน Query นี้ เพราะเอกสาร SQLAlchemy ไม่แนะนำให้ใช้ joined eager loading คู่กับ FOR UPDATE)
        products = db.scalars(
            select(Product)
            .options(lazyload(Product.category))
            .where(Product.id.in_(wanted))
            .order_by(Product.id)
            .with_for_update()
        ).all()
        found = {p.id: p for p in products}

        missing = sorted(set(wanted) - set(found))
        if missing:
            raise AppError("มีสินค้าบางรายการไม่อยู่ในระบบ", {"product_ids": missing})

        shortages = [
            {"product_id": pid, "name": found[pid].name, "requested": qty, "available": found[pid].stock}
            for pid, qty in wanted.items()
            if found[pid].stock < qty
        ]
        if shortages:
            raise InsufficientStockError("สินค้าบางรายการมีไม่พอ", shortages)

        order = Order(user_id=user.id, status="pending", total_amount=Decimal("0"))
        total = Decimal("0")
        for pid, qty in wanted.items():
            product = found[pid]
            product.stock -= qty  # ตัดสต็อก
            order.items.append(OrderItem(product_id=pid, quantity=qty, unit_price=product.price))
            total += product.price * qty
        order.total_amount = total

        db.add(order)
        db.commit()  # บันทึก Order, Order Items และสต็อกใหม่ พร้อมกันใน Transaction เดียว
    except Exception:
        db.rollback()  # ผิดพลาดตรงไหนก็ตาม ยกเลิกทั้งหมด ไม่มีข้อมูลครึ่ง ๆ กลาง ๆ
        raise

    db.refresh(order)
    logger.info("Order #%s created by user %s total=%s", order.id, user.id, order.total_amount)
    return order


def list_my_orders(db: Session, user: User) -> list[Order]:
    stmt = select(Order).where(Order.user_id == user.id).order_by(Order.id.desc())
    return list(db.scalars(stmt).all())


def get_order(db: Session, user: User, order_id: int) -> Order:
    order = db.get(Order, order_id)
    # ผู้ใช้ทั่วไปเห็นได้เฉพาะคำสั่งซื้อของตนเอง ผู้ดูแลระบบเห็นได้ทั้งหมด
    if order is None or (order.user_id != user.id and user.role != "admin"):
        raise NotFoundError("ไม่พบคำสั่งซื้อ", {"order_id": order_id})
    return order