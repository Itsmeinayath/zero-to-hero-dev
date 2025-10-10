# Lets Learn and practice classes in Python

# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# An object is an instance of a class. It is created using the class blueprint and can have its own unique attributes and methods.
# Classes help to organize code, promote reusability, and implement object-oriented programming principles.
# Methods are functions defined within a class that operate on the attributes of the class and its instances.
# Abstraction: Hiding complex implementation details and showing only the essential features of the object.
# Encapsulation: Bundling data (attributes) and methods (functions) that operate on the data into a single unit (class).

# Syntax to create a class

class ClassName:
    # class attributes and methods
    pass
# Syntax to create an object
object_name = ClassName()

# Example

# class Student:
#     # class attribute (also called class variable)
#     school_name  = "International School"

#     # constructor to initialize object attributes
#     def __init__(self,name,age,grade):
#         self.name = name  # instance attribute
#         self.age = age    # instance attribute
#         self.grade = grade # instance attribute
#         self.marks = []   # instance attribute to store marks

#     # method to add marks
#     def add_marks(self,marks):
#         self.marks.append(marks)
    
#     # method to calculate average marks
#     def average_marks(self):
#         return sum(self.marks) / len(self.marks) if self.marks else 0
    
# creating objects
# student1 = Student("Alice", 14, 9)
# student2 = Student("Bob", 15, 10)
# student3 = Student("Charlie", 13, 8)
# student4 = Student("David", 16, 11)

# # adding marks
# student1.add_marks(85)
# student1.add_marks(90)
# student2.add_marks(78)
# student2.add_marks(88)
# student3.add_marks(92)
# student3.add_marks(95)
# student4.add_marks(80)
# student4.add_marks(85)

# calculating average marks
# here we are calling the method using the object . all methods are used here 
# print(f"Student 1 - Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}, School: {student1.school_name}")
# print(f"Marks: {student1.marks}")
# print(f"Average Marks: {student1.average_marks()}")
# print()

# print(f"Student 2 - Name: {student2.name}, Age: {student2.age}, Grade: {student2.grade}, School: {student2.school_name}")
# print(f"Marks: {student2.marks}")
# print(f"Average Marks: {student2.average_marks()}")
# print()

# print(f"Student 3 - Name: {student3.name}, Age: {student3.age}, Grade: {student3.grade}, School: {student3.school_name}")
# print(f"Marks: {student3.marks}")
# print(f"Average Marks: {student3.average_marks()}")
# print()

# print(f"Student 4 - Name: {student4.name}, Age: {student4.age}, Grade: {student4.grade}, School: {student4.school_name}")
# print(f"Marks: {student4.marks}")
# print(f"Average Marks: {student4.average_marks()}")

# Example for abstraction and encapsulation

# Lets practice more
# create Account class with 2 attributes account_number and balance
# Crete methods for debit, credit and check_balance

class Account:
    def __init__(self,account_number,balance =0):
        self.account_number = account_number
        self.__balance = balance  # private attribute
    
    def debit(self,amount):
        self.__balance -= amount
        print(f"Debited {amount}. New balance is {self.__balance}")
    def credit(self,amount):
        self.__balance += amount
        print(f"Credited {amount}. New balance is {self.__balance}")

    def check_balance(self):
        print(f"Account {self.account_number} has balance: {self.__balance}")

Account1 = Account("1234567890", 1000)
Account2 = Account("0987654321", 500)

Account1.check_balance()
Account1.debit(200)
Account1.credit(300)
Account1.check_balance()

Account2.check_balance()
Account2.debit(100)
Account2.credit(400)
Account2.check_balance()

# Note: Here we have made balance attribute private by adding __ before it. This is to prevent direct access from outside the class.
# We can only access it using the methods provided in the class. This is an example of
# Abstraction and Encapsulation in OOP.
# Abstraction: We are hiding the complex implementation of balance management and providing simple methods to interact with it.
# Encapsulation: We are bundling the balance attribute and the methods that operate on it into a single unit (the Account class).
# This ensures that the balance can only be modified through the debit and credit methods, maintaining data integrity.
# This is a comprehensive guide on Python classes and objects with examples.
# You can practice more by creating different classes and objects as per your requirement.

# lets foucs on inheritance in next file :
# Inheritance is a mechanism in OOP that allows a new class (derived class) to inherit attributes and methods from an existing class (base class).
# This promotes code reusability and establishes a hierarchical relationship between classes.
# Syntax for inheritance
# class BaseClass:

