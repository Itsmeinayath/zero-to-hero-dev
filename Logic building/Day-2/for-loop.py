# For loops are used for iterating over a sequence (such as a list, tuple, or string) or other iterable objects.

# this example on iterating through a list
# my_list = [1, 2, 3, 4, 5]

# for item in my_list:
#     print(item)


# This is another example on iterating through a list of strings
# veg = ["carrot", "potato", "spinach"]
# for item in veg:
#     print(item)

# This is an example of iterating through a tuple
# my_tuple = (10, 20, 30, 40, 50)

# for i in my_tuple:
#     print(i)

# And in for loop we can also use "else" also , what else is doing here
# Here the else in for loop is executed when the loop is exhausted (i.e., no more items to iterate over)'

# example
# for i in range(5):
#     print(i)
# else:
#     print("Loop finished")

# example 
# str = "Hello"
# for char in str:
#     if char == "e":
#         print("Found an 'e'")
#         break
#     print(char)
# else:
#     print("Loop finished")
# The else block will not be executed because the loop was terminated by the break statement

# Example find the x in the list 
# my_list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36)
# x =36
# ind = 0
# for i in my_list:
#     if i == x:
#         print("Found", x, "at index:", ind)
#         break;
#     ind += 1

# What is range() ?
# The range() function generates a sequence of numbers. It is commonly used in for loops to specify the number of iterations.
# Range function returns a sequence of numbers ,starting from 0 by default and increment by 1(by default), and stops before a specified number.
# start from 0 step by 1 and end before 5. so it will print 0 to 4
# for i in range(5):
#     print(i)


# This will print odd numbers from 1 to 10 . how here the range function is used range(1,11,2)  first is the start, second is the stop and third is the step by means it will increment by 2
# for i in range(1,11,2):
#     print(i)


# And there is also "pass"
# The pass statement is a null operation; it is syntactically required but you do not want any command or code to execute.
for i in range(5):
    if i == 3:
        pass
    print(i)