from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.core.deps import SessionDep, require_admin
from app.schemas.common import Page
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate
from app.services import product_service
from app.services.product_service import SortOption

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("", response_model=Page[ProductOut])
def list_products(
    db: SessionDep,
    search: Annotated[str | None, Query(max_length=100)] = None,
    category: Annotated[str | None, Query(description="slug ของหมวดหมู่ เช่น audio")] = None,
    sort: SortOption = "newest",
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1, le=100)] = 12,
):
    return product_service.list_products(
        db, page=page, size=size, search=search, category=category, sort=sort
    )


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: SessionDep):
    return product_service.get_product(db, product_id)


# Endpoint ที่แก้ไขข้อมูล ต้องเป็นผู้ดูแลระบบเท่านั้น
@router.post(
    "",
    response_model=ProductOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
def create_product(payload: ProductCreate, db: SessionDep):
    return product_service.create_product(db, payload)


@router.patch("/{product_id}", response_model=ProductOut, dependencies=[Depends(require_admin)])
def update_product(product_id: int, payload: ProductUpdate, db: SessionDep):
    return product_service.update_product(db, product_id, payload)


@router.delete(
    "/{product_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_admin)]
)
def delete_product(product_id: int, db: SessionDep):
    product_service.delete_product(db, product_id)