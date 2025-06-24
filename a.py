class Car:
    def __init__(self,brand,model,price,horsepower):
        self.brand=brand
        self.model=model
        self.price=price
        self.horspower=horsepower
    @property
    def info(self):
        return self.horspower
    @info.setter
    def infoset(self):
        if 500<self.horspower>100:
            self.horspower=900
        return self.brand.model.price.horsepower



c1=Car("BMW","M3","180000",300)
