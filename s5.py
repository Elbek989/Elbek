class Apple:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
app=Apple("olma",99)
print(Apple)

class App(Apple):
    def __init__(self,title):
        super().__init__()
        self.title=title

ap=App("olma",99,"www")

