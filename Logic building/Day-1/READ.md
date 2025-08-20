## Day 1  Variables and Input/Output (Python)

Learn the basics of variables, data types, user input, and printing in Python. Timebox: 1 hour theory + 2 hours practice.

### Learning outcomes
- Understand primitive types: int, float, str, bool
- Declare/assign variables and follow naming rules
- Read input with input() and display output with print()
- Convert types (int(), float(), str()) and handle simple arithmetic

### Theory (60 min)
- Video (20 min): NeetCode — “Python for Beginners” (YouTube)
    https://www.youtube.com/watch?v=kqtD5dpn9C8
- Article (20 min): GeeksforGeeks — “Python Variables”
    https://www.geeksforgeeks.org/python-variables/
- Notes to capture:
    - Assignment: x = 5, y = "hello"; dynamic typing
    - Input/Output: name = input("Name? "); print(name)
    - Type conversion: int("42"), float("3.14"), str(123)
    - Good names and basic operators: +, -, *, /, //, %

### Practice (120 min)

1) Problem: Simple Array Sum (HackerRank)
Link: https://www.hackerrank.com/challenges/simple-array-sum
- Approaches:
- Loop and accumulate (O(n))
- Built-in sum(arr) for clarity (O(n))
- Pseudocode:
    ```
    Input: array of numbers
    total = 0
    for each number in array:
    total = total + number
    return total
    ```
- Do this: write pseudocode, then implement; sketch a flowchart of the loop.

2) Problem: Solve Me First (HackerRank)
Link: https://www.hackerrank.com/challenges/solve-me-first
- Approach: read two numbers, return a + b (O(1))
- Pseudocode:
    ```
    Input: two numbers a, b
    return a + b
    ```
- Do this: explain the logic in plain English (“Take two numbers and add them”).

### Mini-exercises (optional, 15–20 min)
- Read an integer and print its square
- Read two floats and print their sum formatted to 2 decimals
- Read a line of space-separated integers into a list and print sum(list)
- Convert a numeric string to int and handle invalid input with a friendly message

### Tips
- Prefer clear variable names (total, count, price)
- Start with the loop solution; refactor to sum() after it passes tests
- Save solutions under `Logic building/Day-1/Data_type.py` or separate files per problem