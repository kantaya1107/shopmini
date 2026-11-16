from decimal import Decimal


# Type Hints บอกชนิดข้อมูลที่คาดหวัง (Python ไม่บังคับตอนรัน แต่ Editor และ FastAPI นำไปใช้)
def apply_vat(price: Decimal, rate: Decimal = Decimal("0.07")) -> Decimal:
    return (price * (1 + rate)).quantize(Decimal("0.01"))


def find_product(products: list[dict], product_id: int) -> dict | None:
    for p in products:
        if p["id"] == product_id:
            return p
    return None


print(apply_vat(Decimal("590")))
print(find_product([{"id": 1, "name": "เมาส์"}], 1))
print(find_product([], 99))

# ทำไมเงินต้องใช้ Decimal ไม่ใช่ float
print(0.1 + 0.2)                          # 0.30000000000000004
print(Decimal("0.1") + Decimal("0.2"))    # 0.3