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
## Day 2 — Loops (Python)

Master for/while loops, iteration patterns, and off‑by‑one pitfalls. Timebox: 1 hour theory + 2 hours practice.

### Learning outcomes
- Trace loop execution (init → condition → body → update)
- Use for i in range(n), nested loops, and while loops
- Generate sequences, compute aggregates, and format output

 ### Theory (60 min)
- Video (15 min): Abdul Bari — “Loops in Programming”
https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
- Article (20 min): GeeksforGeeks — “Python Loops”
https://www.geeksforgeeks.org/loops-in-python/
- Notes to capture:
- for i in range(n), for x in iterable; while condition
- Break vs continue; enumerate() for index+value
- Common mistakes: wrong range end, not updating loop variable in while

### Practice (120 min)

1) Problem: HackerRank — Python Loops
Link: https://www.hackerrank.com/challenges/python-loops
- Approach: use for i in range(n) to generate squares
- Pseudocode:
  ```
  input n
  for i from 0 to n-1:
          print(i*i)
  ```
- Do this: write tests with small n (0, 1, 2, 5) and verify output lines

 2) Problem: LeetCode — Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz/
- Approach: loop 1..n with modulo checks
- Pseudocode:
                         ```
input n
for i from 1 to n:
if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
elif i % 3 == 0: print("Fizz")
elif i % 5 == 0: print("Buzz")
else: print(i)
```
- Do this: list conditions in plain English; ensure order prevents double-print

### Mini-exercises (optional, 15–20 min)
- Sum numbers 1..n with a loop, then compare with sum(range(...))
- Print a right triangle of stars with nested loops
- Iterate a list with enumerate() and print index:value
- While loop: keep reading input until user types "quit"

### Tips
- Prefer for loops over while unless you need manual control
- Keep loop bodies small; extract logic into helper functions
- Validate boundaries: test n in {0, 1, typical, large}