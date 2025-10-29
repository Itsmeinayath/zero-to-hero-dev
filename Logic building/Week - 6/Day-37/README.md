# Day 37 — Queue Basics (short)

- Queue = FIFO (first-in, first-out). Use `collections.deque` for efficient queues in Python. Avoid `list.pop(0)` (O(N)).

Cheat-sheet
- Import: `from collections import deque`
- Enqueue: `dq.append(x)` (right)
- Dequeue: `dq.popleft()` (left)
- Peek: `dq[0]` (check empty first)
- Empty: `not dq`
- Complexity: append/popleft/peek = O(1)

Quick visual (why deque > list)
- list: [A][B][C][D] -> pop(0) shifts all elements -> O(N)
- deque: head->[A]<->[B]<->[C] tail -> popleft() updates head pointer -> O(1)

Minimal MyQueue (copy-paste)
```python
from collections import deque

class MyQueue:
    def __init__(self):
        self._dq = deque()

    def enqueue(self, x):
        self._dq.append(x)

    def dequeue(self):
        return self._dq.popleft() if self._dq else None

    def peek(self):
		# Day 37 — Queue Basics (rich & clean)

		What this file gives you
		- Short intuition, a small visual, copy-paste `MyQueue`, an example (BFS), and a compact interview twist (stack via queues). Quick to read, useful to keep in your repo.

		TL;DR
		- Queue = FIFO. Use `collections.deque` in Python — O(1) append and popleft. Avoid repeated `list.pop(0)`.

		Quick visual
		- list: [A][B][C][D] -> pop(0) shifts all elements -> O(N)
		- deque: head->[A]<->[B]<->[C] tail -> popleft() updates head pointer -> O(1)

		Cheat-sheet
		- Import: `from collections import deque`
		- Enqueue: `dq.append(x)`
		- Dequeue: `dq.popleft()`
		- Peek: `dq[0]` (check empty first)

		Minimal, production-minded MyQueue

		```python
		from collections import deque

		class MyQueue:
			"""Simple deque-backed FIFO queue with a clear API.

			- Returns None on empty dequeue/peek to simplify demos/tests.
			- Use this as a small building block in exercises and examples.
			"""

			def __init__(self):
				self._dq = deque()

			def enqueue(self, item):
				self._dq.append(item)

			def dequeue(self):
				return self._dq.popleft() if self._dq else None

			def peek(self):
				return self._dq[0] if self._dq else None

			def is_empty(self):
				return not self._dq

			def size(self):
				return len(self._dq)
		```

		Example: BFS (level-order)

		```python
		from collections import deque

		def bfs(root):
			if not root: return []
			q = deque([root])
			out = []
			while q:
				node = q.popleft()
				out.append(node.val)
				if node.left: q.append(node.left)
				if node.right: q.append(node.right)
			return out
		```

		Interview twist — stack via one queue (push-heavy)

		```python
		from collections import deque

		class MyStackUsingQueues:
			def __init__(self):
				self.q = deque()

			def push(self, x):
				self.q.append(x)
				for _ in range(len(self.q)-1):
					self.q.append(self.q.popleft())

			def pop(self):
				return self.q.popleft() if self.q else None

			def top(self):
				return self.q[0] if self.q else None
		```

		Complexities
		- enqueue/popleft/peek: O(1)
		- push (stack-via-queue): O(N) (rotation); pop/top: O(1)


		Practice (quick)
		- Implement a circular buffer (fixed-size queue). Compare behavior & complexity.
		- LeetCode: Implement Stack Using Queues — try both push-heavy and pop-heavy.

		If you'd like, I'll now:
		- run `Queue.py` and paste the output, or
		- add `unittest` tests for `MyQueue` and `MyStackUsingQueues`, or
		- trim further to a one-paragraph TL;DR + single copyable MyQueue block.
```



