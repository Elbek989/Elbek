from tkinter.font import names


class Student:
    def __init__(self,name,age,mail):
        self.name=name
        self.age=age
    @property
    def info(self):
        return self.name
    @info.setter
    def info(self,info_get):
        self.name=info_get


student=Student("Elbek",17,"@nnn")
info_get="Ali"
print(student.name)





