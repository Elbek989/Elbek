

def talaba(ism, familiya, yil, universitet, viloyat, yunalish):
    return (f"{ism} {familiya}, {yil}-yilda tug‘ilgan. {viloyat} viloyatida yashaydi. {universitet} universitetining "
            f"{yunalish} yo‘nalishiga ariza.")


a = input("Ismingizni kiriting: ")
b = input("Familiyangizni kiriting: ")
c = input("Tug‘ilgan yilingizni kiriting: ")
d = input("Universitet nomini kiriting: ")
e = input("Viloyatingizni kiriting: ")
f = input("Yo‘nalishingizni kiriting: ")


natija = talaba(a, b, c, d, e, f)
print(natija)

