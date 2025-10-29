# Day 36 — Stack Basics

What you'll learn
- LIFO concept and stack operations (push, pop, peek)
- Implementing a stack in Python (list-backed)
- Solving classic stack problems: Valid Parentheses
- Complexity and common pitfalls

---

Concept: What is a Stack?

A stack is a Last-In, First-Out (LIFO) data structure. Think of a pile of plates: you put new plates on top and take plates from the top.

Core operations
- push(item): add to top
- pop(): remove and return top
- peek()/top(): inspect top without removing
- is_empty(), size()

Why use a stack?
- Tracks nested state (parens, recursion simulation)
- Useful in expression evaluation, DFS, undo-redo systems

---

Python tool: list-backed stack

The simplest, idiomatic stack in Python uses a list:

push -> list.append(item)
pop  -> list.pop()
peek -> list[-1]

---

Simple Stack class (list-backed)

```python
class MyStack:
	"""Minimal list-backed stack with safety checks."""
	def __init__(self):
		self._data = []

	def push(self, item):
		self._data.append(item)

	def pop(self):
		if not self._data:
			raise IndexError("pop from empty stack")
		return self._data.pop()

	def peek(self):
		if not self._data:
			raise IndexError("peek from empty stack")
		return self._data[-1]

	def is_empty(self):
		return len(self._data) == 0

	def size(self):
		return len(self._data)
```

---

Problem: Valid Parentheses (LeetCode)

Idea
- Push opening brackets on the stack.
- On a closing bracket, pop and check if it matches the expected opener.

Clean solution

```python
def is_valid_parentheses(s: str) -> bool:
	stack = []
	matches = {')':'(', ']':'[', '}':'{'}

	for ch in s:
		if ch in matches.values():  # opener
			stack.append(ch)
		else:  # closer
			if not stack or stack.pop() != matches[ch]:
				return False
	return len(stack) == 0
```

Complexity
- Time: O(N) — single pass
- Space: O(N) — worst-case all openers

Edge cases and tips
- Always check for empty stack before pop
- Use a dictionary for matching brackets
- For short strings, the function is tiny and very fast

---

Practice problems
- GFG: Implement Stack using Array (practice OOP)
- LeetCode: Valid Parentheses

---
