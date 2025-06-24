class Student:
    def __init__(self, name):
        self.name = name


class Xona:
    def __init__(self, room_number):
        self.room_number = room_number
        self.students = []

    def bush_xona(self):
        return len(self.students) == 0

    def full_xona(self):
        return len(self.students) >= 10

    def active_xona(self):
        return len(self.students) < 10

    def student_qushish(self, student):
        if self.active_xona():
            self.students.append(student)
            print(f"{student.name} xonaga qushildi")
        else:
            print("xona tulgan0")

    def remove_student(self, student_ism):
        for student in self.students:
            if student.name == student_ism:
                self.students.remove(student)
                print(f"{student.name} xonadan o'chirildi")
            else:
                print("bu ismli student topilmadi")

    def student_shows(self):
        if self.students:
            print(f"{self.room_number} xonasidagi studentlar")
            for student in self.students:
                print(student.name, end="  ")
        else:
            print(f"{self.room_number} xonasi bush")


class TTJ:
    def __init__(self, nomi, tel_raqami, manzil):
        self.nomi = nomi
        self.tel_raqami = tel_raqami
        self.manzil = manzil
        self.rooms = []

    def xona_qushish(self, room_number,title,qavat):
        bor = False
        for room in self.rooms:
            if room.room_number == room_number:
                bor = True
        if not bor:
            self.rooms.append(Xona(room_number))

    def xona_topamiz(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
            else:
                return None

    def active_room_kursatish(self):
        print("======Active xonalar========")
        for room in self.rooms:
            if room.active_xona():
                print(f"{room.room_number} - xona , {len(room.students)} ta student")

    def bush_room_kursatish(self):
        for room in self.rooms:
            if room.bush_xona():
                print(f"{room.room_number} - xona , {qavat}-qavat, {title}-nomli")

    def student_room_qush(self, room_number, student_name):
        room = self.xona_topamiz(room_number)
        if room:
            student = Student(student_name)
            room.student_qushish(student)
        else:
            print("xona topilmadi")

    def remove_student_room(self, room_number, student_name):
        room = self.xona_topamiz(room_number)
        if room:
            room.remove_student(student_name)
        else:
            print("xona topilmadi")

    def lis_room_student(self, room_number):
        room = self.xona_topamiz(room_number)
        if room:
            room.student_shows()
        else:
            print("xona topilmadi")


ttj = TTJ("Yoshlar TTJ", "+998 90 123-45-67", "Toshkent shahri, Chilonzor-9")
print("Yoshlar TTJ -- mehmonxonasiga xush kelibsiz")
print("(1-5) gacha tanlang")
while True:
    print("1.Xona qushish")
    print("2.Student qushish")
    print("3.Active xonalarni kurish")
    print("4.Bush xonalarni kursatish")
    print("5.Studentni olib tashlash")
    t = input("tanlov: ")
    if t == "1":
        title = input("title: ")
        qavat = int(input("qavat: "))
        room_numbers = int(input("room_number: "))
        ttj.xona_qushish(room_numbers, title, qavat)
    elif t== "2":
        print("Student qushasiz va malumotlarini kiriting")
        student_name = input("ism: ")
        student_name2 = input("ism: ")
        room_number = room_numbers
        ttj.student_room_qush(room_number,student_name)
        ttj.student_room_qush(room_number,student_name2)
        print(f"{student_name} xonaga qushildi")
    elif t == "3":
        print(ttj.active_room_kursatish())
    elif t == "4":
        print(ttj.bush_room_kursatish())
    elif t == "5":
        print("Student haqida malumot kiriting")
        student_name = input("Talana ismini kiriting: ")
        room_number = room_numbers
        ttj.remove_student_room(room_number,student_name)
        print("Talaba olib tashlandi")
    else:
        print("Dasturdan chiqildi")
        break
