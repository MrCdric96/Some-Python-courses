class Parent:
    def func1(self):
        print("This is function 1")


class Child(Parent):
    def func2(self):
        super().func1()
        print("This is function 2")


ob = Child()
ob.func2()