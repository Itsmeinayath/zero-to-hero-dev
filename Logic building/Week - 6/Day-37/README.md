# Day 37 — Queue Basics

What you'll learn
- FIFO concept and queue operations (enqueue, dequeue, peek)
- Why Python lists are a poor queue implementation
- Using `collections.deque` for efficient queues
- A tiny `SimpleQueue` wrapper and a runnable demo

---

Concept: What is a Queue?

A queue is a First-In, First-Out (FIFO) data structure. Imagine a line at a ticket counter: people join at the back (enqueue) and are served at the front (dequeue).

Core operations
- enqueue(item): add to the back
- dequeue(): remove and return front
- peek()/front(): inspect front without removing
- is_empty(), size()

Why not use a plain list?

- list.append(x) is O(1) on average for adding to the back.
- But list.pop(0) removes the first element and shifts all others left — O(N). If you frequently dequeue, this is slow and memory-inefficient.

A short visual explanation

- A Python list is an array: all elements live in one continuous block of memory, side-by-side. Removing the first element requires shifting every element down to fill the gap.

	list.pop(0): [A] [B] [C] [D]

	To remove [A], the list shifts every other element left:

	[ ] [B] [C] [D]  ->  [B] [C] [D] [ ]

	This is an O(N) operation — slow when the list is large.

- A `deque` (double-ended queue) is not an array. Internally it's implemented as a linked structure (conceptually like a doubly-linked list):

	(Head) -> [A] <-> [B] <-> [C] -> (Tail)

	To remove the first element ([A]) the deque does not shift anything. It simply updates the head pointer to [B]:

	(Head) -> [B] <-> [C] -> (Tail)

	That pointer update is an O(1) operation — constant time regardless of queue size.

You've completely mastered the concept. The tool for a Queue is `deque`. The operations are `append()` (to the back) and `popleft()` (from the front).

Use deque instead
- The standard tool is `collections.deque` (double-ended queue). `deque.append()` and `deque.popleft()` are both O(1) amortized.

---

Quick mapping

enqueue -> deque.append(item)
dequeue -> deque.popleft()
peek    -> deque[0]

---

Minimal Queue wrapper (deque-backed)

```python
from collections import deque

class SimpleQueue:
	"""Small deque-backed FIFO queue with safe operations."""
	def __init__(self):
		self._dq = deque()

	def enqueue(self, item):
		self._dq.append(item)

	def dequeue(self):
		if not self._dq:
			raise IndexError("dequeue from empty queue")
		return self._dq.popleft()

	def peek(self):
		if not self._dq:
			raise IndexError("peek from empty queue")
		return self._dq[0]

	def is_empty(self):
		return len(self._dq) == 0

	def size(self):
		return len(self._dq)
```

---

Example use-case: level-order traversal (BFS) or task scheduling — queues mirror real-world lines.

Complexity
- enqueue: O(1)
- dequeue: O(1)
- peek: O(1)
- Space: O(N)

Edge cases and tips
- Never use `list.pop(0)` in a loop for large lists.
- `deque` is safe, fast, and part of the standard library.
- For thread-safe queues use `queue.Queue` (has locking and blocking methods).

Practice problems
- Implement a circular buffer (fixed-size queue) — good exercise on capacity handling.
- Use a queue to implement BFS on a small graph.

Run the demo

I added a small demo file `Queue.py` next to this README; run it to see enqueue/dequeue/peek in action:

```powershell
python .\Queue.py
```

If you'd like, I can also:
- add a `linked-list`-backed Queue implementation for comparison, or
- add `unittest`/`pytest` tests for `SimpleQueue`.

---

Notes
- This file follows the same rich-doc pattern used in earlier days: short intuition, code, complexity, and run instructions.
