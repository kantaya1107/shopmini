# list เทียบได้กับ Array
products = [
    {"id": 1, "name": "เมาส์ไร้สาย", "price": 590, "stock": 25},
    {"id": 5, "name": "หูฟังบลูทูธ ANC", "price": 2490, "stock": 10},
    {"id": 10, "name": "ขาตั้งโทรศัพท์", "price": 350, "stock": 0},
]

print(products[0]["name"]) #เมาส์ไร้สาย


# dict เทียบได้กับ Object
first = {"id": 1, "name": "เมาส์ไร้สาย", "price": 590, "stock": 25}
print(first["name"])
print(first["name"], first.get("color", "ไม่ระบุสี"))

# tuple: ลำดับที่แก้ไขไม่ได้ (immutable)
point = (13.75, 100.50)
lat, lng = point                    # unpacking เทียบได้กับ destructuring
print(lat, lng)

# for loop
for product in products:
    print(f"- {product['name']} ({product['price']} บาท)")

# # List Comprehension = map + filter ในบรรทัดเดียว
# names = [p["name"] for p in products]
# in_stock = [p["name"] for p in products if p["stock"] > 0]
# total_value = sum(p["price"] * p["stock"] for p in products)
# print(names)
# print(in_stock)
# print(f"มูลค่าสต็อกรวม {total_value:,} บาท")