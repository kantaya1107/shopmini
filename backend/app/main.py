import logging
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.routers import auth, categories, orders, products

setup_logging()
logger = logging.getLogger("shopmini")

# app = FastAPI(
#     title=settings.app_name,
#     version="1.0.0",
#     description="REST API ของระบบร้านค้าออนไลน์ ShopMini",
# )
app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="REST API ของระบบร้านค้าออนไลน์ ShopMini",
    # ปิดหน้าเอกสาร API ได้บน Production ด้วย DOCS_ENABLED=false
    docs_url="/docs" if settings.docs_enabled else None,
    redoc_url="/redoc" if settings.docs_enabled else None,
    openapi_url="/openapi.json" if settings.docs_enabled else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    logger.info("%s %s -> %s (%.1f ms)", request.method, request.url.path, response.status_code, duration_ms)
    return response


register_exception_handlers(app)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/api/health", tags=["health"])
def health_check():
    return {"status": "ok"}