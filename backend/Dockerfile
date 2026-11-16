# ---------- Stage 1: builder (ติดตั้ง Dependency) ----------
FROM python:3.14-slim AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# ---------- Stage 2: runtime (Image ที่ใช้รันจริง) ----------
FROM python:3.14-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# สร้างผู้ใช้ที่ไม่ใช่ root สำหรับรันแอป
RUN groupadd --system app && useradd --system --gid app --no-create-home app

WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY --chown=app:app . .

USER app
EXPOSE 8000

# รัน Migration ก่อน แล้วจึงเปิดเซิร์ฟเวอร์ (Render จะส่งค่า PORT มาให้เอง)
CMD ["sh", "-c", "alembic upgrade head && exec fastapi run app/main.py --host 0.0.0.0 --port ${PORT:-8000}"]