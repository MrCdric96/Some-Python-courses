class Car():
    def __init__(self, model_name, year, price):
        self.model_name = model_name
        self.year = year
        self.price = price

    def price_incrase(self):
        self.price = int(self.price * 1.15)


class SuperCar(Car):
    def __init__(self, model_name, year, price, cc):
        super.__init__(model_name, year, price)
        self.cc = cc 


honda = SuperCar("City", 2017, 1000000)
tata = Car("Bolt", 2016, 600000)

honda.cc = 1500
#print(help(honda))
honda.price_incrase()
print(honda.price)



