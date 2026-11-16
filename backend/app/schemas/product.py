from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.category import CategoryOut


class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=200, examples=["เมาส์ไร้สาย Ergonomic"])
    description: str = ""
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2, examples=[590])
    stock: int = Field(default=0, ge=0)
    image_url: str | None = None
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    """ใช้กับ PATCH: ทุกช่องไม่บังคับ ส่งมาเฉพาะช่องที่ต้องการแก้"""

    name: str | None = Field(default=None, min_length=2, max_length=200)
    description: str | None = None
    price: Decimal | None = Field(default=None, gt=0, max_digits=10, decimal_places=2)
    stock: int | None = Field(default=None, ge=0)
    image_url: str | None = None
    category_id: int | None = None


class ProductOut(BaseModel):
    """ข้อมูลที่ส่งออก: ไม่มี category_id ดิบ แต่ส่ง category เป็น Object แทน"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    price: float  # ฐานข้อมูลเก็บ NUMERIC(10,2) แต่ส่งเป็นตัวเลขให้ Frontend ใช้งานง่าย
    stock: int
    image_url: str | None
    category: CategoryOut
    created_at: datetime
    
    
# ProductCreate	Body ของ POST	ทุกช่องตรวจตามกติกา, price เป็น Decimal ไม่เกินทศนิยม 2 ตำแหน่ง
# ProductUpdate	Body ของ PATCH	ทุกช่องเป็น None ได้ (ส่งมาเฉพาะช่องที่จะแก้)
# ProductOut	response_model	from_attributes=True อ่านค่าจาก Object ของ SQLAlchemy ได้, category เป็น Object ซ้อน, price: float