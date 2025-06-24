import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Jadval yaratish (products)
create_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    supplier_id INTEGER,
    category_id INTEGER,
    quantity_per_unit TEXT,
    unit_price REAL,
    units_in_stock INTEGER,
    units_on_order INTEGER,
    reorder_level INTEGER,
    discontinued INTEGER
)
"""
cur.execute(create_table_sql)

# Ma’lumot qo‘shish
insert_sql = """
INSERT INTO products (product_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued) VALUES
(1, 'Chai', 8, 1, '10 boxes x 30 bags', 18, 39, 0, 10, 1),
(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19, 17, 40, 25, 1),
(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10, 13, 70, 25, 0),
(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22, 53, 0, 0, 0),
(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35, 0, 0, 0, 1)
"""
cur.execute(insert_sql)

conn.commit()

# Ma’lumotlarni olish uchun products jadvalini tanlaymiz
select_sql = "SELECT * FROM products"
cur.execute(select_sql)

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
