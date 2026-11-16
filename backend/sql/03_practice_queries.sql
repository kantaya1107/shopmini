SET search_path TO practice;

-- 1) SELECT + WHERE + ORDER BY + LIMIT/OFFSET
SELECT id, name, price FROM products
WHERE price < 2000
ORDER BY price DESC
LIMIT 3 OFFSET 0;

-- 2) INNER JOIN: สินค้าพร้อมชื่อหมวดหมู่
SELECT p.name, c.name AS category, p.price
FROM products p
INNER JOIN categories c ON c.id = p.category_id
WHERE c.slug = 'audio';

-- 3) LEFT JOIN: สินค้าทุกตัว รวมตัวที่ยังไม่เคยถูกสั่ง (order_id เป็น NULL)
SELECT p.name, oi.order_id
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
ORDER BY p.id;

-- 4) GROUP BY + COUNT + SUM: ยอดขายต่อหมวดหมู่
SELECT c.name AS category,
       COUNT(oi.id)                                   AS lines,
       COALESCE(SUM(oi.quantity), 0)                  AS units,
       COALESCE(SUM(oi.quantity * oi.unit_price), 0)  AS revenue
FROM categories c
LEFT JOIN products p     ON p.category_id = c.id
LEFT JOIN order_items oi ON oi.product_id = p.id
GROUP BY c.name
ORDER BY revenue DESC;

-- 5) UPDATE และ DELETE (ต้องมี WHERE เสมอ)
UPDATE products SET stock = stock - 2 WHERE id = 1 RETURNING id, name, stock;
DELETE FROM order_items WHERE order_id = 3 RETURNING *;


# Windows PowerShell
-- docker cp sql shopmini-db:/tmp/sql
-- docker exec shopmini-db psql -U shopmini -d shopmini -f /tmp/sql/02_practice_data.sql
-- docker exec shopmini-db psql -U shopmini -d shopmini -f /tmp/sql/03_practice_queries.sql