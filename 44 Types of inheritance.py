#Single : when the inheritance involves one child class and one parent class
class Parent:
    def func1(self):
        print("This is function 1")


class Parent2(Parent):
    def func3(self):
        print("This is function 3")


class Parent3:
    def func4(self):
        print("This is function 4")


class Child(Parent, Parent3):
    def func2(self):
        print("this is function 2")


ob = Child()
ob.func1()
ob.func4()
#Multiple : it involves more than one parent class
#Multilevel : The child class acts as a parent class for another child class 
#Hierarchical : More than one type of inheritance