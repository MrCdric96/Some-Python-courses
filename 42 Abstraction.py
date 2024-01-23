from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def price_increase(self):
        pass


class SuperCar(Car):
    def __init__(self, model_name, year, price, cc):
        super.__init__(model_name, year, price)
        self.cc = cc
    def price_increase(self):
        self.price = int(self.price * 2)

honda = SuperCar("City", 2017, 1000000)
tata = Car("Bolt", 2016, 600000)

honda.cc = 1500
honda.price_increase()
print(honda.price)