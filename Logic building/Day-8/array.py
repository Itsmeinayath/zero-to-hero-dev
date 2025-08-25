# What is an Array?
# An array is a data structure that stores a collection of elements, typically of the same data type.
# In Python, arrays are implemented as lists, which are dynamic and can hold elements of different types.
# Lists in Python are versatile and can be used to implement various data structures, such as stacks, queues, and more.

# What are the use of arrays?
# Arrays are used to store multiple values in a single variable, making it easier to manage and manipulate data.
# They allow for efficient indexing and iteration, making them ideal for tasks that involve collections of items.
# Common use cases include:
# - Storing and accessing lists of items (e.g., user inputs, sensor readings)
# - Implementing data structures (e.g., stacks, queues, hash tables)
# - Performing mathematical operations on large datasets (e.g., image processing, scientific computing)

# In programming the index starts from 0 (Zero-based indexing). Why?
# This convention simplifies the calculation of memory addresses and offsets, making it more efficient for the underlying hardware.

# List and Array are Mutable
# This means we can change, add, or remove elements after the array has been created.

# Example :
marks = [85, 90, 78, 92, 88]
print("Marks:", marks)
print("First mark:", marks[0])  # Accessing the first element .This called indexing . This is how we can access elements in an array.
print(type(marks))  # Output: <class 'list'> . "type" is key to understanding the what data structure we are working with.
print("Length of marks array:", len(marks))  # Output: 5 . "len" is used to find the length of the array.

# here we are storing different types of information about a student in one array
student = ["John",85,20,"Mumbai"]
print("Student Information:","Name:", student[0],"Marks:", student[1],"Age:", student[2],"City:", student[3])

# List Slicing
# Slicing allows us to create a new list from a subset of an existing list.
# Syntax: new_list = old_list[start:end] (end is exclusive)
# Example:
print("Marks (sliced):", marks[1:4])  # Output: [90, 78, 92]
