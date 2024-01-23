class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage

    
    def view(self):
        print(self.name, self.age)


class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "edureka"


    def view(self):
        print(self.age, self.lastname, self.name)





ob = Child(27, "Python")
ob.view()

