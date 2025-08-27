## Day 6 - Recap & Mixed Practice (Python / DSA)

Timebox: ~3 hours  
Objective: Reinforce Week 1 fundamentals (variables, loops, conditionals, functions, Big-O) and apply them to mixed problems.

### Learning outcomes
- Recall core syntax and patterns from Days 1–5
- Apply digit processing and conditionals in simple algorithms
- Analyze time/space complexity confidently
- Practice clean pseudocode → implementation

---
## 1. Recap (~1 hour)
Topics to skim and self‑quiz:
- Variables & I/O: assignment, input(), print()
- Loops: for range(n), while, enumerate
- Conditionals: if / elif / else, logical operators (and / or / not)
- Functions: parameters vs arguments, return values, pure vs side‑effect
- Big-O: O(1), O(n), O(log n), O(n^2) basics; digit loops = O(log n)

Quick self‑checks:
- Write a one‑line function that returns square
- Explain why a single pass max function is O(n)
- Identify complexity of nested loops vs two separate loops

Optional resources (pick 1):
- Python basics recap (video excerpt)
- GFG: Python basics summary

Log 3 takeaways (e.g., "Loops + Big-O feel clearer").

---
## 2. Practice (~2 hours)
Process: Understand → Pseudocode → Code → Tests → Complexity.

### Problem 1: Palindrome Number (LeetCode)
Link: https://leetcode.com/problems/palindrome-number/
Goal: Return True if integer reads same forward/backward.

Pseudocode
```
if x < 0: return False
orig = x
rev = 0
while x > 0:
    d = x % 10
    rev = rev * 10 + d
    x //= 10
return orig == rev
```

Python
```python
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    orig = x
    rev = 0
    while x:
        d = x % 10
        rev = rev * 10 + d
        x //= 10
    return orig == rev

assert is_palindrome(121) is True
assert is_palindrome(-121) is False
assert is_palindrome(10) is False
assert is_palindrome(0) is True
```
Complexity: Time O(log n) (digits), Space O(1).

### Problem 2: Compare the Triplets (HackerRank)
Link: https://www.hackerrank.com/challenges/compare-the-triplets
Goal: Compare elementwise scores of two length‑3 arrays; count wins.

Pseudocode
```
alice = bob = 0
for i in 0..2:
    if a[i] > b[i]: alice += 1
    elif a[i] < b[i]: bob += 1
return [alice, bob]
```

Python
```python
def compare_triplets(a: list[int], b: list[int]) -> list[int]:
    alice = bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]

assert compare_triplets([1,2,3],[3,2,1]) == [1,1]
assert compare_triplets([5,6,7],[3,6,10]) == [1,1]
assert compare_triplets([1,1,1],[1,1,1]) == [0,0]
```
Complexity: Time O(1) (fixed 3 comparisons), Space O(1).

### Optional stretch
- Rewrite palindrome check without reversing whole number (compare first/last digits) 
- Add input validation (non-integers) gracefully
- Implement second largest of a list in one pass

---
## 3. Reflection (~10–15 min)
Answer briefly:
- Strongest concept now?
- Weakest / needs more reps?
- One target for Day 7 / Week 2 (e.g., arrays & string operations)

Commit message suggestion: `Day 6: Recap & Mixed Practice`.

---
## Cheat sheet
```
Single pass over n            O(n)
Digit extraction loop         O(log n)
Three fixed comparisons       O(1)
Double nested full loops      O(n^2)
Accumulator space only        O(1) space
New list proportional to n    O(n) space
```

### Tips
- Keep functions pure; separate I/O from logic
- Test edge cases first (0, negative, single element)
- Name intermediates clearly (rev, orig)
- Stop over-commenting obvious lines; focus on intent

End of Day 6 guide.