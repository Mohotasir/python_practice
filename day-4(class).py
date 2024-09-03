class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print("my name is  " + self.name)


f1 = Family("Tasin", 22)
f1.printname()


class House(Family):
   def __init__(self, name, age, address):
    # Family.__init__(self, name, age)
    super().__init__(name, age)
# super() function that will make the child class inherit all the methods and properties from its parent

# add a property to House class
    self.address = address


h1 = House("bari", 33, 5666)
print(h1.address)
