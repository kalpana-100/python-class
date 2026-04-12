#Object-Oriented Programming (OOP) in Python is a way of writing programs using objects and classes, 
    # instead of just functions and variables. 
    # It helps organize code better, especially for large projects.
    #1. What is a Class?
    #A class is like a blueprint for creating objects.
    #2. What is an Object?
    #An object is an instance of a class.  instance= object created from a class.
    # 3. Constructor (__init__) = Used to initialize object data.
    # Four Pillars of OOP
     # 1. Encapsulation (Data Hiding) = hiding data so others can’t change it directly.
     # 2. Inheritance = One class can use properties of another.
     # 3. Polymorphism = Same function name, different behavior.
     # 4. Abstraction = Hiding complex details and showing only necessary parts.
     #self keyword: self helps the object use its own data.

class Person: #class          
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def greet(self):
    #     return f"Hello,my name is {self.name} and I am {self.age} years old."
    
    def __str__(self):  
        return f"Person(name={self.name},age={self.age})"
    
# p1=Person()  # p1 is an object of class person.
# p1.name="Ram"
# p1.age=20

p1=Person("Ram", 20)
print(p1)

p2=Person("sita",22)
print(p2)
# print(p1.greet())  #output: Hello, my name is Ram and I am 20 years old.

# p2=Person()  # p2 is an object of class person.
# p2.name="Sita"
# p2.age=22

# print(p2.greet())  #output: Hello, my name is Sita and I am 22 years old.

