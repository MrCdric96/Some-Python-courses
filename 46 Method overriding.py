# Method overriding : can be achieved to change functionality of parent class
class Parent:
    def func1(self):
        print("This is function 1")


class Child(Parent):
    def func1(self):
        print("This is function 2")

ob = Child()
ob.func1()