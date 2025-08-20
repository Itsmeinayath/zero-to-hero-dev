# Nested Conditional statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
    if age >= 21:
        print("You are also eligible to drink alcohol")
    else:
        print("But you are not eligible to drink alcohol")
else:
    print("You are not eligible to vote")
