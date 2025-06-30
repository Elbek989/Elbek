from random import randint
class TTJ:
    def __init__(self,title,phone,adress,rooms):
        self.title=title
        self.phone=phone
        self.adress=adress
        self.rooms=rooms
p1=TTJ("TTJ",9999999,"Mirzo Ulugbek","200")
bx=[]
tx=[]
ax=[]
def xona_malumot():
    for i in range(1,201):
        a=randint(0,10)

        if a==0:
            bx.append(i)
        elif a>0:
            ax.append(i)
print(xona_malumot())

print("Salom nma yordam kerak!!!"
      "Bush xonalarni kurmoqchi bulsaz 1 ni bosing."
      "activ xonalarni kurmoqchi bulsaz 2ni bosing."
      "xona malumotlarini kurmoqchi bulsaz 3ni bosing"
      "talaba qushmoqchi bulsaz 4 ni bosing"
      "talablarni royxattan chiqarmoqchi bolsangiz 5 ni bosing "
      "chiqish uchun 0 ni bosing")
p=int(input("0 dan 5 gacha son kiriting-"))
if p==0:
    print("dasturdan chiqildi!!!")
if p==1:
    print(bx,"xonalar bush")
if p==2:
    print(ax,"xonalar activ")
if p==3:
    print(ax,"xonalar activ",bx,"xonalar bush")
if p==4:
    tq=int(input("nechta talaba-"))
    print("talabalar qushildi")
if p==5:
    tc=int(input("nechta talaba-"))
    print("talabalar royhatdan chiqarildi")
if p>5:
    print("hato son tanlandi")



