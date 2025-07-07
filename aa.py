import time
# import re
#
#
# class CONTACT_MANAGER:
#     def __init__(self, name, phonenumber):
#         self.name = name
#         self.phonenumber = phonenumber
#         self.messeges = []
#
#
# p1 = CONTACT_MANAGER("Ali", "+998992222345")
# p2 = CONTACT_MANAGER("Vali", "+998923454321")
# a = [p1, p2]
# pattern = r'^\+998(90|91|93|94|95|97|98|99|88|33)\d{7}$'
#
# while True:
#     h = int(input("Contact managerni tanlash-1\nSMS manager tanlash-2\nChiqish-3\nRaqam kiriting-----------"))
#
#     if h == 1:
#         while True:
#             s = int(input("Malumotlarni kurish-1\nMalumot qushish-2\nChiqish-3\nsms larni uqish-4\nsms yuborish-5"
#                           "\nRaqam kiriting-----------"))
#             if s == 1:
#                 for i in a:
#                     print(i.name, i.phonenumber)
#             elif s == 2:
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
#             elif s == 3:
#                 print("Dasturdan chiqildi!!!")
#                 break
#             elif s == 4:
#                 uqish = input("telefon raqamni kiriting:")
#
#                 for i in a:
#                     if uqish == i.phonenumber:
#                         print(i.messeges)
#                     else:
#                         print("kiritilgan raqam hato")
#             elif s == 5:
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
# import time,os
# from threading import Thread, current_thread
# from multiprocessing import Process,current_process
# count =100000000
# sleep=0.5
# def io_b(sec):
#     p_id=os.getpid()
#     print(f"{p_id}---{current_process().name}---{current_thread().name}----kutw")
#     time.sleep(sleep)
#     print(f"{p_id}---{current_process().name}---{current_thread().name}----kutw tugad")
# def cpu_b(k):
#     p_id = os.getpid()
#     print(f"{p_id}---{current_process().name}---{current_thread().name}----kutw")
#     while k>0:
#         k-=1
#     print(f"{p_id}---{current_process().name}---{current_thread().name}----kutw tugad")
# if __name__=="__main__":
#     s_time=time.time()
#     # io_b(sleep)
#     # io_b(sleep)
#     # t1=Thread(target=io_b,args=(sleep,))
#     # t2 = Thread(target=io_b, args=(sleep,))
#     # t1.start()
#     # t2.start()
#     # t1.join()
#     # t1.join()
#     # cpu_b(count)
#     # cpu_b(count)
#     t1 = Thread(target=cpu_b, args=(count,))
#     t2 = Thread(target=cpu_b, args=(count,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     # p1=Process(target=cpu_b, args=(count,))
#     # p2=Process(target=cpu_b, args=(count,))
#     # p1.start()
#     # p2.start()
#     # p1.join()
#     # p2.join()
#     # p1 = Process(target=io_b, args=(sleep,))
#     # p2 = Process(target=io_b, args=(sleep,))
#     # p1.start()
#     # p2.start()
#     # p1.join()
#     # p2.join()2
#
#     e_time = time.time()
#     print("vaqt = ", e_time - s_time)
# import asyncio
# import time
# async def funksya():
#     print("funksya1 bowlandi")
#     await asyncio.sleep(2)
#     print("funksya1 tugadi")
# async def funksya2():
#     print("funksya1 bowlandi")
#     await asyncio.sleep(1)
#     print("funksya1 tugadi")
# async def asosiy():
#     await asyncio.gather(funksya2(),funksya())
# asyncio.run(asosiy())
# def kvadrat(a):
#     for i in range(1,a):
#         i*=i
#         print("bajarildi")
#         yield i
# result=kvadrat(10)
# for b in result:
#     print(b)



