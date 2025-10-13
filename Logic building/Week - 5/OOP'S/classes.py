"""
🐍 Complete OOP Fundamentals Guide
Classes, Objects, Abstraction, Encapsulation + Inheritance Basics

🎯 Goal: Master first 2 pillars of OOP in simple examples
⏰ Time: 45 minutes | 🎨 Focus: Core concepts only
"""

print("="*60)
print("🐍 COMPLETE OOP FUNDAMENTALS - SIMPLE & EASY")
print("="*60)

# =============================================================================
# PART 1: CLASSES & OBJECTS (THE FOUNDATION)
# =============================================================================

print("\n🏗️ PART 1: CLASSES & OBJECTS - THE FOUNDATION")
print("-" * 50)

# 🎯 SIMPLE CONCEPT: Class = Recipe, Object = Actual Cake

class Car:
    """🚗 Simple Car class to understand basics"""
    
    # Class variable (shared by all cars)
    brand = "Toyota"
    
    def __init__(self, model, year):
        """🔧 Constructor - runs when creating new car"""
        print(f"🚗 Creating {model} car...")
        self.model = model      # Instance variable (unique to each car)
        self.year = year        # Instance variable
        self.is_running = False # Instance variable
    
    def start_engine(self):
        """🔥 Start the car"""
        self.is_running = True
        print(f"🔥 {self.model} engine started!")
    
    def stop_engine(self):
        """🛑 Stop the car"""
        self.is_running = False
        print(f"🛑 {self.model} engine stopped!")

# Creating objects (actual cars from the Car class)
print("\n🏭 Creating Cars:")
car1 = Car("Camry", 2020)
car2 = Car("Corolla", 2022)

print("\n🚗 Using Cars:")
car1.start_engine()
car2.start_engine()
print(f"Car1 running: {car1.is_running}")
print(f"Car2 running: {car2.is_running}")

car1.stop_engine()
print(f"Car1 running: {car1.is_running}")
print(f"Car2 running: {car2.is_running}")

print("\n🔍 Key Points:")
print("✅ Class = Blueprint/Recipe")
print("✅ Object = Real thing made from blueprint")
print("✅ Each object has its own data (instance variables)")
print("✅ Methods define what objects can do")

# =============================================================================
# PART 2: ENCAPSULATION (PILLAR 1) - HIDING & PROTECTING DATA
# =============================================================================

print("\n\n🔒 PART 2: ENCAPSULATION - HIDING & PROTECTING DATA")
print("-" * 50)

class BankAccount:
    """🏦 Bank Account showing Encapsulation"""
    
    def __init__(self, owner, balance):
        """🏦 Create bank account"""
        self.owner = owner              # 🔓 PUBLIC - anyone can access
        self.__balance = balance        # 🔒 PRIVATE - hidden from outside
        self.__pin = "1234"            # 🔒 PRIVATE - secret PIN
        print(f"🏦 Account created for {owner}")
    
    def __check_pin(self, pin):
        """🔒 PRIVATE method - only used inside class"""
        return pin == self.__pin
    
    def deposit(self, amount, pin):
        """💰 PUBLIC method - deposit money"""
        if not self.__check_pin(pin):
            print("❌ Wrong PIN!")
            return False
        
        if amount > 0:
            self.__balance += amount
            print(f"💰 Deposited ${amount}. Balance: ${self.__balance}")
            return True
        else:
            print("❌ Invalid amount!")
            return False
    
    def withdraw(self, amount, pin):
        """💳 PUBLIC method - withdraw money"""
        if not self.__check_pin(pin):
            print("❌ Wrong PIN!")
            return False
        
        if amount > self.__balance:
            print("❌ Not enough money!")
            return False
        
        self.__balance -= amount
        print(f"💳 Withdrew ${amount}. Balance: ${self.__balance}")
        return True
    
    def check_balance(self, pin):
        """📊 PUBLIC method - check balance"""
        if not self.__check_pin(pin):
            print("❌ Wrong PIN!")
            return None
        
        print(f"📊 Balance: ${self.__balance}")
        return self.__balance

print("\n🏦 Encapsulation Demo:")
account = BankAccount("Alice", 1000)

print("\n✅ Correct PIN operations:")
account.deposit(200, "1234")
account.withdraw(100, "1234")
account.check_balance("1234")

print("\n❌ Wrong PIN operations:")
account.deposit(200, "0000")
account.withdraw(100, "9999")

print("\n🚫 Trying to access private data directly:")
print(f"Owner (public): {account.owner}")
try:
    print(f"Balance (private): {account.__balance}")  # This will fail
except AttributeError:
    print("❌ Cannot access private __balance!")

print("\n🎯 Encapsulation Benefits:")
print("✅ Data protection - sensitive info is hidden")
print("✅ Controlled access - only through proper methods")
print("✅ Prevents accidental changes to important data")

# =============================================================================
# PART 3: ABSTRACTION (PILLAR 2) - HIDING COMPLEXITY
# =============================================================================

print("\n\n🎭 PART 3: ABSTRACTION - HIDING COMPLEXITY")
print("-" * 50)

class CoffeeMachine:
    """☕ Coffee Machine showing Abstraction"""
    
    def __init__(self):
        """☕ Initialize coffee machine"""
        self.__water_level = 100
        self.__coffee_beans = 50
        self.__milk = 30
        print("☕ Coffee machine ready!")
    
    def __check_ingredients(self, water_needed, beans_needed, milk_needed=0):
        """🔒 PRIVATE - Complex ingredient checking (hidden from user)"""
        if self.__water_level < water_needed:
            return False, "Not enough water"
        if self.__coffee_beans < beans_needed:
            return False, "Not enough coffee beans"
        if self.__milk < milk_needed:
            return False, "Not enough milk"
        return True, "OK"
    
    def __use_ingredients(self, water, beans, milk=0):
        """🔒 PRIVATE - Complex ingredient usage (hidden from user)"""
        self.__water_level -= water
        self.__coffee_beans -= beans
        self.__milk -= milk
    
    def __brew_process(self):
        """🔒 PRIVATE - Complex brewing process (hidden from user)"""
        print("🔥 Heating water...")
        print("⚙️ Grinding beans...")
        print("💧 Brewing coffee...")
        print("✅ Coffee ready!")
    
    # 🔓 PUBLIC METHODS - Simple interface for user
    def make_espresso(self):
        """☕ SIMPLE method - user doesn't need to know complexity"""
        print("\n☕ Making Espresso...")
        
        # Complex checks hidden from user
        can_make, message = self.__check_ingredients(10, 5)
        if not can_make:
            print(f"❌ Cannot make espresso: {message}")
            return False
        
        # Complex process hidden from user
        self.__use_ingredients(10, 5)
        self.__brew_process()
        return True
    
    def make_latte(self):
        """🥛 SIMPLE method - user doesn't see complexity"""
        print("\n🥛 Making Latte...")
        
        can_make, message = self.__check_ingredients(15, 5, 10)
        if not can_make:
            print(f"❌ Cannot make latte: {message}")
            return False
        
        self.__use_ingredients(15, 5, 10)
        self.__brew_process()
        print("🥛 Adding steamed milk...")
        return True
    
    def show_status(self):
        """📊 SIMPLE method - shows current status"""
        print(f"\n📊 Machine Status:")
        print(f"   💧 Water: {self.__water_level}%")
        print(f"   ☕ Beans: {self.__coffee_beans}%")
        print(f"   🥛 Milk: {self.__milk}%")

print("\n☕ Abstraction Demo:")
machine = CoffeeMachine()

print("\n👤 User Experience (Simple Interface):")
machine.show_status()
machine.make_espresso()
machine.make_latte()
machine.make_latte()  # This should fail (not enough milk)
machine.show_status()

print("\n🎯 Abstraction Benefits:")
print("✅ Simple interface - users don't need to know complexity")
print("✅ Hidden implementation - complex logic is internal")
print("✅ Easy to use - just call simple methods")
print("✅ Maintainable - can change internal code without affecting users")

# =============================================================================
# PART 4: PUBLIC vs PRIVATE vs PROTECTED ACCESS
# =============================================================================

print("\n\n🔐 PART 4: ACCESS MODIFIERS - PUBLIC, PRIVATE, PROTECTED")
print("-" * 50)

class AccessDemo:
    """🔐 Demonstrating different access levels"""
    
    def __init__(self):
        """🔐 Initialize with different access levels"""
        self.public_var = "Everyone can see this"           # 🔓 PUBLIC
        self._protected_var = "Subclasses can see this"     # 🔒 PROTECTED
        self.__private_var = "Only this class can see this" # 🔒 PRIVATE
    
    def public_method(self):
        """🔓 PUBLIC method - anyone can call"""
        print("🔓 This is a public method")
    
    def _protected_method(self):
        """🔒 PROTECTED method - for subclasses"""
        print("🔒 This is a protected method")
    
    def __private_method(self):
        """🔒 PRIVATE method - only this class"""
        print("🔒 This is a private method")
    
    def test_access(self):
        """🧪 Test all access levels from inside class"""
        print("\n🧪 Testing access from INSIDE class:")
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")
        
        self.public_method()
        self._protected_method()
        self.__private_method()

print("\n🔐 Access Control Demo:")
demo = AccessDemo()

print("\n✅ Testing access from OUTSIDE class:")
print(f"Public variable: {demo.public_var}")               # ✅ Works
print(f"Protected variable: {demo._protected_var}")        # ⚠️ Works but shouldn't
demo.public_method()                                        # ✅ Works

try:
    print(f"Private variable: {demo.__private_var}")        # ❌ Fails
except AttributeError:
    print("❌ Cannot access private variable!")

try:
    demo.__private_method()                                 # ❌ Fails
except AttributeError:
    print("❌ Cannot access private method!")

demo.test_access()  # This works because it's called from inside the class

print("\n📋 Access Level Summary:")
print("🔓 PUBLIC (no underscore): Anyone can access")
print("🔒 PROTECTED (_underscore): Subclasses should access")
print("🔒 PRIVATE (__double_underscore): Only same class can access")

# =============================================================================
# PART 5: THE `del` KEYWORD - OBJECT DESTRUCTION
# =============================================================================

print("\n\n🗑️ PART 5: THE `del` KEYWORD - OBJECT DESTRUCTION")
print("-" * 50)

class Student:
    """👨‍🎓 Student class with lifecycle management"""
    
    total_students = 0  # Class variable to track total students
    
    def __init__(self, name):
        """👨‍🎓 Create new student"""
        self.name = name
        Student.total_students += 1
        print(f"👨‍🎓 {name} enrolled! Total students: {Student.total_students}")
    
    def __del__(self):
        """🗑️ Called when student object is deleted"""
        Student.total_students -= 1
        print(f"🗑️ {self.name} graduated! Remaining students: {Student.total_students}")
    
    def study(self):
        """📚 Student studies"""
        print(f"📚 {self.name} is studying")

print("\n👨‍🎓 Object Lifecycle Demo:")

print("\n1️⃣ Creating students:")
alice = Student("Alice")
bob = Student("Bob")
charlie = Student("Charlie")

print("\n2️⃣ Students studying:")
alice.study()
bob.study()

print("\n3️⃣ Deleting specific student:")
del alice  # Remove alice from memory

print("\n4️⃣ Trying to use deleted student:")
try:
    alice.study()  # This will fail
except NameError:
    print("❌ Alice no longer exists!")

print("\n5️⃣ Other students still exist:")
bob.study()
charlie.study()

print("\n6️⃣ Program ending (auto-cleanup):")
# When program ends, remaining objects are automatically deleted

print("\n🎯 `del` Keyword Points:")
print("✅ `del` removes object from memory")
print("✅ `__del__` method called when object is destroyed")
print("✅ Other objects remain unaffected")
print("✅ Python automatically cleans up when program ends")

# =============================================================================
# PART 6: SIMPLE INHERITANCE INTRODUCTION
# =============================================================================

print("\n\n🧬 PART 6: SIMPLE INHERITANCE INTRODUCTION")
print("-" * 50)

class Animal:
    """🐾 Base Animal class"""
    
    def __init__(self, name):
        """🐾 Create animal"""
        self.name = name
        print(f"🐾 Animal {name} created")
    
    def eat(self):
        """🍽️ All animals eat"""
        print(f"🍽️ {self.name} is eating")
    
    def sleep(self):
        """😴 All animals sleep"""
        print(f"😴 {self.name} is sleeping")

class Dog(Animal):  # Dog inherits from Animal
    """🐕 Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        """🐕 Create dog"""
        super().__init__(name)  # Call parent constructor
        self.breed = breed
        print(f"🐕 Dog breed: {breed}")
    
    def bark(self):
        """🔊 Dogs can bark (unique to dogs)"""
        print(f"🔊 {self.name} says: Woof! Woof!")
    
    def eat(self):
        """🍽️ Override parent method"""
        print(f"🐕 {self.name} is eating dog food")

class Cat(Animal):  # Cat inherits from Animal
    """🐱 Cat class inheriting from Animal"""
    
    def __init__(self, name, color):
        """🐱 Create cat"""
        super().__init__(name)
        self.color = color
        print(f"🐱 Cat color: {color}")
    
    def meow(self):
        """🔊 Cats can meow (unique to cats)"""
        print(f"🔊 {self.name} says: Meow! Meow!")

print("\n🧬 Inheritance Demo:")

print("\n🐕 Creating Dog:")
dog = Dog("Buddy", "Golden Retriever")

print("\n🐱 Creating Cat:")
cat = Cat("Whiskers", "Orange")

print("\n🎬 Animals in action:")
# Inherited methods (from Animal class)
dog.eat()    # Uses Dog's overridden version
dog.sleep()  # Uses Animal's version
cat.eat()    # Uses Animal's version
cat.sleep()  # Uses Animal's version

# Unique methods
dog.bark()   # Only dogs can bark
cat.meow()   # Only cats can meow

print("\n🎯 Inheritance Benefits:")
print("✅ Code reuse - common methods in parent class")
print("✅ Specialization - child classes add unique features")
print("✅ Override - child classes can modify parent behavior")
print("✅ Organization - logical hierarchy of classes")

# =============================================================================
# SUMMARY & MASTERY CHECKLIST
# =============================================================================

print("\n\n✅ COMPLETE OOP MASTERY CHECKLIST")
print("="*50)

concepts = [
    "🏗️ Classes & Objects: Blueprint vs Real Things",
    "🔒 Encapsulation: Hiding and protecting data with private attributes",
    "🎭 Abstraction: Hiding complexity with simple interfaces",
    "🔓 Public Access: Variables/methods anyone can use",
    "🔒 Private Access: Variables/methods only same class can use",
    "🔒 Protected Access: Variables/methods for inheritance",
    "🗑️ Object Destruction: Using `del` keyword and `__del__` method",
    "🧬 Basic Inheritance: Creating child classes from parent classes",
    "⚙️ Method Override: Child classes changing parent behavior",
    "🔄 super(): Calling parent class methods from child"
]

for i, concept in enumerate(concepts, 1):
    print(f"{i:2d}. ✅ {concept}")

print("\n🎊 CONGRATULATIONS!")
print("="*30)
print("🏆 You've mastered the fundamentals:")
print("   ✅ First 2 Pillars of OOP (Abstraction & Encapsulation)")
print("   ✅ Classes and Objects creation")
print("   ✅ Access control (Public/Private/Protected)")
print("   ✅ Object lifecycle management")
print("   ✅ Basic inheritance concepts")

print("\n🎯 Key Takeaways:")
print("   1. 🏗️ Classes = Blueprints, Objects = Real things")
print("   2. 🔒 Encapsulation = Hide and protect data")
print("   3. 🎭 Abstraction = Hide complexity, show simple interface")
print("   4. 🧬 Inheritance = Reuse code, create specialized classes")

print("\n🚀 You're ready for:")
print("   📚 Advanced inheritance concepts")
print("   🎭 Polymorphism (3rd pillar)")
print("   🏗️ Multiple inheritance")
print("   🎯 Real-world OOP projects")

print("\n🐍 OOP Fundamentals Complete!")
print("⭐ Ready for advanced topics!")
print("="*60)