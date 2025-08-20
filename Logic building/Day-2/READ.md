- **Day 2 : Loops**
    - **Theory (1 hr)**:
        - Learn for/while loops, loop structure (start, condition, update).
        - **Video**: Abdul Bari’s “Loops in Programming” (15 min) ([YouTube](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)).
        - **Article**: GFG’s “Python Loops” (20 min) ([Link](https://www.geeksforgeeks.org/loops-in-python/)).
        - Note: for loop (for i in range(n)), while loop (while condition).
    - **Practice (2 hr)**:
        - **Problem 1**: HackerRank: Loops ([Link](https://www.hackerrank.com/challenges/python-loops)).
            - **Brute Force**: Print numbers manually (impractical).
            - **Better**: Use for loop (O(n)).
            - **Optimal**: Same, with clean output format (O(n)).
            - **Pseudocode**:
                
                ```
                Input: number n
                For i from 0 to n-1:
                    Print i
                ```
                
            - **Logic Exercise**: Draw a flowchart for the loop (e.g., “i starts at 0, check i < n, print i, i++”).
        - **Problem 2**: LeetCode: Print Numbers ([Link](https://leetcode.com/problems/fizz-buzz/)).
            - **Brute Force**: Manual if-else for each number (impractical).
            - **Better**: Loop with modulo checks (O(n)).
            - **Optimal**: Same, with concise conditions (O(n)).
            - **Pseudocode**:
                
                ```
                Input: number n
                For i from 1 to n:
                    If i divisible by 3 and 5: Print "FizzBuzz"
                    Else if divisible by 3: Print "Fizz"
                    Else if divisible by 5: Print "Buzz"
                    Else: Print i
                ```
                
            - **Logic Exercise**: List loop conditions in plain English