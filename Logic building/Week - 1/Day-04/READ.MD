## Day 4 - Functions (Python)

Timebox: ~3 hours
Objective: Master defining, calling, and using functions to structure solutions for DSA problems.

### Learning outcomes
- Explain what functions are and why they improve readability and reuse
- Define functions with parameters and return values; call them with arguments
- Choose appropriate function shapes (no params, params, return vs print)
- Write small, testable functions and reason about time/space complexity

---

## 1) Theory - Understanding Functions (~1 hour)

### What are functions?
Reusable blocks of code for a specific task. They help break problems into smaller parts, reduce repetition, and make programs easier to test and maintain.

### Components
- Definition: `def name(params):` followed by an indented block
- Parameters: inputs (e.g., `def add(a, b):`)
- Return: outputs using `return` (e.g., `return a + b`)
- Call: `add(3, 4)` executes the function with arguments

### Common shapes
- No parameters, no return (side effects like printing)
- With parameters (perform work on inputs)
- With return (produce a value for composition and testing)

### Best practices
- Clear names: `calculate_sum`, not `x`
- One job per function; keep them short
- Prefer returning values over printing inside logic
- Test with varied inputs, including edge cases

### Examples
```python
def greet(name: str) -> str:
	return f"Hello, {name}!"

print(greet("Mohammed"))  # Hello, Mohammed!
```

```python
def square(number: int) -> int:
	return number * number

print(square(5))  # 25
```

### How to think
Ask: Can I reuse this logic elsewhere? If yes, wrap it in a function. Define inputs and outputs first, outline steps as pseudocode, then implement.

### Resources
- Video (20 min): Corey Schafer — Python Functions
  https://www.youtube.com/watch?v=9Os0o3wzS_I
- Article (40 min): Real Python — Defining Your Own Python Function
  https://realpython.com/defining-your-own-python-function/

Log key takeaways in your tracker: definitions, params vs args, return vs print, examples.

---

## 2) Practice - Solve with Functions (~2 hours)
For each problem: Understand → Pseudocode → Code → Test edge cases → Complexity.

### Problem 1: Simple Array Sum (HackerRank)
- Link: https://www.hackerrank.com/challenges/simple-array-sum
- Description: Given an array of integers, return the sum using a function.
- Input: integer `n` (length), array `ar` (1 ≤ n ≤ 1000, 0 ≤ ar[i] ≤ 1000)
- Output: integer sum

Pseudocode
```
Function sum_array(arr):
	total = 0
	for each number in arr:
		total = total + number
	return total
```

Python
```python
def simpleArraySum(ar: list[int]) -> int:
	total = 0
	for num in ar:
		total += num
	return total

if __name__ == "__main__":
	n = int(input().strip())
	ar = list(map(int, input().strip().split()))
	result = simpleArraySum(ar)
	print(result)
```

Tests (try mentally or via stdin)
- n=3, ar=[1,2,3] → 6
- n=1, ar=[0] → 0
- n=5, ar=[1,2,3,4,5] → 15

Complexity
- Time: O(n) — single pass over array
- Space: O(1) — constant extra space (accumulator)

Notes
- Order doesn’t matter for sum, but input parsing must match the platform format.

---

### Problem 2: Add Two Integers (LeetCode)
- Link: https://leetcode.com/problems/add-two-integers/
- Description: Given two integers, return their sum using a function.
- Input: integers `num1`, `num2` (−100 ≤ values ≤ 100)
- Output: integer sum

Pseudocode
```
Function add_numbers(num1, num2):
	sum = num1 + num2
	return sum
```

Python
```python
def add_numbers(num1: int, num2: int) -> int:
	return num1 + num2

if __name__ == "__main__":
	print(add_numbers(2, 3))  # 5
	print(add_numbers(-1, 1)) # 0
	print(add_numbers(0, 0))  # 0
```

Complexity
- Time: O(1)
- Space: O(1)

---

## Logging and wrap‑up
- Tracker: capture theory notes, pseudocode, code, edge cases, and complexity
- Reflection: What was tricky? Any off‑by‑one or input parsing issues?
- GitHub: commit under `Logic building` with message: `Day 4: Functions`

## Tips & pitfalls
- Prefer returning values to printing inside helpers
- Keep I/O (input/print) at the top level; keep functions pure when possible
- Test boundaries: empty lists, zeros, negatives
- Name functions and variables descriptively; avoid single letters outside indexes
