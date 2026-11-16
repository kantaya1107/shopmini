from fastapi import FastAPI,Query,HTTPException,status
from pydantic import BaseModel, Field

app = FastAPI(title="Hello FastAPI", descripton="A simple",version="1.0.0")

fake_db = {
    1: {"id": 1, "name": "เมาส์ไร้สาย", "price": 590, "cost_price": 320},
    2: {"id": 2, "name": "หูฟังบลูทูธ", "price": 2490, "cost_price": 1500},
}

class ProductIn(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    cost_price: float = Field(gt=0)


class ProductPublic(BaseModel):
    """ข้อมูลที่ยอมให้ลูกค้าเห็น (ไม่มีต้นทุน)"""
    id: int
    name: str
    price: float

#คำสั่งรัน fastapi dev .\playground\hello_api.py
#create API
@app.get("/")
def read_root():
    return{"message": "welcome to FastAPI"}

@app.get("/hello")
def hello(name:str = "Word"):
    return {"message":f"Hello,{name}!"}

# Query Parameter: ค่าหลังเครื่องหมาย ? เช่น /products?max_price=1000
@app.get("/products", response_model=list[ProductPublic])
def list_products(max_price: float | None = Query(default=None, gt=0)):
    items = list(fake_db.values())
    if max_price is not None:
        items = [p for p in items if p["price"] <= max_price]
    return items

@app.get("/products/{product_id}", response_model=ProductPublic)
def get_product(product_id: int):
    if product_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ไม่พบสินค้า")
    return fake_db[product_id]


# Request Body: ข้อมูล JSON ที่ส่งมากับ POST ถูกตรวจด้วย Pydantic Model
@app.post("/products", response_model=ProductPublic, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductIn):
    new_id = max(fake_db) + 1
    fake_db[new_id] = {"id": new_id, **payload.model_dump()}
    return fake_db[new_id]

#แก้ไข
@app.put("/products/{product_id}",response_model=ProductPublic)
def update_product(product_id:int, payload:ProductIn):
    if product_id not in fake_db:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="ไม่พบสินค้าที่ต้องการแก้ไข")
    fake_db[product_id] = {"id":product_id,**payload.model_dump()}
    return fake_db[product_id]

# Endpoint สำหรับการลบข้อมูล
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    # ตรวจสอบก่อนว่ามีสินค้าชิ้นนี้อยู่ในระบบหรือไม่
    if product_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ไม่พบสินค้าที่ต้องการลบ")
 
    # ลบข้อมูลออกจาก dictionary
    del fake_db[product_id]
    return None