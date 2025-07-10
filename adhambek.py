# import time
# import re
# def time_tracker(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed = end_time - start_time
#         print(f"Dastur ishlash vaqti: {elapsed:.2f} soniya")
#         return result
#     return wrapper
#
# class CONTACT_MANAGER:
#     def __init__(self,name,phonenumber):
#         self.name=name
#         self.phonenumber=phonenumber
# p1=CONTACT_MANAGER("Ali","+998992222345")
# p2=CONTACT_MANAGER("Vali","+998923454321")
# a=[p1,p2]
# pattern = r'^\+998(90|91|93|94|95|97|98|99|88|33)\d{7}$'
#
# @time_tracker
# def run_contact_manager():
#     while True:
#
#         s=int(input("Malumotlarni kurish-1\nMalumot qushish-2\nChiqish-3\nRaqam kiriting-----------"))
#         if s==1:
#             for i in a:
#                 print(i.name,i.phonenumber)
#         elif s==2:
#             o = input("Ismni kiriting: ")
#             while True:
#                 t = input("Telefon raqamni kiriting (+998 bilan): ")
#                 if re.fullmatch(pattern, t):
#                     d = CONTACT_MANAGER(o, t)
#                     a.append(d)
#                     print(" Ma'lumot qo‘shildi.")
#                     break
#                 else:
#                     print(" Noto‘g‘ri raqam! Qaytadan urinib ko‘ring.")
#         elif s==3:
#             print("Dasturdan chiqildi!!!")
#             break
#         else:
#             print("Xato raqam kiritilgan!!!")
#
# if __name__ == "__main__":
#     run_contact_manager()
#
#
import time
import re
import psycopg2




conn = psycopg2.connect(
    dbname="hometask",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS CONTACT_MANAGER")
cur.execute("""
CREATE TABLE  (

     ID PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL,
    balance  NOT NULL
    
)
""")
Kartalar = [("19181716151413", "+998949000989", 2_000_000, 1234),
            ("92939495657432", "+998954442355", 544_000, 2344),
            ("93939291474744", "+998921253321", 1_223_000, 7657),
            ("93939291474764", "+998921253351", 1_213_000, 7057)
            ]
cur.executemany(


while True:

    s=int(input("Malumotlarni kurish-1\nMalumot qushish-2\nChiqish-3\nRaqam kiriting-----------"))
    if s==1:
        for i in a:
            print(i.name,i.phonenumber)
    elif s==2:
        o = input("Ismni kiriting: ")
        while True:
            t = input("Telefon raqamni kiriting (+998 bilan): ")
            if re.fullmatch(pattern, t):
                d = CONTACT_MANAGER(o, t)
                a.append(d)
                print(" Ma'lumot qo‘shildi.")
                break
            else:
                print(" Noto‘g‘ri raqam! Qaytadan urinib ko‘ring.")
    elif s==3:
        print("Dasturdan chiqildi!!!")
        break
    else:
        print("Xato raqam kiritilgan!!!")





