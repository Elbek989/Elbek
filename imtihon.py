class Person:
    def __init__(self, username, surname, age, phonenumber):
        self.username = username
        self.surname = surname
        self.age = age
        self.phonenumber = phonenumber
        self.card = []
        self.korzinka = []
        self.korzinka.append(object)


class Card:
    def __init__(self, user, number, code, balance, activetime):
        self.user = user
        self.number = number
        self.code = code
        self.balance = balance
        self.activetime = activetime


class Supermarket:
    def __init__(self, location, hisobraqam, title):
        self.location = location
        self.hisobraqam = hisobraqam

        self.title = title
        self.mahsulotlar = []

    def mahsulot_qoshish(self, mahsulot: object):
        self.mahsulotlar.append(mahsulot)


class Mahsulot:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


user2 = Person("ali4", "val1", "20", "+998990009931")
card = Card("ali4", "220000", 0000, 100000, "05/28")
user1 = Person("ali5", "vali1", "23", "+998990004311")
card1 = Card("ali5", "330000", 1111, 77000, "08/20")
user3 = Person("ali3", "vai1", "30", "+998990009211")
card2 = Card("ali3", "330090", 2222, 700000, "08/10")
user4 = Person("ali1", "val", "20", "+998990009944")
card3 = Card("ali1", "330001", 3333, 1770000, "05/20")
user5 = Person("ali2", "vli1", "50", "+998990039911")
card4 = Card("ali2", "330033", 4444, 7740000, "08/21")
users = [user1, user2, user3, user4, user5]
cards = [card, card4, card1, card2, card3]


def supermarket_manager():
    supermarket = Supermarket("yunusobod", 1000, "MAKRO")
    mahsulot = Mahsulot("Olma", 25000, 100)
    mahsulot1 = Mahsulot("Anor", 35000, 100)
    mahsulot2 = Mahsulot("Olcha", 30000, 100)
    supermarket.mahsulot_qoshish(mahsulot)
    supermarket.mahsulot_qoshish(mahsulot1)
    supermarket.mahsulot_qoshish(mahsulot2)
    user = [user1, user2, user3, user4, user5]


supermarket = Supermarket("yunusobod", 1000, "MAKRO")
mahsulot = Mahsulot("Olma", 25000, 100)
mahsulot1 = Mahsulot("Anor", 35000, 100)
mahsulot2 = Mahsulot("Olcha", 30000, 100)
mevalar = [mahsulot.title, mahsulot1.title, mahsulot2.title]


def supermarket_login():
    name = input("Usernameni kiriting:")
    for item in users:
        if item.username == name:
            while True:

                kod = int(input("1.mahsulotlarni kurish:\n2.karzinkani kurish\n4.chiqish:"))
                if kod == 1:
                    a = 1
                    for i in mevalar:
                        print(a, ".", i)
                        a += 1
                    haridlar = int(input("Harid qilmoqchi bulgan mevangizni tartib raqmini kiriting:\nkarzinkani kurish uchun 5 ni bosing:"))
                    if haridlar==1 or haridlar==2 or haridlar==3:

                        kilo = int(input("miqdorini kiriting<<kg da>>:"))
                    if haridlar == 1 and kilo < mahsulot.quantity - 5 or haridlar == 2 and kilo < mahsulot1.quantity - 5 or haridlar == 3 and kilo < mahsulot2.quantity - 5:
                        if haridlar == 1:
                            narx = mahsulot.price * kilo
                            print(narx, "so'm")
                            pinkod = int(input("plastik kartangizni kodini kiriting:"))

                            for c in cards:
                                if c.user == item.username:
                                    if c.code == pinkod:
                                        if c.balance >= narx:
                                            tanlov = int(input("haridni  tasdiqlash uchun 1 ni bosing"))
                                            if tanlov == 1:
                                                c.balance = c.balance - narx
                                                supermarket.hisobraqam = supermarket.hisobraqam + narx
                                                print("haridingiz tasdiqlandi, haridingiz uchun rahmat!!!")
                                                item.korzinka.append(mahsulot.title)





                                        else:
                                            print("hisobingizda mablag yetarli emas")
                                            break
                                    else:
                                        print("pin kod hato!!!")
                                        break

                        if haridlar == 2:

                            narx = mahsulot1.price * kilo
                            print(narx, "so'm")
                            pinkod = int(input("plastik kartangizni kodini kiriting:"))
                            for c in cards:
                                if c.user == name:
                                    if c.code == pinkod:
                                        if c.balance >= narx:
                                            tanlov = int(input("haridni  tasdiqlash uchun 1 ni bosing"))
                                            if tanlov == 1:
                                                c.balance = c.balance - narx
                                                supermarket.hisobraqam = supermarket.hisobraqam + narx

                                                print("haridingiz tasdiqlandi, haridingiz uchun rahmat!!!")
                                                item.korzinka.append( mahsulot1.title)

                                        else:
                                            print("hisobingizda mablag yetarli emas")
                                            break
                                    else:
                                        print("pin kod hato!!!")
                                        break

                        if haridlar == 3:

                            narx = mahsulot.price * kilo
                            print(narx, "so'm")
                            pinkod = int(input("plastik kartangizni kodini kiriting:"))
                            for c in cards:
                                if c.user == item.username:
                                    if c.code == pinkod:
                                        if c.balance >= narx:
                                            tanlov = int(input("haridni  tasdiqlash uchun 1 ni bosing"))
                                            if tanlov == 1:
                                                c.balance = c.balance - narx
                                                supermarket.hisobraqam = supermarket.hisobraqam + narx
                                                print("haridingiz tasdiqlandi, haridingiz uchun rahmat!!!")
                                                item.korzinka.append( mahsulot2.title)

                                        else:
                                            print("hisobingizda mablag yetarli emas")
                                            break
                                    else:
                                        print("pin kod hato!!!")
                                        break
                        if haridlar==5:
                            print(item.korzinka)






                if kod == 2:
                    print(item.korzinka)

                if kod == 4:
                    break

    else:
        print("kiritilgan ism hato!!!")



supermarket_login()
