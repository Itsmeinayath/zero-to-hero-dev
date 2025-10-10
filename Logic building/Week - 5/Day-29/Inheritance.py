# Inheritance in Python
# Inheritance is a mechanism in OOP that allows a new class (derived class) to inherit
# attributes and methods from an existing class (base class).
# This promotes code reusability and establishes a hierarchical relationship between classes.
# Syntax for inheritance
# class BaseClass:
#     # base class code
# class DerivedClass(BaseClass):
#     # derived class codef
# Example of inheritance
class Animal:
    def speak(self):
        return "Animal speaks"  
class Dog(Animal):
    def speak(self):
        return "Dog barks"  
class Cat(Animal):
    def speak(self):
        return "Cat meows"
# Creating instances of the derived classes
dog = Dog() 
cat = Cat()
print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows
print(isinstance(dog, Animal))  # Output: True
print(isinstance(cat, Animal))  # Output: True
print(issubclass(Dog, Animal))  # Output: True
print(issubclass(Cat, Animal))  # Output: True

# Multi-level inheritance