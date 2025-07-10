# import time
# import re
#
#
# class CONTACT_MANAGER:
#     def __init__(self,name,phonenumber):
#         self.name=name
#         self.phonenumber=phonenumber
#         self.messeges=[]
# p1=CONTACT_MANAGER("Ali","+998992222345")
# p2=CONTACT_MANAGER("Vali","+998923454321")
# a=[p1,p2]
# pattern = r'^\+998(90|91|93|94|95|97|98|99|88|33)\d{7}$'
#
#
# while True:
#     h=int(input("Contact managerni tanlash-1\nSMS manager tanlash-2\nChiqish-3\nRaqam kiriting-----------"))
#
#     if h==1:
#         while True:
#             s=int(input("Malumotlarni kurish-1\nMalumot qushish-2\nChiqish-3\nsms larni uqish-4\nsms yuborish-5"
#                         "\nRaqam kiriting-----------"))
#             if s==1:
#                 for i in a:
#                     print(i.name,i.phonenumber)
#             elif s==2:
#                 o = input("Ismni kiriting: ")
#                 while True:
#                     t = input("Telefon raqamni kiriting (+998 bilan): ")
#                     if re.fullmatch(pattern, t):
#                         d = CONTACT_MANAGER(o, t)
#                         a.append(d)
#                         print(" Ma'lumot qo‘shildi.")
#                         break
#                     else:
#                         print(" Noto‘g‘ri raqam! Qaytadan urinib ko‘ring.")
#             elif s==3:
#                 print("Dasturdan chiqildi!!!")
#                 break
#             elif s==4:
#                 uqish=input("telefon raqamni kiriting:")
#
#                 for i in a:
#                     if uqish == i.phonenumber:
#                         print(i.messeges)
#                     else:
#                         print("kiritilgan raqam hato")
#             elif s==5:
#                 tel = input("SMS yubormoqchi bo‘lgan raqamni kiriting: ")
#                 found = False
#                 for i in a:
#                     if tel == i.phonenumber:
#                         sms = input("SMS ni kiriting: ")
#                         i.messeges.append(sms)
#                         print("SMS yuborildi.")
#                         found = True
#                         break
#                 if not found:
#                     print("Xato raqam kiritilgan!")
#
#
#
#     elif h == 2:
#         tel = input("SMS yubormoqchi bo‘lgan raqamni kiriting: ")
#         found = False
#         for i in a:
#             if tel == i.phonenumber:
#                 sms = input("SMS ni kiriting: ")
#                 i.messeges.append(sms)
#                 print("SMS yuborildi.")
#                 found = True
#                 break
#         if not found:
#             print("Xato raqam kiritilgan!")
#
#
#
#
#
#
#
#
#
#
#
#
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

cur.execute("DROP TABLE IF EXISTS Kartalar")
cur.execute("""
CREATE TABLE Kartalar (

     id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    phonenumber VARCHAR NOT NULL,
    salon_id INTEGER REFERENCES autosalonlar(id)
)
""")


while True:
    h=int(input("Contact managerni tanlash-1\nSMS manager tanlash-2\nChiqish-3\nRaqam kiriting-----------"))

    if h==1:
        while True:
            s=int(input("Malumotlarni kurish-1\nMalumot qushish-2\nChiqish-3\nsms larni uqish-4\nsms yuborish-5"
                        "\nRaqam kiriting-----------"))
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
            elif s==4:
                uqish=input("telefon raqamni kiriting:")

                for i in a:
                    if uqish == i.phonenumber:
                        print(i.messeges)
                    else:
                        print("kiritilgan raqam hato")
            elif s==5:
                tel = input("SMS yubormoqchi bo‘lgan raqamni kiriting: ")
                found = False
                for i in a:
                    if tel == i.phonenumber:
                        sms = input("SMS ni kiriting: ")
                        i.messeges.append(sms)
                        print("SMS yuborildi.")
                        found = True
                        break
                if not found:
                    print("Xato raqam kiritilgan!")



    elif h == 2:
        tel = input("SMS yubormoqchi bo‘lgan raqamni kiriting: ")
        found = False
        for i in a:
            if tel == i.phonenumber:
                sms = input("SMS ni kiriting: ")
                i.messeges.append(sms)
                print("SMS yuborildi.")
                found = True
                break
        if not found:
            print("Xato raqam kiritilgan!")














