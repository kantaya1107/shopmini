from fastapi import APIRouter
from sqlalchemy import select

from app.core.deps import SessionDep
from app.models import Category
from app.schemas.category import CategoryOut

router = APIRouter(prefix="/api/categories", tags=["categories"])


@router.get("", response_model=list[CategoryOut])
def list_categories(db: SessionDep):
    return db.scalars(select(Category).order_by(Category.id)).all()
# จุดออกแบบ	เหตุผล
# Annotated[Session, Depends(get_db)] ตั้งชื่อเป็น SessionDep	เขียนครั้งเดียวใช้ได้ทุก Endpoint และอ่านง่าย (รูปแบบที่เอกสาร FastAPI แนะนำ)
# Query(ge=0), Query(ge=1, le=100)	กันผู้ใช้ขอ limit=1000000 จนฐานข้อมูลทำงานหนัก
# ilike(f"%{search}%")	ค้นหาไม่สนตัวพิมพ์เล็กใหญ่ SQLAlchemy ส่งค่าแบบ Parameter จึงปลอดภัยจาก SQL Injection
# model_dump(exclude_unset=True)	PATCH แก้เฉพาะช่องที่ผู้ใช้ส่งมาจริง ช่องที่ไม่ส่งไม่ถูกเขียนทับเป็น None
# status_code=204 สำหรับ DELETE	ลบสำเร็จ ไม่มีเนื้อหาส่งกลับ