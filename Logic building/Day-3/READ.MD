- **Day 3 : Conditionals**
    - **Theory (1 hr)**:
        - Learn if-else, nested conditionals, logical operators (and, or, not).
        - **Video**: NeetCode’s “Python Conditionals” (15 min) ([YouTube](https://www.youtube.com/watch?v=kqtD5dpn9C8&t=300s)).
        - **Article**: GFG’s “Python If-Else” (20 min) ([Link](https://www.geeksforgeeks.org/python-if-else/)).
        - Note: if condition, elif, else syntax.
    - **Practice (2 hr)**:
        - **Problem 1**: HackerRank: If-Else ([Link](https://www.hackerrank.com/challenges/py-if-else)).
            - **Brute Force**: Multiple nested ifs (O(1)).
            - **Better**: Single if-elif chain (O(1)).
            - **Optimal**: Same, with clear logic (O(1)).
            - **Pseudocode**:
                
                ```
                Input: number n
                If n odd: Print "Weird"
                Else if n even and 2<=n<=5: Print "Not Weird"
                Else if n even and 6<=n<=20: Print "Weird"
                Else: Print "Not Weird"
                ```
                
            - **Logic Exercise**: Write all conditions in plain English.
        - **Problem 2**: LeetCode: Sign of the Product of an Array ([Link](https://leetcode.com/problems/sign-of-the-product-of-an-array/)).
            - **Brute Force**: Multiply all numbers (O(n)).
            - **Better**: Count negatives (O(n)).
            - **Optimal**: Same, with early exit on zero (O(n)).
            - **Pseudocode**:
                
                ```
                Input: array of numbers
                Initialize sign = 1
                For each number:
                    If number = 0: Return 0
                    If number < 0: Flip sign
                Return sign
                ```
                
            - **Logic Exercise**: Draw decision tree for conditions.
    - **Support**: Share code; I’ll check conditional logic errors.



Conditional Statements and logical operators

Explanation:

What are Conditionals?: Conditionals let you execute code based on whether a condition is true or false (e.g., “if it’s raining, take an umbrella”). They’re the decision-making backbone of programming.
Types:

if condition: – Runs if true (e.g., if x > 0:).
elif condition: – Else if, checks next condition if previous is false (e.g., elif x == 0:).
else: – Runs if all above are false (e.g., else:).


Logical Operators:

and: True if both conditions are true (e.g., x > 0 and x < 10).
or: True if at least one condition is true (e.g., x > 0 or x < -5).
not: Negates a condition (e.g., not x == 0).


Comparison Operators:

== (equal), != (not equal), < (less than), > (greater than), <=, >=.


Nesting: if inside if (e.g., if x > 0: if x < 5:).
Best Practices:

Avoid complex nesting—use elif to flatten.
Test edge cases (e.g., 0, negative numbers).
Use comments to explain logic.