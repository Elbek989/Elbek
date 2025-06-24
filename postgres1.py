import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Jadval yaratish (mos ustun nomlari bilan)
create_table_sql = """
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL,
    description TEXT,
    picture BLOB
)
"""
cur.execute(create_table_sql)

# Ma’lumot qo‘shish
insert_sql = """
INSERT INTO categories (category_id, category_name, description, picture) VALUES
(1, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales', NULL),
(2, 'Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings', NULL),
(3, 'Confections', 'Desserts, candies, and sweet breads', NULL),
(4, 'Dairy Products', 'Cheeses', NULL),
(5, 'Grains/Cereals', 'Breads, crackers, pasta, and cereal', NULL)
"""
cur.execute(insert_sql)

conn.commit()

# Ma’lumotlarni ko‘rish uchun
select_sql = "SELECT * FROM categories"
cur.execute(select_sql)

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
