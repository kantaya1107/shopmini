from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    """รูปแบบผลลัพธ์แบบแบ่งหน้า พร้อม Metadata ที่ Frontend ต้องใช้"""

    items: list[T]
    total: int
    page: int
    size: int
    pages: int