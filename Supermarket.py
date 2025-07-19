import psycopg2


conn = psycopg2.connect(
    dbname="hometask",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS USERS (
    name VARCHAR NOT NULL,
    card_number BIGINT PRIMARY KEY
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS MAHSULOTLAR (
    title VARCHAR NOT NULL,
    balance INTEGER NOT NULL,
    id_number INTEGER PRIMARY KEY,
    price INTEGER NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS KARTALAR (
    balance INTEGER NOT NULL,
    card_number BIGINT PRIMARY KEY,
    password INTEGER NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS KORZINKA (
    card_number BIGINT REFERENCES USERS(card_number),
    product_id INTEGER REFERENCES MAHSULOTLAR(id_number),
    quantity INTEGER NOT NULL
)
""")


USERS = [("Ali", 33333333333333), ("Vali", 22222222222222), ("Elbek", 11111111111111)]
MAHSULOTLAR = [("Olma", 40, 100, 22000), ("Banan", 50, 129, 35000), ("Apelsin", 75, 101, 25000)]
KARTALAR = [(1400000, 33333333333333, 1111), (1400000, 22222222222222, 2222), (1500000, 11111111111111, 3333)]

for user in USERS:
    cur.execute("INSERT INTO USERS (name, card_number) VALUES (%s, %s) ON CONFLICT DO NOTHING", user)

for mahsulot in MAHSULOTLAR:
    cur.execute("INSERT INTO MAHSULOTLAR (title, balance, id_number, price) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING", mahsulot)

for karta in KARTALAR:
    cur.execute("INSERT INTO KARTALAR (balance, card_number, password) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", karta)

conn.commit()

print("=== SUPERMARKETGA XUSH KELIBSIZ ===")


while True:
    try:
        a = int(input("Karta raqamingizni kiriting: "))
    except ValueError:
        print("Faqat raqam kiriting.")
        continue

    cur.execute("SELECT * FROM KARTALAR WHERE card_number = %s", (a,))
    karta = cur.fetchone()

    if not karta:
        print("Bunday karta topilmadi.")
        continue

    print("Karta topildi.")

    while True:
        print("\n--- MAHSULOTLAR ---")
        cur.execute("SELECT id_number, title, balance, price FROM MAHSULOTLAR")
        mahsulotlar = cur.fetchall()
        for id, title, balans, price in mahsulotlar:
            print(f"{title} (id={id}) - {balans} kg - {price} so'm/kg")

        try:
            tanlov = int(input("Mahsulot ID sini kiriting (0 - savatga o‘tish): "))
        except ValueError:
            print("Noto‘g‘ri kiritildi.")
            continue

        if tanlov == 0:
            break

        cur.execute("SELECT title, balance, price FROM MAHSULOTLAR WHERE id_number = %s", (tanlov,))
        mahsulot = cur.fetchone()
        if mahsulot is None:
            print("Bunday mahsulot mavjud emas.")
            continue

        title, mavjud_miqdor, narx = mahsulot

        try:
            kg = int(input("Necha kg olmoqchisiz: "))
        except ValueError:
            print("Faqat raqam kiriting.")
            continue

        if kg > mavjud_miqdor:
            print(f"Bizda {mavjud_miqdor} kg {title} mavjud.")
            continue

        umumiy_narx = narx * kg
        print(f"Umumiy narx: {umumiy_narx} so'm")

        cur.execute("SELECT quantity FROM KORZINKA WHERE card_number = %s AND product_id = %s", (a, tanlov))
        mavjud = cur.fetchone()
        if mavjud:
            yangi_miqdor = mavjud[0] + kg
            cur.execute("UPDATE KORZINKA SET quantity = %s WHERE card_number = %s AND product_id = %s",
                        (yangi_miqdor, a, tanlov))
        else:
            cur.execute("INSERT INTO KORZINKA (card_number, product_id, quantity) VALUES (%s, %s, %s)",
                        (a, tanlov, kg))

        cur.execute("UPDATE MAHSULOTLAR SET balance = balance - %s WHERE id_number = %s", (kg, tanlov))
        conn.commit()
        print(f"{kg} kg {title} savatga qo‘shildi.")


    print("\n Sizning savatingiz:")
    cur.execute("""
        SELECT M.title, M.price, K.quantity
        FROM KORZINKA K
        JOIN MAHSULOTLAR M ON K.product_id = M.id_number
        WHERE K.card_number = %s
    """, (a,))
    karzinka = cur.fetchall()

    if not karzinka:
        print("Savat bo‘sh.")
    else:
        jami = 0
        for nom, narx, miqdor in karzinka:
            summa = narx * miqdor
            jami += summa
            print(f"{nom}: {miqdor} kg × {narx} = {summa} so'm")
        print(f"Jami summa: {jami} so'm")

    c = int(input("\n1 - Savatni tozalash\n2 - Xaridni tasdiqlash\n3 - Orqaga\nTanlang: "))
    if c == 1:
        cur.execute("DELETE FROM KORZINKA WHERE card_number = %s", (a,))
        conn.commit()
        print("Savat tozalandi.")
    elif c == 2:
        cur.execute("SELECT balance FROM KARTALAR WHERE card_number = %s", (a,))
        balans = cur.fetchone()[0]
        if balans >= jami:
            cur.execute("UPDATE KARTALAR SET balance = %s WHERE card_number = %s", (balans - jami, a))
            cur.execute("DELETE FROM KORZINKA WHERE card_number = %s", (a,))
            conn.commit()
            print(" Xarid muvaffaqiyatli! Yangi balans:", balans - jami, "so'm")
        else:
            print(" Mablag' yetarli emas.")

    yana = input("\nYana xarid qilasizmi? (ha/yo‘q): ").lower()
    if yana == "ha":
        continue
    if yana=="yo'q":
        break
