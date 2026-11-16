SET search_path TO practice;

INSERT INTO categories (name, slug) VALUES
  ('อุปกรณ์คอมพิวเตอร์', 'accessories'),
  ('เครื่องเสียง', 'audio'),
  ('อุปกรณ์มือถือ', 'mobile'),
  ('ของใช้บนโต๊ะทำงาน', 'office');

INSERT INTO products (name, price, stock, category_id) VALUES
  ('เมาส์ไร้สาย Ergonomic', 590, 25, 1),
  ('คีย์บอร์ด Mechanical TKL', 1890, 12, 1),
  ('หูฟังบลูทูธ ANC', 2490, 10, 2),
  ('ลำโพงพกพากันน้ำ', 1590, 15, 2),
  ('สายชาร์จ USB-C 2 เมตร', 250, 60, 3),
  ('พาวเวอร์แบงก์ 20000mAh', 990, 22, 3);

INSERT INTO users (email, full_name, hashed_password) VALUES
  ('somchai@example.com', 'สมชาย ใจดี', 'x'),
  ('somying@example.com', 'สมหญิง รักเรียน', 'x');

INSERT INTO orders (user_id, total_amount) VALUES (1, 1430), (1, 2490), (2, 1590);

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
  (1, 1, 2, 590), (1, 5, 1, 250),
  (2, 3, 1, 2490),
  (3, 4, 1, 1590);