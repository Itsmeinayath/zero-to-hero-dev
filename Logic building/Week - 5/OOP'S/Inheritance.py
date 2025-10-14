"""
INHERITANCE in Python - Complete Guide with Practical Examples
============================================================

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows
a class (child/derived) to inherit attributes and methods from another class (parent/base).

Benefits of Inheritance:
- Code Reusability
- Method Overriding
- Extensibility
- Hierarchical Classification

Types of Inheritance:
1. Single Inheritance
2. Multiple Inheritance  
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""

print("="*60)
print("1. SINGLE INHERITANCE")
print("="*60)
print("One child class inherits from one parent class")
print("-"*40)

# Parent Class (Base Class)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started!")
        else:
            print(f"{self.brand} {self.model} is already running!")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped!")
        else:
            print(f"{self.brand} {self.model} is already stopped!")
    
    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}"

# Child Class (Derived Class)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        print(f"{self.brand} {self.model} goes BEEP BEEP! 🚗")
    
    def get_info(self):  # Method Overriding
        return f"Car: {self.brand} {self.model} with {self.doors} doors"

# Creating objects and testing Single Inheritance
print("\n--- Single Inheritance Example ---")
my_car = Car("Tesla", "Model 3", 4)
print(my_car.get_info())
my_car.start()  # Inherited method
my_car.honk()   # Own method
my_car.stop()   # Inherited method

print("\n" + "="*60)
print("2. MULTIPLE INHERITANCE")
print("="*60)
print("One child class inherits from multiple parent classes")
print("-"*40)

# First Parent Class
class Engine:
    def __init__(self):
        self.engine_type = "Internal Combustion"
    
    def start_engine(self):
        print("🔥 Engine started!")
    
    def stop_engine(self):
        print("🛑 Engine stopped!")

# Second Parent Class  
class GPS:
    def __init__(self):
        self.gps_enabled = True
    
    def get_location(self):
        return "Current Location: 40.7128° N, 74.0060° W"
    
    def navigate_to(self, destination):
        print(f"🗺️ Navigating to {destination}...")

# Child Class inheriting from both Engine and GPS
class SmartCar(Engine, GPS):
    def __init__(self, brand, model):
        Engine.__init__(self)
        GPS.__init__(self)
        self.brand = brand
        self.model = model
    
    def auto_drive(self):
        print(f"🤖 {self.brand} {self.model} is driving automatically!")

# Testing Multiple Inheritance
print("\n--- Multiple Inheritance Example ---")
smart_car = SmartCar("BMW", "i8")
smart_car.start_engine()  # From Engine class
print(smart_car.get_location())  # From GPS class
smart_car.navigate_to("New York")  # From GPS class
smart_car.auto_drive()  # Own method
smart_car.stop_engine()  # From Engine class

print("\n" + "="*60)
print("3. MULTILEVEL INHERITANCE")
print("="*60)
print("Child class inherits from parent, which inherits from grandparent")
print("-"*40)

# Grandparent Class
class Animal:
    def __init__(self, species):
        self.species = species
    
    def breathe(self):
        print("🫁 Breathing...")
    
    def move(self):
        print("🚶 Moving around...")

# Parent Class (inherits from Animal)
class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species)
        self.fur_color = fur_color
    
    def give_birth(self):
        print("👶 Giving birth to live young...")
    
    def produce_milk(self):
        print("🥛 Producing milk for offspring...")

# Child Class (inherits from Mammal, which inherits from Animal)
class Dog(Mammal):
    def __init__(self, species, fur_color, breed):
        super().__init__(species, fur_color)
        self.breed = breed
    
    def bark(self):
        print("🐕 WOOF WOOF!")
    
    def wag_tail(self):
        print("🐕 Wagging tail happily!")
    
    def get_info(self):
        return f"Dog: {self.breed} with {self.fur_color} fur"

# Testing Multilevel Inheritance
print("\n--- Multilevel Inheritance Example ---")
my_dog = Dog("Canine", "Golden", "Golden Retriever")
print(my_dog.get_info())
my_dog.breathe()      # From Animal (grandparent)
my_dog.move()         # From Animal (grandparent)  
my_dog.give_birth()   # From Mammal (parent)
my_dog.bark()         # Own method
my_dog.wag_tail()     # Own method

print("\n" + "="*60)
print("4. HIERARCHICAL INHERITANCE")
print("="*60)
print("Multiple child classes inherit from one parent class")
print("-"*40)

# Parent Class
class Shape:
    def __init__(self, color):
        self.color = color
    
    def display_color(self):
        print(f"🎨 Color: {self.color}")

# Child Class 1
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        area = 3.14159 * self.radius ** 2
        print(f"⭕ Circle Area: {area:.2f}")

# Child Class 2
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        print(f"📱 Rectangle Area: {area}")

# Child Class 3
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        area = 0.5 * self.base * self.height
        print(f"🔺 Triangle Area: {area}")

# Testing Hierarchical Inheritance
print("\n--- Hierarchical Inheritance Example ---")
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 10, 6)
triangle = Triangle("Green", 8, 4)

shapes = [circle, rectangle, triangle]
for shape in shapes:
    shape.display_color()  # Inherited from Shape
    shape.area()          # Own method
    print("-" * 20)

print("\n" + "="*60)
print("5. PRACTICAL REAL-WORLD EXAMPLE")
print("="*60)
print("Employee Management System using Inheritance")
print("-"*40)

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def get_details(self):
        return f"Employee: {self.name} (ID: {self.emp_id})"
    
    def calculate_pay(self):
        return self.salary

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language
    
    def code(self):
        print(f"💻 {self.name} is coding in {self.programming_language}")
    
    def calculate_pay(self):  # Method overriding with bonus
        return self.salary + 5000  # Developer bonus

class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size
    
    def conduct_meeting(self):
        print(f"📊 {self.name} is conducting a meeting with {self.team_size} team members")
    
    def calculate_pay(self):  # Method overriding with bonus
        return self.salary + (self.team_size * 1000)  # Manager bonus based on team size

# Testing the Employee System
print("\n--- Employee Management System ---")
dev = Developer("Alice", "DEV001", 80000, "Python")
manager = Manager("Bob", "MGR001", 90000, 10)

print(dev.get_details())
print(f"💰 Developer Pay: ${dev.calculate_pay()}")
dev.code()

print(f"\n{manager.get_details()}")
print(f"💰 Manager Pay: ${manager.calculate_pay()}")
manager.conduct_meeting()

print("\n" + "="*60)
print("KEY CONCEPTS SUMMARY")
print("="*60)
print("""
🔹 super() function: Calls parent class methods
🔹 Method Overriding: Child class redefines parent method
🔹 isinstance(): Check if object is instance of class
🔹 issubclass(): Check if class is subclass of another
🔹 MRO (Method Resolution Order): Order of method lookup
""")

# Demonstrating isinstance and issubclass
print("\n--- Type Checking Examples ---")
print(f"isinstance(my_car, Car): {isinstance(my_car, Car)}")
print(f"isinstance(my_car, Vehicle): {isinstance(my_car, Vehicle)}")
print(f"issubclass(Car, Vehicle): {issubclass(Car, Vehicle)}")
print(f"issubclass(Vehicle, Car): {issubclass(Vehicle, Car)}")

print(f"\n🎉 Inheritance examples completed successfully!")
print("="*60)


