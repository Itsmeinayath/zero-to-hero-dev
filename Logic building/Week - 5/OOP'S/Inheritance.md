# 🧬 Inheritance in Object-Oriented Programming (OOP)

## 📖 Table of Contents
- [What is Inheritance?](#what-is-inheritance)
- [Fundamental Concepts](#fundamental-concepts)
- [Real-World Examples](#real-world-examples)
- [Types of Inheritance](#types-of-inheritance)
- [Class Methods in Inheritance](#class-methods-in-inheritance)
- [Benefits and Drawbacks](#benefits-and-drawbacks)
- [Best Practices](#best-practices)
- [Practice Exercises](#practice-exercises)

---

## 🤔 What is Inheritance?

**Inheritance** is one of the four fundamental pillars of Object-Oriented Programming (along with Encapsulation, Abstraction, and Polymorphism). It's a mechanism that allows a new class (called **child class** or **derived class**) to inherit properties and methods from an existing class (called **parent class** or **base class**).

### 🔑 Key Terms:
- **Parent/Base/Super Class**: The class being inherited from
- **Child/Derived/Sub Class**: The class that inherits from another class
- **Method Overriding**: Redefining a parent method in the child class
- **Method Overloading**: Multiple methods with the same name but different parameters
- **super()**: Function to access parent class methods

---

## 🏗️ Fundamental Concepts

### 1. **IS-A Relationship**
Inheritance represents an "IS-A" relationship between classes.
- A `Car` **IS-A** `Vehicle`
- A `Dog` **IS-A** `Animal`
- A `Manager` **IS-A** `Employee`

### 2. **Code Reusability**
Instead of writing the same code multiple times, we can inherit common functionality.

### 3. **Extensibility**
Child classes can add new features while keeping parent functionality.

### 4. **Method Resolution Order (MRO)**
The order in which Python looks for methods in class hierarchies.

---

## 🌍 Real-World Examples

Before diving into code, let's understand inheritance through everyday examples:

### 🚗 **Vehicles Example**
```
Vehicle (Parent)
├── Car
├── Motorcycle  
├── Truck
└── Bus
```
All vehicles can start, stop, and move, but each has specific features.

### 🏢 **Company Structure**
```
Employee (Parent)
├── Developer
├── Manager
├── Designer
└── Tester
```
All employees have name, ID, salary, but different roles have different responsibilities.

### 🐾 **Animal Kingdom**
```
Animal (Parent)
├── Mammal
│   ├── Dog
│   ├── Cat
│   └── Human
└── Bird
    ├── Eagle
    └── Penguin
```

---

## 📊 Types of Inheritance

### 1. 🔗 Single Inheritance

**Definition**: One child class inherits from one parent class.

**Structure**: `Parent → Child`

#### 📝 Example: Vehicle and Car

```python
# Parent Class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} started!"
        return f"{self.brand} {self.model} is already running!"
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} stopped!"
        return f"{self.brand} {self.model} is already stopped!"
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Child Class
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, fuel_type):
        super().__init__(brand, model, year)  # Call parent constructor
        self.doors = doors
        self.fuel_type = fuel_type
    
    def honk(self):
        return f"{self.brand} {self.model} goes BEEP BEEP! 🚗"
    
    def open_trunk(self):
        return f"Trunk of {self.brand} {self.model} is now open!"
    
    # Method Overriding
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info} - {self.doors} doors, {self.fuel_type} fuel"

# Usage
my_car = Car("Toyota", "Camry", 2023, 4, "Gasoline")
print(my_car.get_info())        # Overridden method
print(my_car.start())           # Inherited method
print(my_car.honk())           # Own method
print(my_car.stop())           # Inherited method
```

**Output:**
```
2023 Toyota Camry - 4 doors, Gasoline fuel
Toyota Camry started!
Toyota Camry goes BEEP BEEP! 🚗
Toyota Camry stopped!
```

---

### 2. 🔀 Multiple Inheritance

**Definition**: One child class inherits from multiple parent classes.

**Structure**: `Parent1, Parent2 → Child`

#### 📝 Example: Smartphone (Multiple Features)

```python
# First Parent Class
class Camera:
    def __init__(self):
        self.camera_resolution = "12MP"
    
    def take_photo(self):
        return f"📸 Photo taken with {self.camera_resolution} camera"
    
    def record_video(self):
        return f"🎥 Recording video in 4K"

# Second Parent Class
class MusicPlayer:
    def __init__(self):
        self.volume = 50
        self.current_song = None
    
    def play_music(self, song):
        self.current_song = song
        return f"🎵 Playing: {song} at volume {self.volume}"
    
    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        return f"🔊 Volume set to {self.volume}"

# Third Parent Class
class GPS:
    def __init__(self):
        self.current_location = "Unknown"
    
    def get_location(self):
        return f"📍 Current location: {self.current_location}"
    
    def navigate_to(self, destination):
        return f"🗺️ Navigating to {destination}"

# Child Class inheriting from all three
class Smartphone(Camera, MusicPlayer, GPS):
    def __init__(self, brand, model):
        Camera.__init__(self)
        MusicPlayer.__init__(self)
        GPS.__init__(self)
        self.brand = brand
        self.model = model
    
    def make_call(self, number):
        return f"📞 Calling {number} from {self.brand} {self.model}"
    
    def send_text(self, number, message):
        return f"📱 Sending '{message}' to {number}"

# Usage
phone = Smartphone("Apple", "iPhone 15")
print(phone.take_photo())                    # From Camera
print(phone.play_music("Shape of You"))      # From MusicPlayer
print(phone.navigate_to("New York"))         # From GPS
print(phone.make_call("+1-555-0123"))       # Own method
```

**Output:**
```
📸 Photo taken with 12MP camera
🎵 Playing: Shape of You at volume 50
🗺️ Navigating to New York
📞 Calling +1-555-0123 from Apple iPhone 15
```

---

### 3. 🪜 Multilevel Inheritance

**Definition**: Child class inherits from a parent, which itself inherits from another parent.

**Structure**: `Grandparent → Parent → Child`

#### 📝 Example: Animal Kingdom

```python
# Grandparent Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def breathe(self):
        return f"{self.name} is breathing..."
    
    def eat(self, food):
        return f"{self.name} is eating {food}"
    
    def sleep(self):
        return f"{self.name} is sleeping... 😴"

# Parent Class (inherits from Animal)
class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
        self.body_temperature = "warm-blooded"
    
    def give_birth(self):
        return f"{self.name} is giving birth to live young"
    
    def produce_milk(self):
        return f"{self.name} is producing milk for offspring"
    
    def regulate_temperature(self):
        return f"{self.name} maintains constant body temperature"

# Child Class (inherits from Mammal)
class Dog(Mammal):
    def __init__(self, name, breed, fur_color, age):
        super().__init__(name, "Canine", fur_color)
        self.breed = breed
        self.age = age
        self.loyalty_level = "Very High"
    
    def bark(self):
        return f"{self.name} barks: WOOF WOOF! 🐕"
    
    def wag_tail(self):
        return f"{self.name} is wagging tail happily!"
    
    def fetch(self, item):
        return f"{self.name} fetched the {item} and brought it back!"
    
    def get_full_info(self):
        return (f"Dog: {self.name}, Breed: {self.breed}, "
                f"Age: {self.age}, Fur: {self.fur_color}, "
                f"Loyalty: {self.loyalty_level}")

# Usage - Accessing methods from all levels
buddy = Dog("Buddy", "Golden Retriever", "Golden", 3)

# Methods from Animal (Grandparent)
print(buddy.breathe())
print(buddy.eat("dog food"))
print(buddy.sleep())

# Methods from Mammal (Parent)
print(buddy.give_birth())
print(buddy.regulate_temperature())

# Own methods (Child)
print(buddy.bark())
print(buddy.fetch("ball"))
print(buddy.get_full_info())
```

**Output:**
```
Buddy is breathing...
Buddy is eating dog food
Buddy is sleeping... 😴
Buddy is giving birth to live young
Buddy maintains constant body temperature
Buddy barks: WOOF WOOF! 🐕
Buddy fetched the ball and brought it back!
Dog: Buddy, Breed: Golden Retriever, Age: 3, Fur: Golden, Loyalty: Very High
```

---

### 4. 🌳 Hierarchical Inheritance

**Definition**: Multiple child classes inherit from one parent class.

**Structure**: 
```
      Parent
    /   |    \
Child1 Child2 Child3
```

#### 📝 Example: Geometric Shapes

```python
import math

# Parent Class
class Shape:
    def __init__(self, color):
        self.color = color
    
    def display_color(self):
        return f"This shape is {self.color}"
    
    def area(self):
        pass  # Abstract method to be overridden
    
    def perimeter(self):
        pass  # Abstract method to be overridden

# Child Class 1
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
    
    def get_info(self):
        return f"Circle: radius={self.radius}, area={self.area()}, perimeter={self.perimeter()}"

# Child Class 2
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def get_info(self):
        return f"Rectangle: {self.length}x{self.width}, area={self.area()}, perimeter={self.perimeter()}"

# Child Class 3
class Triangle(Shape):
    def __init__(self, color, base, height, side1, side2):
        super().__init__(color)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + self.side1 + self.side2
    
    def get_info(self):
        return f"Triangle: base={self.base}, height={self.height}, area={self.area()}, perimeter={self.perimeter()}"

# Usage
shapes = [
    Circle("Red", 5),
    Rectangle("Blue", 10, 6),
    Triangle("Green", 8, 6, 7, 9)
]

print("🎨 Shape Information:")
print("=" * 50)

for shape in shapes:
    print(f"{shape.display_color()}")  # Inherited method
    print(f"{shape.get_info()}")       # Own method
    print("-" * 30)
```

**Output:**
```
🎨 Shape Information:
==================================================
This shape is Red
Circle: radius=5, area=78.54, perimeter=31.42
------------------------------
This shape is Blue
Rectangle: 10x6, area=60, perimeter=32
------------------------------
This shape is Green
Triangle: base=8, height=6, area=24.0, perimeter=24
------------------------------
```

---

### 5. 💎 Hybrid Inheritance

**Definition**: Combination of multiple inheritance types in a single program.

#### 📝 Example: University Management System

```python
# Base Class
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number
    
    def get_basic_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}"

# Multiple Inheritance - Academic and Administrative
class Academic:
    def __init__(self):
        self.research_papers = []
    
    def publish_paper(self, title):
        self.research_papers.append(title)
        return f"Published paper: {title}"

class Administrative:
    def __init__(self):
        self.meetings_scheduled = 0
    
    def schedule_meeting(self, topic):
        self.meetings_scheduled += 1
        return f"Meeting scheduled for: {topic}"

# Hierarchical Inheritance from Person
class Student(Person):
    def __init__(self, name, age, id_number, major):
        super().__init__(name, age, id_number)
        self.major = major
        self.gpa = 0.0
    
    def study(self, subject):
        return f"{self.name} is studying {subject}"

class Faculty(Person):
    def __init__(self, name, age, id_number, department):
        super().__init__(name, age, id_number)
        self.department = department
    
    def teach(self, course):
        return f"Prof. {self.name} is teaching {course}"

# Multilevel + Multiple Inheritance
class Professor(Faculty, Academic, Administrative):
    def __init__(self, name, age, id_number, department, specialization):
        Faculty.__init__(self, name, age, id_number, department)
        Academic.__init__(self)
        Administrative.__init__(self)
        self.specialization = specialization
    
    def conduct_research(self, topic):
        return f"Prof. {self.name} is researching {topic} in {self.specialization}"

# Usage
student = Student("Alice Johnson", 20, "S12345", "Computer Science")
professor = Professor("Dr. Smith", 45, "F67890", "Computer Science", "AI/ML")

print("👩‍🎓 Student Activities:")
print(student.get_basic_info())  # From Person
print(student.study("Data Structures"))  # Own method

print("\n👨‍🏫 Professor Activities:")
print(professor.get_basic_info())  # From Person (via Faculty)
print(professor.teach("Machine Learning"))  # From Faculty
print(professor.publish_paper("Deep Learning in Healthcare"))  # From Academic
print(professor.schedule_meeting("Department Review"))  # From Administrative
print(professor.conduct_research("Neural Networks"))  # Own method
```

---

## 🏭 Class Methods in Inheritance

Class methods are methods that belong to the class rather than to any specific instance. They're decorated with `@classmethod` and take `cls` as the first parameter (representing the class). In inheritance, class methods provide powerful patterns for object creation and class-level operations.

### 🔑 Key Concepts:

- **`@classmethod`**: Decorator that makes a method belong to the class
- **`cls` parameter**: Refers to the class (not instance)
- **Alternative Constructors**: Create objects in different ways
- **Factory Methods**: Create specialized instances
- **Inheritance-aware**: `cls` refers to the actual class being called

### 📝 Example 1: Alternative Constructors

```python
import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor: create Person from birth year"""
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age)  # cls refers to the actual class
    
    @classmethod
    def create_baby(cls, name):
        """Factory method: create a baby (age 0)"""
        return cls(name, 0)
    
    @classmethod
    def create_adult(cls, name):
        """Factory method: create an adult (age 18+)"""
        return cls(name, 18)

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
    
    def __str__(self):
        return f"{self.name} ({self.age} years old) - Student ID: {self.student_id}, Major: {self.major}"
    
    @classmethod
    def from_birth_year(cls, name, birth_year, student_id, major):
        """Override parent class method with additional parameters"""
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age, student_id, major)
    
    @classmethod
    def create_freshman(cls, name, student_id, major):
        """Factory method: create a typical freshman (age 18)"""
        return cls(name, 18, student_id, major)

# Usage Examples
print("👤 Person Examples:")
person1 = Person("John", 25)                          # Regular constructor
person2 = Person.from_birth_year("Alice", 1995)       # From birth year
person3 = Person.create_adult("Bob")                  # Factory method

print(f"Regular: {person1}")
print(f"From birth year: {person2}")
print(f"Factory method: {person3}")

print("\n🎓 Student Examples:")
student1 = Student("Emma", 20, "S12345", "Computer Science")
student2 = Student.from_birth_year("Mike", 2003, "S67890", "Physics")
student3 = Student.create_freshman("Sarah", "S11111", "Biology")

print(f"Regular: {student1}")
print(f"From birth year: {student2}")
print(f"Freshman: {student3}")
```

**Output:**
```
👤 Person Examples:
Regular: John (25 years old)
From birth year: Alice (29 years old)
Factory method: Bob (18 years old)

🎓 Student Examples:
Regular: Emma (20 years old) - Student ID: S12345, Major: Computer Science
From birth year: Mike (21 years old) - Student ID: S67890, Major: Physics
Freshman: Sarah (18 years old) - Student ID: S11111, Major: Biology
```

### 📝 Example 2: Database-like Operations

```python
class Vehicle:
    # Class variable to keep track of all vehicles
    all_vehicles = []
    vehicle_count = 0
    
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.vehicle_id = Vehicle.vehicle_count + 1
        
        # Add to class registry
        Vehicle.all_vehicles.append(self)
        Vehicle.vehicle_count += 1
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} (${self.price:,})"
    
    @classmethod
    def get_total_count(cls):
        """Get total number of vehicles created"""
        return cls.vehicle_count
    
    @classmethod
    def get_all_vehicles(cls):
        """Get all vehicles of this class and its subclasses"""
        return [v for v in cls.all_vehicles if isinstance(v, cls)]
    
    @classmethod
    def find_by_make(cls, make):
        """Find all vehicles by make"""
        return [v for v in cls.get_all_vehicles() if v.make.lower() == make.lower()]
    
    @classmethod
    def get_average_price(cls):
        """Calculate average price of all vehicles"""
        vehicles = cls.get_all_vehicles()
        if not vehicles:
            return 0
        return sum(v.price for v in vehicles) / len(vehicles)
    
    @classmethod
    def create_from_string(cls, vehicle_string):
        """Factory method: create vehicle from string format 'Make Model Year Price'"""
        parts = vehicle_string.split()
        if len(parts) >= 4:
            make, model, year, price = parts[0], parts[1], int(parts[2]), int(parts[3])
            return cls(make, model, year, price)
        raise ValueError("Invalid format. Expected: 'Make Model Year Price'")

class Car(Vehicle):
    def __init__(self, make, model, year, price, doors=4):
        super().__init__(make, model, year, price)
        self.doors = doors
    
    def __str__(self):
        return f"{super().__str__()} - {self.doors} doors"
    
    @classmethod
    def create_sedan(cls, make, model, year, price):
        """Factory method: create a sedan (4 doors)"""
        return cls(make, model, year, price, doors=4)
    
    @classmethod
    def create_coupe(cls, make, model, year, price):
        """Factory method: create a coupe (2 doors)"""
        return cls(make, model, year, price, doors=2)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, price, engine_cc):
        super().__init__(make, model, year, price)
        self.engine_cc = engine_cc
    
    def __str__(self):
        return f"{super().__str__()} - {self.engine_cc}cc"
    
    @classmethod
    def create_sport_bike(cls, make, model, year, price):
        """Factory method: create a sport bike (600cc+)"""
        return cls(make, model, year, price, engine_cc=600)

# Usage Examples
print("🚗 Vehicle Management System")
print("=" * 50)

# Create vehicles using different methods
car1 = Car.create_sedan("Toyota", "Camry", 2023, 28000)
car2 = Car.create_coupe("Ford", "Mustang", 2023, 35000)
car3 = Car.create_from_string("Honda Civic 2022 25000")
bike1 = Motorcycle.create_sport_bike("Yamaha", "R6", 2023, 12000)
bike2 = Motorcycle("Harley", "Sportster", 2022, 15000, 883)

print(f"Total vehicles created: {Vehicle.get_total_count()}")
print(f"\nAll vehicles:")
for vehicle in Vehicle.get_all_vehicles():
    print(f"  {vehicle}")

print(f"\nCars only:")
for car in Car.get_all_vehicles():
    print(f"  {car}")

print(f"\nMotorcycles only:")
for bike in Motorcycle.get_all_vehicles():
    print(f"  {bike}")

print(f"\nToyota vehicles:")
toyota_vehicles = Vehicle.find_by_make("Toyota")
for vehicle in toyota_vehicles:
    print(f"  {vehicle}")

print(f"\nAverage vehicle price: ${Vehicle.get_average_price():,.2f}")
print(f"Average car price: ${Car.get_average_price():,.2f}")
print(f"Average motorcycle price: ${Motorcycle.get_average_price():,.2f}")
```

**Output:**
```
🚗 Vehicle Management System
==================================================
Total vehicles created: 5

All vehicles:
  2023 Toyota Camry ($28,000) - 4 doors
  2023 Ford Mustang ($35,000) - 2 doors
  2022 Honda Civic ($25,000) - 4 doors
  2023 Yamaha R6 ($12,000) - 600cc
  2022 Harley Sportster ($15,000) - 883cc

Cars only:
  2023 Toyota Camry ($28,000) - 4 doors
  2023 Ford Mustang ($35,000) - 2 doors
  2022 Honda Civic ($25,000) - 4 doors

Motorcycles only:
  2023 Yamaha R6 ($12,000) - 600cc
  2022 Harley Sportster ($15,000) - 883cc

Toyota vehicles:
  2023 Toyota Camry ($28,000) - 4 doors

Average vehicle price: $23,000.00
Average car price: $29,333.33
Average motorcycle price: $13,500.00
```

### 📝 Example 3: Configuration and Validation

```python
class DatabaseConnection:
    # Class variables for configuration
    default_host = "localhost"
    default_port = 5432
    connection_count = 0
    active_connections = []
    
    def __init__(self, host, port, database, username):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.connection_id = DatabaseConnection.connection_count + 1
        self.is_connected = False
        
        DatabaseConnection.connection_count += 1
        DatabaseConnection.active_connections.append(self)
    
    def connect(self):
        self.is_connected = True
        return f"Connected to {self.database} at {self.host}:{self.port}"
    
    def disconnect(self):
        self.is_connected = False
        return f"Disconnected from {self.database}"
    
    @classmethod
    def create_default_connection(cls, database, username):
        """Factory method: create connection with default host/port"""
        return cls(cls.default_host, cls.default_port, database, username)
    
    @classmethod
    def create_from_url(cls, connection_url, username):
        """Factory method: create from URL format 'host:port/database'"""
        try:
            host_port, database = connection_url.split('/')
            host, port = host_port.split(':')
            return cls(host, int(port), database, username)
        except ValueError:
            raise ValueError("Invalid URL format. Expected: 'host:port/database'")
    
    @classmethod
    def set_default_config(cls, host, port):
        """Class method: update default configuration"""
        cls.default_host = host
        cls.default_port = port
        return f"Default config updated: {host}:{port}"
    
    @classmethod
    def get_connection_stats(cls):
        """Class method: get connection statistics"""
        connected = sum(1 for conn in cls.active_connections if conn.is_connected)
        total = len(cls.active_connections)
        return {
            'total_created': cls.connection_count,
            'active_connections': total,
            'connected': connected,
            'disconnected': total - connected
        }
    
    @classmethod
    def cleanup_disconnected(cls):
        """Class method: remove disconnected connections from active list"""
        initial_count = len(cls.active_connections)
        cls.active_connections = [conn for conn in cls.active_connections if conn.is_connected]
        cleaned = initial_count - len(cls.active_connections)
        return f"Cleaned up {cleaned} disconnected connections"

class PostgreSQLConnection(DatabaseConnection):
    default_port = 5432
    
    @classmethod
    def create_local_dev(cls, database, username):
        """Factory method: create local development connection"""
        return cls("localhost", 5432, database, username)
    
    @classmethod
    def create_production(cls, database, username):
        """Factory method: create production connection"""
        return cls("prod-server.company.com", 5432, database, username)

class MySQLConnection(DatabaseConnection):
    default_port = 3306
    
    @classmethod
    def create_local_dev(cls, database, username):
        """Factory method: create local development connection"""
        return cls("localhost", 3306, database, username)

# Usage Examples
print("🗄️ Database Connection Management")
print("=" * 50)

# Update default configuration
print(DatabaseConnection.set_default_config("new-host", 8080))

# Create connections using different methods
pg_conn1 = PostgreSQLConnection.create_local_dev("myapp_dev", "developer")
pg_conn2 = PostgreSQLConnection.create_production("myapp_prod", "app_user")
pg_conn3 = PostgreSQLConnection.create_from_url("backup-server:5433/myapp_backup", "backup_user")

mysql_conn1 = MySQLConnection.create_local_dev("test_db", "root")
mysql_conn2 = MySQLConnection.create_default_connection("analytics", "analyst")

# Connect some of them
print(pg_conn1.connect())
print(pg_conn2.connect())
print(mysql_conn1.connect())

# Check statistics
stats = DatabaseConnection.get_connection_stats()
print(f"\n📊 Connection Statistics:")
for key, value in stats.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")

# Disconnect and cleanup
print(f"\n{pg_conn1.disconnect()}")
print(f"{mysql_conn1.disconnect()}")
print(DatabaseConnection.cleanup_disconnected())

# Final statistics
final_stats = DatabaseConnection.get_connection_stats()
print(f"\n📊 Final Statistics:")
for key, value in final_stats.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")
```

### 🔄 Class Methods vs Instance Methods vs Static Methods

```python
class MathOperations:
    pi = 3.14159
    calculations_performed = 0
    
    def __init__(self, name):
        self.name = name
        self.personal_calculations = 0
    
    # Instance method - operates on instance data
    def calculate_circle_area(self, radius):
        """Instance method: uses instance and class data"""
        self.personal_calculations += 1
        MathOperations.calculations_performed += 1
        area = self.pi * radius ** 2
        return f"{self.name} calculated circle area: {area}"
    
    # Class method - operates on class data, can create instances
    @classmethod
    def get_total_calculations(cls):
        """Class method: accesses class variables"""
        return f"Total calculations performed: {cls.calculations_performed}"
    
    @classmethod
    def create_calculator(cls, name):
        """Class method: alternative constructor"""
        return cls(name)
    
    @classmethod
    def reset_counter(cls):
        """Class method: modifies class state"""
        cls.calculations_performed = 0
        return "Calculation counter reset"
    
    # Static method - independent utility function
    @staticmethod
    def add_numbers(a, b):
        """Static method: pure utility function, no class/instance access"""
        return a + b
    
    @staticmethod
    def is_prime(number):
        """Static method: utility function for prime checking"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

# Demonstration
calc1 = MathOperations("Alice")
calc2 = MathOperations.create_calculator("Bob")  # Using class method

print(calc1.calculate_circle_area(5))  # Instance method
print(calc2.calculate_circle_area(3))  # Instance method

print(MathOperations.get_total_calculations())  # Class method

print(f"Static method - Add: {MathOperations.add_numbers(10, 20)}")  # Static method
print(f"Static method - Is 17 prime? {MathOperations.is_prime(17)}")  # Static method

print(MathOperations.reset_counter())  # Class method
print(MathOperations.get_total_calculations())  # Class method
```

### 🎯 Key Points About Class Methods in Inheritance:

1. **Inheritance-Aware**: `cls` refers to the actual class being called (not the parent)
2. **Factory Pattern**: Perfect for creating specialized instances
3. **Alternative Constructors**: Provide different ways to create objects
4. **Class-Level Operations**: Manage class-wide state and configuration
5. **Polymorphic**: Inherited and can be overridden in child classes

---

## ✅ Benefits and Drawbacks

### 🎯 Benefits:

1. **Code Reusability**: Write once, use multiple times
2. **Maintainability**: Changes in parent reflect in all children
3. **Extensibility**: Easy to add new features
4. **Polymorphism**: Same interface, different implementations
5. **Real-world Modeling**: Represents natural relationships

### ⚠️ Drawbacks:

1. **Tight Coupling**: Changes in parent can break children
2. **Complexity**: Deep hierarchies can be hard to understand
3. **Diamond Problem**: In multiple inheritance (resolved by MRO in Python)
4. **Performance**: Method lookup can be slower in deep hierarchies

---

## 🛠️ Best Practices

### 1. **Use `super()` Properly**
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # ✅ Good
        # Parent.__init__(self, name)  # ❌ Avoid this
        self.age = age
```

### 2. **Favor Composition Over Inheritance**
```python
# ❌ Inheritance might not be the best choice
class Bird:
    def fly(self): pass

class Penguin(Bird):  # Penguins can't fly!
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

# ✅ Better approach with composition
class Bird:
    def __init__(self, flight_behavior=None):
        self.flight_behavior = flight_behavior
    
    def fly(self):
        if self.flight_behavior:
            return self.flight_behavior.fly()
        return "This bird cannot fly"

class CanFly:
    def fly(self):
        return "Flying high in the sky!"

eagle = Bird(CanFly())
penguin = Bird()  # No flight behavior
```

### 3. **Keep Hierarchies Shallow**
```python
# ❌ Too deep
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass
class E(D): pass  # Too many levels

# ✅ Better
class Animal: pass
class Mammal(Animal): pass
class Dog(Mammal): pass  # Just right
```

### 4. **Use Abstract Base Classes**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

---

## 🏋️ Practice Exercises

### Exercise 1: Banking System
Create a banking system with:
- `Account` (base class)
- `SavingsAccount` (inherits from Account)
- `CheckingAccount` (inherits from Account)
- `PremiumAccount` (inherits from both SavingsAccount and CheckingAccount)

### Exercise 2: Game Characters
Design a game character system:
- `Character` (base class with health, attack)
- `Warrior` (high attack, low magic)
- `Mage` (high magic, low attack)
- `Paladin` (balanced warrior with healing magic)

### Exercise 3: Media Library
Build a media library:
- `Media` (base class)
- `Book`, `Movie`, `Music` (different media types)
- `DigitalMedia` (mixin for digital properties)
- `DigitalBook`, `StreamingMovie` (combining physical and digital)

---

## 🎯 Key Takeaways

1. **Inheritance models "IS-A" relationships** - use it when there's a clear hierarchical relationship
2. **Single inheritance is often sufficient** - multiple inheritance should be used carefully
3. **Always use `super()`** for calling parent methods
4. **Method Resolution Order (MRO)** determines method lookup in complex hierarchies
5. **Composition can be better than inheritance** in many scenarios
6. **Keep hierarchies shallow and focused** for maintainability

---

## 📚 Additional Resources

- **Python Official Documentation**: [Classes and Inheritance](https://docs.python.org/3/tutorial/classes.html)
- **Design Patterns**: Study patterns like Strategy, Template Method, and Factory
- **SOLID Principles**: Especially Liskov Substitution Principle (LSP)

---

*📝 This comprehensive guide covers all aspects of inheritance in OOP. Practice with the examples and exercises to master this fundamental concept!* 