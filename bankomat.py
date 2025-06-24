


class Person:
    def __init__(self,name,seria,password,balance):
        self.name = name
        self.seria=seria
        self.password=password
        self.balance=balance
p1 = Person("Elbek",1234,1111,5000)
p2 = Person("Ali",4726,2222,10000)
p3 = Person("Vali",3848,3333,100000)
a=[p1,p2,p3]



for i in range(1):
    b = int(input("Seriya raqamni kiriting-"))
    if b==p1.seria :
        k=int(input("kodni kiriting-"))
        if k==p1.password:
            print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing."
                    "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing"
                    "Agar chiqmoqchi bulsaz 0ni bosing")
            p=int(input("raqam kiriting-"))
            if p==0:
                print("dasturdan chiqildi!!!")
                break
            if p==1:
                print(p1.balance)
            if p==2:
                p1.password=int(input("Yangi parolni kiriting-"))
            if p==3:
                m=int(input("qancha ab lag yechb olmoqchisiz-"))
                if m>p1.balance:
                    print("buncha mablag mavjud emas")
                else:
                     q=p1.balance-m
                     print(q,"sum mablag qoldi")
            if p==4:
                k=int(input("qancha mablag kiritasz-"))
                j=p1.balance+k
                print("jami",j,"sum mablag buldi")
        else:
            print("kod hato qayta urinib kuring")
            k = int(input("kodni kiriting-"))
            if k == p1.password:
                print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing."
                      "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing"
                      "Agar chiqmoqchi bulsaz 0ni bosing")
                p = int(input("raqam kiriting-"))
                if p == 0:
                    print("dasturdan chiqildi!!!")

                if p == 1:
                    print(p1.balance)
                if p == 2:
                    p1.password = int(input("Yangi parolni kiriting-"))
                if p == 3:
                    m = int(input("qancha ab lag yechb olmoqchisiz-"))
                    if m > p1.balance:
                        print("buncha mablag mavjud emas")
                    else:
                        q = p1.balance - m
                        print(q, "sum mablag qoldi")
                if p == 4:
                    k = int(input("qancha mablag kiritasz-"))
                    j = p1.balance + k
                    print("jami", j, "sum mablag buldi")
            else:
                print("kod hato qayta urinib kuring")
                k = int(input("kodni kiriting-"))
                if k == p1.password:
                    print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing.\n"
                          "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing.\n"
                          "Agar chiqmoqchi bulsaz 0ni bosing")
                    p = int(input("raqam kiriting-"))
                    if p == 0:
                        print("dasturdan chiqildi!!!")

                    if p == 1:
                        print(p1.balance)
                    if p == 2:
                        p1.password = int(input("Yangi parolni kiriting-"))
                    if p == 3:
                        m = int(input("qancha ab lag yechb olmoqchisiz-"))
                        if m > p1.balance:
                            print("buncha mablag mavjud emas")
                        else:
                            q = p1.balance - m
                            print(q, "sum mablag qoldi")
                    if p == 4:
                        k = int(input("qancha mablag kiritasz-"))
                        j = p1.balance + k
                        print("jami", j, "sum mablag buldi")
                else:
                    print("juda kup muofaquyatsiz urinishlar sababli hisobingiz muzlatildi!!!")
                    break
    
    elif b == p2.seria:
        k = int(input("kodni kiriting-"))
        if k == p2.password:
            print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing."
                  "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing"
                  "Agar chiqmoqchi bulsaz 0ni bosing")
            p = int(input("raqam kiriting-"))
            if p == 0:
                print("dasturdan chiqildi!!!")
                break
            if p == 1:
                print(p2.balance)
            if p == 2:
                p2.password = int(input("Yangi parolni kiriting-"))
            if p == 3:
                m = int(input("qancha ab lag yechb olmoqchisiz-"))
                if m > p2.balance:
                    print("buncha mablag mavjud emas")
                else:
                    q = p2.balance - m
                    print(q, "sum mablag qoldi")
            if p == 4:
                k = int(input("qancha mablag kiritasz-"))
                j = p2.balance + k
                print("jami", j, "sum mablag buldi")
        else:
            print("kod hato qayta urinib kuring")
            k = int(input("kodni kiriting-"))
            if k == p2.password:
                print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing."
                      "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing"
                      "Agar chiqmoqchi bulsaz 0ni bosing")
                p = int(input("raqam kiriting-"))
                if p == 0:
                    print("dasturdan chiqildi!!!")

                if p == 1:
                    print(p2.balance)
                if p == 2:
                    p2.password = int(input("Yangi parolni kiriting-"))
                if p == 3:
                    m = int(input("qancha ab lag yechb olmoqchisiz-"))
                    if m > p2.balance:
                        print("buncha mablag mavjud emas")
                    else:
                        q = p2.balance - m
                        print(q, "sum mablag qoldi")
                if p == 4:
                    k = int(input("qancha mablag kiritasz-"))
                    j = p2.balance + k
                    print("jami", j, "sum mablag buldi")
            else:
                print("kod hato qayta urinib kuring")
                k = int(input("kodni kiriting-"))
                if k == p2.password:
                    print(
                        "Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing.\n"
                        "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing.\n"
                        "Agar chiqmoqchi bulsaz 0ni bosing")
                    p = int(input("raqam kiriting-"))
                    if p == 0:
                        print("dasturdan chiqildi!!!")

                    if p == 1:
                        print(p2.balance)
                    if p == 2:
                        p2.password = int(input("Yangi parolni kiriting-"))
                    if p == 3:
                        m = int(input("qancha ab lag yechb olmoqchisiz-"))
                        if m > p2.balance:
                            print("buncha mablag mavjud emas")
                        else:
                            q = p2.balance - m
                            print(q, "sum mablag qoldi")
                    if p == 4:
                        k = int(input("qancha mablag kiritasz-"))
                        j = p2.balance + k
                        print("jami", j, "sum mablag buldi")
                else:
                    print("juda kup muofaquyatsiz urinishlar sababli hisobingiz muzlatildi!!!")
                    break

    elif b == p3.seria:
        k = int(input("kodni kiriting-"))
        if k == p3.password:
            print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing."
                  "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing"
                  "Agar chiqmoqchi bulsaz 0ni bosing")
            p = int(input("raqam kiriting-"))
            if p == 0:
                print("dasturdan chiqildi!!!")
                break
            if p == 1:
                print(p3.balance)
            if p == 2:
                p3.password = int(input("Yangi parolni kiriting-"))
            if p == 3:
                m = int(input("qancha ab lag yechb olmoqchisiz-"))
                if m > p3.balance:
                    print("buncha mablag mavjud emas")
                else:
                    q = p3.balance - m
                    print(q, "sum mablag qoldi")
            if p == 4:
                k = int(input("qancha mablag kiritasz-"))
                j = p3.balance + k
                print("jami", j, "sum mablag buldi")
        else:
            print("kod hato qayta urinib kuring")
            k = int(input("kodni kiriting-"))
            if k == p3.password:
                print("Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing."
                      "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing"
                      "Agar chiqmoqchi bulsaz 0ni bosing")
                p = int(input("raqam kiriting-"))
                if p == 0:
                    print("dasturdan chiqildi!!!")

                if p == 1:
                    print(p3.balance)
                if p == 2:
                    p3.password = int(input("Yangi parolni kiriting-"))
                if p == 3:
                    m = int(input("qancha ab lag yechb olmoqchisiz-"))
                    if m > p3.balance:
                        print("buncha mablag mavjud emas")
                    else:
                        q = p3.balance - m
                        print(q, "sum mablag qoldi")
                if p == 4:
                    k = int(input("qancha mablag kiritasz-"))
                    j = p3.balance + k
                    print("jami", j, "sum mablag buldi")
            else:
                print("kod hato qayta urinib kuring")
                k = int(input("kodni kiriting-"))
                if k == p3.password:
                    print(
                        "Agar balansni kurmoqchi bulsaz 1ni bosing.\n Agar parolni uzgartirmoqchi bulsaz 2ni bosing.\n"
                        "Aagar mablag yechb olmoqchi bulsaz 3ni bosing.\n Agar mablag kiritmoqchi bulsaz 4ni bosing.\n"
                        "Agar chiqmoqchi bulsaz 0ni bosing")
                    p = int(input("raqam kiriting-"))
                    if p == 0:
                        print("dasturdan chiqildi!!!")

                    if p == 1:
                        print(p3.balance)
                    if p == 2:
                        p3.password = int(input("Yangi parolni kiriting-"))
                    if p == 3:
                        m = int(input("qancha ab lag yechb olmoqchisiz-"))
                        if m > p3.balance:
                            print("buncha mablag mavjud emas")
                        else:
                            q = p3.balance - m
                            print(q, "sum mablag qoldi")
                    if p == 4:
                        k = int(input("qancha mablag kiritasz-"))
                        j = p3.balance + k
                        print("jami", j, "sum mablag buldi")
                else:
                    print("juda kup muofaquyatsiz urinishlar sababli hisobingiz muzlatildi!!!")
                    break
    else:
        print("Bunday seriali karta mavjud emas")




