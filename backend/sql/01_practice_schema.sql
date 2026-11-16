-- ฝึก SQL ใน Schema แยก ชื่อ practice (ไม่ปนกับตารางจริงที่ Alembic จะสร้างใน public)
DROP SCHEMA IF EXISTS practice CASCADE;
CREATE SCHEMA practice;
SET search_path TO practice;

CREATE TABLE users (
    id              SERIAL PRIMARY KEY,
    email           VARCHAR(255) NOT NULL UNIQUE,
    full_name       VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role            VARCHAR(20)  NOT NULL DEFAULT 'customer',
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE categories (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    slug VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(200)  NOT NULL,
    price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock       INTEGER       NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category_id INTEGER       NOT NULL REFERENCES categories(id)
);

CREATE TABLE orders (
    id           SERIAL PRIMARY KEY,
    user_id      INTEGER       NOT NULL REFERENCES users(id),
    status       VARCHAR(20)   NOT NULL DEFAULT 'pending',
    total_amount NUMERIC(12,2) NOT NULL,
    created_at   TIMESTAMPTZ   NOT NULL DEFAULT now()
);

CREATE TABLE order_items (
    id         SERIAL PRIMARY KEY,
    order_id   INTEGER       NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER       NOT NULL REFERENCES products(id),
    quantity   INTEGER       NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10,2) NOT NULL
);


# Windows PowerShell: ไม่รองรับเครื่องหมาย < และการส่งต่อด้วย Get-Content ทำให้ภาษาไทยเพี้ยนเป็น ???
# ให้คัดลอกทั้งโฟลเดอร์ sql เข้าไปใน Container ก่อน แล้วสั่ง psql อ่านไฟล์ด้วย -f
-- docker cp sql shopmini-db:/tmp/sql
-- docker exec shopmini-db psql -U shopmini -d shopmini -f /tmp/sql/01_practice_schema.sql