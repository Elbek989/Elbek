import time
import re
def time_tracker(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Dastur ishlash vaqti: {elapsed:.2f} soniya")
        return result
    return wrapper

class CONTACT_MANAGER:
    def __init__(self,name,phonenumber):
        self.name=name
        self.phonenumber=phonenumber
p1=CONTACT_MANAGER("Ali","+998992222345")
p2=CONTACT_MANAGER("Vali","+998923454321")
a=[p1,p2]
pattern = r'^\+998(90|91|93|94|95|97|98|99|88|33)\d{7}$'

@time_tracker
def run_contact_manager():
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

if __name__ == "__main__":
    run_contact_manager()


