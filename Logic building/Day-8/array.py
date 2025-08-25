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
# marks = [85, 90, 78, 92, 88]
# print("Marks:", marks)
# print("First mark:", marks[0])  # Accessing the first element .This called indexing . This is how we can access elements in an array.
# print(type(marks))  # Output: <class 'list'> . "type" is key to understanding the what data structure we are working with.
# print("Length of marks array:", len(marks))  # Output: 5 . "len" is used to find the length of the array.

# # here we are storing different types of information about a student in one array
# student = ["John",85,20,"Mumbai"]
# print("Student Information:","Name:", student[0],"Marks:", student[1],"Age:", student[2],"City:", student[3])

# List Slicing
# Slicing allows us to create a new list from a subset of an existing list.
# Syntax: new_list = old_list[start:end] (end is exclusive)
# Example:
# print("Marks (sliced):", marks[1:4])  # Output: [90, 78, 92]


# List methods:
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)
my_list.append(60)  # Adds 60 to the end of the list
print("After append:", my_list)

list2 = [90,40,30,20,1,99,89]
print("Original list2:", list2)

list2.sort() # sort() is builtin function for sorting lists
print("After sort:", list2)

list2.reverse() # reverse() is builtin function for reversing lists
print("After reverse:", list2)

print(list2.sort(reverse=True)) # sort() with reverse=True sorts the list in descending order

list2.insert(2,100) # insert() is builtin function for inserting an element at a specific index
print("After insert:", list2)

list2.remove(1) # remove() is builtin function for removing the first occurrence of a value . we have to specify the value to remove
print("After remove:", list2)

list2.pop() # pop() is builtin function for removing and returning the last item in the list . Here we are removing the last element
print("After pop:", list2)