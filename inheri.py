# Inheritance in Python is an OOP (Object-Oriented Programming) concept where one 
# class (child class) can use the properties and methods of another class (parent class).
class Pet:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def belongs(self):
        return f"{self.name} is a {self.species}"
    
class Dog(Pet):
    def __init__(self,name,species):
        super().__init__(name,species)

class Cat(Pet):
    def __init__(self,name,species):
        super().__init__(name,species)

dog1=Dog("Buddy","Dog")
print(dog1.belongs())

