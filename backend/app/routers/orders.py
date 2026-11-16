from fastapi import APIRouter, status

from app.core.deps import CurrentUser, SessionDep
from app.schemas.order import OrderCreate, OrderOut
from app.services import order_service

router = APIRouter(prefix="/api/orders", tags=["orders"])


@router.post("", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate, db: SessionDep, current_user: CurrentUser):
    return order_service.create_order(db, current_user, payload)


@router.get("/me", response_model=list[OrderOut])
def my_orders(db: SessionDep, current_user: CurrentUser):
    return order_service.list_my_orders(db, current_user)


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: SessionDep, current_user: CurrentUser):
    return order_service.get_order(db, current_user, order_id)