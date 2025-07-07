import psycopg2


conn = psycopg2.connect(
    dbname="hometask",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS cars")
cur.execute("DROP TABLE IF EXISTS autosalonlar")


cur.execute("""
CREATE TABLE autosalonlar (
    id INTEGER PRIMARY KEY,
    brand VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    city VARCHAR NOT NULL
)
""")


cur.execute("""
CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    model VARCHAR NOT NULL,
    brand VARCHAR NOT NULL,
    salon_id INTEGER REFERENCES autosalonlar(id)
)
""")


salons = [
    (1, "BMW", "+998938000747", "Toshkent"),
    (2, "Mercedes", "+998901112233", "Toshkent"),
    (3, "Chevrolet", "+998977776655", "Samarqand"),
    (4, "Hyundai", "+998935551234", "Buxoro"),
    (5, "Kia", "+998935556677", "Namangan"),
    (6, "Toyota", "+998901234567", "Andijon"),
    (7, "Lexus", "+998998889900", "Farg'ona"),
    (8, "Audi", "+998994443322", "Xorazm"),
    (9, "Ford", "+998935553333", "Jizzax"),
    (10, "Volkswagen", "+998977771111", "Qarshi")
]

cur.executemany("""
INSERT INTO autosalonlar (id, brand, phone, city)
VALUES (%s, %s, %s, %s)
""", salons)


cars = [
    ("X5", "BMW", 1),
    ("C-Class", "Mercedes", 2),
    ("Malibu", "Chevrolet", 3),
    ("Tucson", "Hyundai", 4),
    ("K5", "Kia", 5),
    ("Camry", "Toyota", 6),
    ("RX 350", "Lexus", 7),
    ("A6", "Audi", 8),
    ("Mustang", "Ford", 9),
    ("Passat", "Volkswagen", 10)
]

cur.executemany("""
INSERT INTO cars (model, brand, salon_id)
VALUES (%s, %s, %s)
""", cars)

conn.commit()


while True:
    tanlov = int(input(":1 - Avtosalonlar ro'yxati\n2 - Avtomobillar ro'yxati\n3 - Chiqish\nTanlang: "))

    if tanlov == 1:
        print("\n---  AVTOSALONLAR ---")
        cur.execute("SELECT * FROM autosalonlar")
        for row in cur.fetchall():
            print(row)
        while True:
            tanlov2=int(input("1-Avtosalon qushish\n2-Autosalon uchirish\n3-Ortga qaytish"))
            if tanlov2==1:
                new_id = int(input("ID raqami: "))
                new_brand = input("Brandi: ")
                new_phone = input("Telefon raqami: ")
                new_city = input("Shahar: ")

                try:
                    cur.execute("""
                        INSERT INTO autosalonlar (id, brand, phone, city)
                        VALUES (%s, %s, %s, %s)
                        """, (new_id, new_brand, new_phone, new_city))
                    conn.commit()
                    print("Avtosalon muvaffaqiyatli qo‘shildi!")
                except psycopg2.errors.UniqueViolation:
                    conn.rollback()
                    print("Bu ID allaqachon mavjud! Boshqa ID kiriting.")
                except Exception as e:
                    conn.rollback()
                    print(" Xatolik:", e)
            elif tanlov2==2:
                delete_id = int(input(" O‘chirmoqchi bo‘lgan avtosalon ID sini kiriting: "))

                cur.execute("SELECT * FROM autosalonlar WHERE id = %s", (delete_id,))
                salon = cur.fetchone()

                if salon:
                    cur.execute("DELETE FROM cars WHERE salon_id = %s", (delete_id,))
                    cur.execute("DELETE FROM autosalonlar WHERE id = %s", (delete_id,))
                    conn.commit()
                    print(" Avtosalon va bog‘liq mashinalar o‘chirildi.")
                else:
                    print(" Bunday avtosalon topilmadi.")
            elif tanlov2==3:
                break
            else:
                print(" Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")
    elif tanlov == 2:
        print("\n---  AVTOMOBILLAR ---")
        cur.execute("""
        SELECT cars.model, cars.brand, autosalonlar.city
        FROM cars
        JOIN autosalonlar ON cars.salon_id = autosalonlar.id
        """)
        for row in cur.fetchall():
            print(f"Model: {row[0]}, Brand: {row[1]}, Joylashuv: {row[2]}")
        while True:
            tanlov3=int(input("1-mashina qushish\n2-mashinani ruyhatdan chiqarish\n3-ortga qaytish"))
            if tanlov3==1:
                new_model = input("Model: ")
                new_brand = input("Brendi: ")
                new_salon_id = int(input("Avtosalon ID: "))

                try:
                    cur.execute("""
                        INSERT INTO cars (model, brand, salon_id)
                        VALUES (%s, %s, %s)
                    """, (new_model, new_brand, new_salon_id))
                    conn.commit()
                    print("Mashina muvaffaqiyatli qo‘shildi!")
                except psycopg2.errors.ForeignKeyViolation:
                    conn.rollback()
                    print(" Bunday avtosalon ID topilmadi! Iltimos, to‘g‘ri ID kiriting.")
                except Exception as e:
                    conn.rollback()
                    print(" Xatolik:", e)
            elif tanlov3==2:
                delete_car_id = int(input("🗑 O‘chirmoqchi bo‘lgan mashina ID sini kiriting: "))

                cur.execute("SELECT * FROM cars WHERE id = %s", (delete_car_id,))
                car = cur.fetchone()

                if car:
                    cur.execute("DELETE FROM cars WHERE id = %s", (delete_car_id,))
                    conn.commit()
                    print(" Mashina muvaffaqiyatli o‘chirildi.")
                else:
                    print(" Bunday mashina topilmadi.")
            elif tanlov3==3:
                break
            else:
                print(" Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")

    elif tanlov == 3:
        print(" Dasturdan chiqildi.")
        break

    else:
        print(" Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")

cur.close()
conn.close()
