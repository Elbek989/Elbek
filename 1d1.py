import re
#os.remove("B")
#if os.path.exists("B"):
#   os.remove("B")
#    print("ochdi")
#else:
  #  print("topilmadi")
class Student:
    t=0
    def __init__(self,name,year,email,phone,surname):
        self.name=name
        self.year=year
        self.phone=phone
        self.email=email
        self.surname=surname
    @property
    def info(self):
        return self.phone

    @info.setter
    def info(self,phone):
        regex=r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

        if re.match(regex,phone):
            self.phone=phone
        else:
            print("hato")








p1 = Student("Elbek", 1954, "iii", "9229999", "Nuraliyev")
# p2 = Student("Ali", 26, "eded", 10000, "Rajabov")
# p3 = Student("Vali", 13, "jjss", 100000, "uut")
# print(Student.find())
p1.info_phone="+938000747"
print(p1.info)



