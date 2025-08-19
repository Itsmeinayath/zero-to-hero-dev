# while loop is a control flow statement that allows code to be executed repeatedly based on a given condition.
# The loop continues to execute as long as the condition evaluates to true.

# print number from 1 to 100

# num = 1
# while num <= 100:
#     print(num)
#     num +=1
# print("The number count ended")

#  Print number from 100 to 1

# num = 100
# while num >= 1:
#     print(num)
#     num -=1
# print("The loop ended")


# print the multiplication table of a number

# num  = int(input("Enter a number to print its multiplication table: "))
# i = 1

# while i <= 10:
#     print(num, "x",i,"=",num * i)
#     i+=1

# Print the elements of the following list suing a loop
# list = [1,4,9,16,25,36,49,64,81,100]

# list = [1,4,9,16,25,36,49,64,81,100]
# ind = 0
# while ind < len(list):
#     print(list[ind])
#     ind +=1


# Search for a number x in this tuple using loop

# my_tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# i = 0

# while i < len(my_tup):
#     if (my_tup[i] == x):
#         print("Found", x, "at index", i)
#     i += 1


# Break is key word in while loop
# what is the use of break statement in while loop
# The break statement is used to exit the loop prematurely, regardless of the loop's condition.
# When a break statement is encountered, the loop is terminated, and control is transferred to the next statement following the loop.

# example
# i = 0
# while i <= 5:
#     if (i == 3):
#         break
#     i += 1
# print(i)

# Here in the above example, the loop is terminated when i equals 3, so the final value of i printed is 3.

# Continue is keyword in while loop
# what is the use of continue statement in while loop
# The continue statement is used to skip the current iteration of the loop and proceed to the next iteration.
# When a continue statement is encountered, the remaining code inside the loop for the current iteration is skipped.

# example
i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1
# here the above code will print all numbers from 0 to 5 except 3
# The continue statement is used to skip the current iteration when i equals 3, so 3 is not printed.
