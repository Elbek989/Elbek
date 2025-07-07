import psycopg2



conn = psycopg2.connect(
    dbname="hometask",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Kartalar")
cur.execute("""
CREATE TABLE Kartalar (
    
     serianumber VARCHAR NOT NULL,
    phonenumber VARCHAR NOT NULL,
    balance integer NOT NULL,
    password integer NOT NULL
)
""")
Kartalar=[("19181716151413","+998949000989",2_000_000,1234),
          ("92939495657432","+998954442355",544_000,2344),
          ("93939291474744","+998921253321",1_223_000,7657),
          ("93939291474764","+998921253351",1_213_000,7057)
]
cur.executemany("""
INSERT INTO Kartalar (serianumber,phonenumber,balance,password)
VALUES (%s, %s, %s,%s)
""", Kartalar)
conn.commit()
while True:
    t1=int(input("1-Bazaga karta kiritish\n2-Karta bilan amallar\n--------------->"))
    if t1==1:
        new_serianumber=input("Kartangizni serya raqamini kiriting---")
        new_phonenumber=input("Telefon raqamni kiriting---")
        new_password=int(input("Parol kiriting---"))
        new_balance=int(input("Mablagni kiriting----"))
        try:
            cur.execute("""
                INSERT INTO Kartalar (serianumber,phonenumber,balance,password)
                VALUES (%s, %s, %s, %s)""", (new_serianumber,new_phonenumber,new_balance,new_password))
            conn.commit()
            print("Karta muofaqiyatli qushildi!")
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            print("Bu ID allaqachon mavjud! Boshqa ID kiriting.")

        except Exception as e:
            conn.rollback()
            print(" Xatolik:", e)
    elif t1 == 2:
        seriya = input("Karta seryasini kiriting--------> ")

        cur.execute("SELECT * FROM Kartalar WHERE serianumber = %s", (seriya,))
        karta = cur.fetchone()

        if karta:
            print("Karta topildi!")
            print(f"Telefon raqam: {karta[1]}")
            print(f"Balans: {karta[2]}")

            parol = int(input("Parolni kiriting: "))
            if parol == karta[3]:
                print(" Parol to‘g‘ri. Endi amallarni bajaring.")
                t3 = int(input(
                    "1 - Kartadan pul yechish\n2 - Kartani bazadan o‘chirish\n3 - Karta parolini o‘zgartirish\n>>> "))

                if t3 == 1:
                    summa = int(input("Yechmoqchi bo‘lgan summani kiriting: "))
                    if karta[2] >= summa:
                        yangi_balans = karta[2] - summa
                        cur.execute("UPDATE Kartalar SET balance = %s WHERE serianumber = %s", (yangi_balans, karta[0]))
                        conn.commit()
                        print(" Pul yechildi. Yangi balans:", yangi_balans)
                    else:
                        print(" Yetarli mablag‘ yo‘q.")

                elif t3 == 2:
                    cur.execute("DELETE FROM Kartalar WHERE serianumber = %s", (karta[0],))
                    conn.commit()
                    print(" Karta bazadan o‘chirildi.")

                elif t3 == 3:
                    yangi_parol = int(input("Yangi parolni kiriting: "))
                    cur.execute("UPDATE Kartalar SET password = %s WHERE serianumber = %s", (yangi_parol, karta[0]))
                    conn.commit()
                    print(" Parol muvaffaqiyatli o‘zgartirildi.")

                else:
                    print(" Noto‘g‘ri tanlov.")


            else:
                print("Parol noto‘g‘ri!")
        else:
            print("Bu seriya raqamli karta topilmadi.")
            break


