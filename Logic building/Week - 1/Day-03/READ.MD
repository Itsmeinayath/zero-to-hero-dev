## Day 3 - Conditionals (Python)

Make decisions with if/elif/else, comparisons, and logical operators. Timebox: 1 hour theory + 2 hours practice.

### Learning outcomes
- Write clear if/elif/else chains and avoid deep nesting
- Combine conditions with and, or, not
- Use comparisons: ==, !=, <, >, <=, >=

### Theory (60 min)
- Video (15 min): NeetCode — Python Conditionals
  https://www.youtube.com/watch?v=kqtD5dpn9C8&t=300s
- Article (20 min): GeeksforGeeks — Python If-Else
  https://www.geeksforgeeks.org/python-if-else/
- Notes to capture:
  - Truthy/Falsey values; guard clauses; ternary: x if cond else y
  - Avoid nested ifs; prefer elif chains and early returns

### Practice (120 min)

1) Problem: HackerRank — If-Else
   Link: https://www.hackerrank.com/challenges/py-if-else
   - Pseudocode:
     ```
     input n
     if n is odd: print("Weird")
     elif n is even and 2 <= n <= 5: print("Not Weird")
     elif n is even and 6 <= n <= 20: print("Weird")
     else: print("Not Weird")
     ```
   - Do this: test with n in {1,2,4,6,20,22}

2) Problem: LeetCode — Sign of the Product of an Array
   Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/
   - Pseudocode:
     ```
     input nums
     sign = 1
     for x in nums:
         if x == 0: return 0
         if x < 0: sign = -sign
     return sign
     ```
   - Do this: add early return on zero and verify with positive/negative mixes

### Mini-exercises (optional, 15–20 min)
- Grading: read score 0–100 and print A/B/C/D/F
- Leap year check using divisible-by-4/100/400 rules
- Read two numbers and print the larger (or "equal")

### Tips
- Keep conditions mutually exclusive; order matters
- Extract condition checks into well-named helpers for readability
- Test edge cases: 0, negatives, boundaries