"""เติมข้อมูลเริ่มต้นของ ShopMini (รันซ้ำได้ ไม่สร้างข้อมูลซ้ำ)

วิธีรัน (ที่โฟลเดอร์ backend):  python -m scripts.seed
"""
from decimal import Decimal

from sqlalchemy import func, select

from app.core.database import SessionLocal
from app.core.security import hash_password
from app.models import Category, Product, User

CATEGORIES = [
    ("accessories", "อุปกรณ์คอมพิวเตอร์"),
    ("audio", "เครื่องเสียง"),
    ("mobile", "อุปกรณ์มือถือ"),
    ("office", "ของใช้บนโต๊ะทำงาน"),
]

# (slug หมวดหมู่, ชื่อ, ราคา, สต็อก, รายละเอียด)
PRODUCTS = [
    ("accessories", "เมาส์ไร้สาย Ergonomic", "590", 25, "เมาส์ทรงตั้ง ลดอาการปวดข้อมือ เชื่อมต่อได้ทั้ง Bluetooth และ USB Receiver"),
    ("accessories", "คีย์บอร์ด Mechanical TKL", "1890", 12, "คีย์บอร์ดขนาด 87 ปุ่ม สวิตช์ Brown เสียงเบา เหมาะกับงานพิมพ์"),
    ("accessories", "แผ่นรองเมาส์ XL", "290", 40, "แผ่นรองขนาด 90 x 40 ซม. ขอบเย็บกันลุ่ย"),
    ("accessories", "USB-C Hub 7-in-1", "1290", 18, "HDMI 4K, USB-A 3 พอร์ต, SD Card และ PD 100W"),
    ("audio", "หูฟังบลูทูธ ANC", "2490", 10, "ตัดเสียงรบกวน ใช้งานต่อเนื่อง 30 ชั่วโมง"),
    ("audio", "ลำโพงพกพากันน้ำ", "1590", 15, "มาตรฐาน IPX7 เสียงเบสแน่น พกไปเที่ยวได้"),
    ("audio", "ไมโครโฟน USB สำหรับประชุม", "1990", 8, "รับเสียงรอบทิศทาง เสียบใช้งานได้ทันที"),
    ("mobile", "สายชาร์จ USB-C 2 เมตร", "250", 60, "สายถักไนลอน รองรับชาร์จเร็ว 60W"),
    ("mobile", "พาวเวอร์แบงก์ 20000mAh", "990", 22, "ชาร์จเร็ว PD 22.5W พร้อมจอแสดงแบตเตอรี่"),
    ("mobile", "ขาตั้งโทรศัพท์ตั้งโต๊ะ", "350", 0, "ปรับมุมได้ 270 องศา วัสดุอะลูมิเนียม"),
    ("office", "โคมไฟตั้งโต๊ะ LED", "890", 14, "ปรับความสว่างและอุณหภูมิสีได้ 5 ระดับ"),
    ("office", "ขาตั้งแล็ปท็อปอะลูมิเนียม", "790", 20, "ยกจอให้อยู่ระดับสายตา พับเก็บได้"),
]


def seed_catalog(db) -> None:
    if db.scalar(select(func.count()).select_from(Category)):
        print("มีหมวดหมู่อยู่แล้ว ข้ามการเพิ่มสินค้า")
        return

    categories = {slug: Category(slug=slug, name=name) for slug, name in CATEGORIES}
    db.add_all(categories.values())

    for index, (slug, name, price, stock, description) in enumerate(PRODUCTS, start=1):
        db.add(
            Product(
                name=name,
                price=Decimal(price),
                stock=stock,
                description=description,
                image_url=f"https://picsum.photos/seed/shopmini-{index}/400/300",
                category=categories[slug],
            )
        )
    db.commit()
    print(f"เพิ่มหมวดหมู่ {len(CATEGORIES)} รายการ และสินค้า {len(PRODUCTS)} รายการ")


ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin@1234"  # ใช้ในห้องเรียนเท่านั้น ต้องเปลี่ยนทันทีบน Production


def seed_admin(db) -> None:
    if db.scalar(select(User).where(User.email == ADMIN_EMAIL)):
        print("มีผู้ดูแลระบบอยู่แล้ว")
        return
    db.add(
        User(
            email=ADMIN_EMAIL,
            full_name="ผู้ดูแลระบบ ShopMini",
            hashed_password=hash_password(ADMIN_PASSWORD),
            role="admin",
        )
    )
    db.commit()
    print(f"สร้างผู้ดูแลระบบ {ADMIN_EMAIL} แล้ว")


def main() -> None:
    with SessionLocal() as db:
        seed_catalog(db)
        seed_admin(db)


if __name__ == "__main__":
    main()