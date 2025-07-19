import psycopg2


conn = psycopg2.connect(
    dbname="hometask",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS KORZINKA")
cur.execute("DROP TABLE IF EXISTS USERS")
cur.execute("DROP TABLE IF EXISTS MAHSULOTLAR")
cur.execute("DROP TABLE IF EXISTS KARTALAR")


cur.execute("""
CREATE TABLE USERS (
    name VARCHAR NOT NULL,
    card_number BIGINT PRIMARY KEY
)
""")


cur.execute("""
CREATE TABLE MAHSULOTLAR (
    title VARCHAR NOT NULL,
    balance INTEGER NOT NULL,
    id_number INTEGER PRIMARY KEY
)
""")


cur.execute("""
CREATE TABLE KARTALAR (
    balance INTEGER NOT NULL,
    card_number BIGINT PRIMARY KEY,
    password INTEGER NOT NULL
)
""")


cur.execute("""
CREATE TABLE KORZINKA (
    card_number BIGINT REFERENCES USERS(card_number),
    product_id INTEGER REFERENCES MAHSULOTLAR(id_number),
    quantity INTEGER NOT NULL
)
""")


USERS = [("Ali", 33333333333333),
         ("Vali", 22222222222222),
         ("Elbek", 11111111111111)]


MAHSULOTLAR = [("Olma", 40, 100),
               ("Banan", 50, 129),
               ("Apelsin", 75, 101)]


KARTALAR = [(1400000, 33333333333333, 1111),
            (1400000, 22222222222222, 2222),
            (1500000, 11111111111111, 3333)]


cur.executemany("INSERT INTO USERS (name, card_number) VALUES (%s, %s)", USERS)
cur.executemany("INSERT INTO MAHSULOTLAR (title, balance, id_number) VALUES (%s, %s, %s)", MAHSULOTLAR)
cur.executemany("INSERT INTO KARTALAR (balance, card_number, password) VALUES (%s, %s, %s)", KARTALAR)
conn.commit()


print("===== SUPERMARKETIMIZGA HUSH KELIBSIZ =====")

while True:
    a = int(input("Karta raqamingizni kiriting: "))
    cur.execute("SELECT * FROM KARTALAR WHERE card_number = %s", (a,))
    karta = cur.fetchone()

    if karta is None:
        print("Bunday karta topilmadi. Qaytadan urinib ko‘ring.")
        continue

    print("Karta topildi.")


    cur.execute("DELETE FROM KORZINKA WHERE card_number = %s", (a,))
    conn.commit()


    while True:
        print("\n--- MAHSULOTLAR ---")
        cur.execute("SELECT id_number, title, balance FROM MAHSULOTLAR")
        mahsulotlar = cur.fetchall()
        for id, title, balans in mahsulotlar:
            print(f"{title} (id={id}) - {balans} kg mavjud")

        tanlov = int(input("\nMahsulot ID sini kiriting (0 - xaridni tugatish): "))
        if tanlov == 0:
            break

        kg = int(input("Necha kg olmoqchisiz: "))
        cur.execute("SELECT title, balance FROM MAHSULOTLAR WHERE id_number = %s", (tanlov,))
        mahsulot = cur.fetchone()

        if mahsulot is None:
            print("Bunday mahsulot topilmadi.")
            continue

        title, mavjud_miqdor = mahsulot

        if kg > mavjud_miqdor:
            print(f"Bizda faqat {mavjud_miqdor} kg {title} bor.")
            continue


        cur.execute("SELECT quantity FROM KORZINKA WHERE card_number = %s AND product_id = %s", (a, tanlov))
        mavjud = cur.fetchone()
        if mavjud:
            yangi_miqdor = mavjud[0] + kg
            cur.execute("UPDATE KORZINKA SET quantity = %s WHERE card_number = %s AND product_id = %s", (yangi_miqdor, a, tanlov))
        else:
            cur.execute("INSERT INTO KORZINKA (card_number, product_id, quantity) VALUES (%s, %s, %s)", (a, tanlov, kg))


        cur.execute("UPDATE MAHSULOTLAR SET balance = balance - %s WHERE id_number = %s", (kg, tanlov))
        conn.commit()
        print(f"{kg} kg {title} savatchaga qo‘shildi.")

    
    print("\nSizning karzinkangiz:")
    cur.execute("""
        SELECT M.title, K.quantity
        FROM KORZINKA K
        JOIN MAHSULOTLAR M ON K.product_id = M.id_number
        WHERE K.card_number = %s
    """, (a,))
    karzinka = cur.fetchall()
    for nom, miqdor in karzinka:
        print(f" - {nom}: {miqdor} kg")

    c = int(input("\nKarzinkani tozalash - 1\nHaridni tasdiqlash - 2\nTanlang: "))
    if c == 1:
        cur.execute("DELETE FROM KORZINKA WHERE card_number = %s", (a,))
        conn.commit()
        print("Karzinka tozalandi.")
    elif c == 2:
        print("Haridingiz uchun rahmat!")

    yana = input("Yana xarid qilasizmi? (ha/yo‘q): ").lower()
    if yana != "ha":
        break
