class Car():
    def __init__(self, model_name, year_of_manufacture, price):
        self.model_name = model_name
        self.year_of_manufacture = year_of_manufacture
        self.price = price

    def price_increase(self):
        self.price = int(self.price * 1.15)


toyota = Car("Land Cruiser HJZ6", 2020, 40000)
print(toyota.__dict__)

land_rover = Car("Range Rover", 2020, 80000)
print(land_rover.__dict__)

print(toyota.price)
toyota.price_increase()
print(toyota.price)

print(land_rover.price)
land_rover.price_increase()
print(land_rover.price)

