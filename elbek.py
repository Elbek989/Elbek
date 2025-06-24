import psycopg2


conn = psycopg2.connect(
    dbname = "test",
    user = "postgres",
    password = "1906",
    host = "localhost",
    port = "5432"
)
cur = conn.cursor()
sql1 = """
select * from categories
"""
cur.execute(sql1)
s = cur.fetchall()
print(s)
for item in s:
    print(item[0],item[1])
conn.commit()
cur.close()
conn.close()
