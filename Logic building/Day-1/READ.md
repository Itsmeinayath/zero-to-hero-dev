- **Day 1 : Variables & Input/Output**
    - **Theory (1 hr)**:
        - **Video**: NeetCode’s “Python for Beginners” (20 min) ([YouTube](https://www.youtube.com/watch?v=kqtD5dpn9C8)).
        - **Article**: GFG’s “Python Variables” (20 min) ([Link](https://www.geeksforgeeks.org/python-variables/)).
        - Note basics: variable assignment (x = 5), input (input()), output (print()).
    - Learn variables (int, float, string), data types, input/output in Python.
    - **Practice (2 hr)**:
        - **Problem 1**: HackerRank: Simple Array Sum ([Link](https://www.hackerrank.com/challenges/simple-array-sum)).
            - **Brute Force**: Loop, add each element (O(n)).
            - **Better**: Single variable sum (O(n)).
            - **Optimal**: Built-in sum() (O(n), cleaner).
            - **Pseudocode**:
                
                ```
                Input: array of numbers
                Initialize sum = 0
                For each number in array:
                    Add number to sum
                Return sum
                ```
                
            - **Logic Exercise**: Write pseudocode, then code. Draw a flowchart showing loop iteration.
        - **Problem 2**: HackerRank: Solve Me First ([Link](https://www.hackerrank.com/challenges/solve-me-first)).
            - **Brute Force**: Add two numbers directly (O(1)).
            - **Better/Optimal**: Same, but with clear variable names (O(1)).
            - **Pseudocode**:
                
                ```
                Input: two numbers a, b
                Return a + b
                ```
                
            - **Logic Exercise**: Explain logic in plain English (e.g., “Take two numbers, add them”).