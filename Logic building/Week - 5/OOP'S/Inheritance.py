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
class Puppy(Dog):
    def speak(self):
        return "Puppy yaps"
puppy = Puppy()
print(puppy.speak())  # Output: Puppy yaps
print(isinstance(puppy, Dog))  # Output: True
print(isinstance(puppy, Animal))  # Output: True
print(issubclass(Puppy, Dog))  # Output: True
print(issubclass(Puppy, Animal))  # Output: True
print(issubclass(Dog, Puppy))  # Output: False
print(issubclass(Animal, Dog))  # Output: False
print(issubclass(Animal, Puppy))  # Output: False
print(issubclass(Dog, Cat))  # Output: False
print(issubclass(Cat, Dog))  # Output: False
print(issubclass(Cat, Animal))  # Output: True

# Hierarchical inheritance
class Bird(Animal):
    def speak(self):
        return "Bird chirps"
class Fish(Animal):
    def speak(self):
        return "Fish blubs"
bird = Bird()
fish = Fish()  
print(bird.speak())  # Output: Bird chirps
print(fish.speak())  # Output: Fish blubs
print(isinstance(bird, Animal))  # Output: True
print(isinstance(fish, Animal))  # Output: True
print(issubclass(Bird, Animal))  # Output: True
print(issubclass(Fish, Animal))  # Output: True
print(issubclass(Bird, Fish))  # Output: False
print(issubclass(Fish, Bird))  # Output: False
print(issubclass(Bird, Dog))  # Output: False
print(issubclass(Dog, Bird))  # Output: False
print(issubclass(Fish, Dog))  # Output: False
print(issubclass(Dog, Fish))  # Output: False
print(issubclass(Fish, Cat))  # Output: False
print(issubclass(Cat, Fish))  # Output: False
