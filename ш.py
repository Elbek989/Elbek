class Avtosalon:
    def __init__(self,nomi,manzil,tel):
        self.nomi = nomi
        self.manzil = manzil
        self.tel = tel
        self.base = []

class Basecar:
    def __init__(self,brand,model,year,tezlik):
        self.brand = brand
        self.model = model
        self.year = year
        self.tezlik = tezlik

class BMW(Basecar):
    def __init__(self,brand,model,year,tezlik,mintezlik):
        super().__init__(brand,model,year,tezlik)
        self.mintezlik = mintezlik

class Mercedes(Basecar):
    def __init__(self,brand,model,year,tezlik,minnarx):
        super().__init__(brand,model,year,tezlik)
        self.minnarx = minnarx

class Chevrolet(Basecar):
    def __init__(self,brand,model,year,tezlik,maxnarx):
        super().__init__(brand,model,year,tezlik)
        self.maxnarx = maxnarx
m1=BMW("BMW","m5","2011","350","20")
m2=Mercedes("Mercedes","G63","2015","300","250000$")
m3=Chevrolet("Chevrolet","Malibu","2017","300","50000$")

t=[m1,m2,m3]

print("Assallomu aleykum, avto salonimizga hush kebsiz, nma yordam kk\nBMW brandidagi avtomobillarni kurish uchun 1 ni "
      "bosing\nMercedes brandidagi avtomobillarni kurish uchun 2 ni bosing\nChevrolet brandidagi avtomobillarni kurish "
      "uchun 3 ni bosing\nAvtomobillarni tizimdan chiqarish uchun 4 ni bosing\n"
      "Tizimga avtomobil qushish uchun 5ni bosing\nChiqish uchun 0 ni bosing ")
i=int(input("soт kiriting-"))
if i==0:
    print("Dasturdan chiqildi!!!")
if i==1:
    print(m1.brand,m1.model,m1.year,m1.tezlik,m1.mintezlik)
if i==2:
    print(m2.brand, m2.model, m2.year, m2.tezlik, m2.minnarx)
if i==3:
    print(m3.brand,m3.model,m3.year,m3.tezlik,m3.maxnarx)
if i==4:
    a=input("BMW-1\nMercedes-2\nChevrolet-3")
    if i==1:
        m1="malumot topilmadi"
    if i==2:
        m2 = "malumot topilmadi"
    else:
        m3 = "malumot topilmadi"
    print("malumotlar uchirildi")
if i==5:
    print("qaysi brenddagi avtomobil kiritmoqchisiz\nBMW-1\nMersedec-2\nChevrolet-3")
    y=int(input("son kiriting:"))
    if y==1:
        m4=BMW(BMW,input("modelini kiriting-"),input("yilini kiriting:"),input("tezligini kiriting"),input("mintezlikni "
                                                                                                           "kiriting"))
    if y==2:
        m4 = Mercedes(Mercedes, input("modelini kiriting-"), input("yilini kiriting:"), input("tezligini kiriting"),
                 input("minnarxkiriting"))
        if y==3:
            m4 = Chevrolet(Chevrolet, input("modelini kiriting-"), input("yilini kiriting:"), input("tezligini kiriting"),
                          input("minnarx kiriting"))
    print("avto.qushildi")



else:
    print("Xato raqam tanadingiz!!!")



