## Day - 39 Deque (clean, practical reference)

TL;DR
- A deque (double-ended queue) supports O(1) adds/removes at both front and back. In Python use `collections.deque` for production; build a DLL-backed `MyDeque` when asked to implement it yourself.

Quick operations table

| Operation | Python deque | Method | Complexity |
|---:|---|---|---:|
| add to back | deque.append(x) | right | O(1) |
| add to front | deque.appendleft(x) | left | O(1) |
| pop back | deque.pop() | right | O(1) |
| pop front | deque.popleft() | left | O(1) |

When to use
- Sliding-window maxima, monotonic queues, deque-based BFS variants, and double-ended buffers.

---

Problem 1 — Sliding Window Maximum (monotonic deque)

Idea in one sentence: keep indices of window elements in a deque in decreasing-by-value order so the max is always at the front.

Clean, runnable solution (Python):

```python
from collections import deque
from typing import List

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    if not nums or k <= 0:
        return []
    q = deque()  # will store indices, values in decreasing order
    out = []
    for i, val in enumerate(nums):
        # 1) remove indices outside the window
        if q and q[0] <= i - k:
            q.popleft()

        # 2) remove smaller values from the back
        while q and nums[q[-1]] <= val:
            q.pop()

        # 3) add current index
        q.append(i)

        # 4) record result when first full window is reached
        if i >= k - 1:
            out.append(nums[q[0]])

    return out

# Example
if __name__ == "__main__":
    print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
```

Complexity: O(N) time (each index enters/exits deque at most once), O(k) extra space.

---

Problem 2 — Implementing `MyDeque` (Doubly-Linked List)

When asked to build a deque from scratch for a coding problem, implement a small DLL with `head`, `tail`, and `size`. Keep methods short and handle edge cases explicitly.

Example implementation (straightforward, tested):

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_front(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def add_back(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            return None
        val = self.head.val
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return val

    def remove_back(self):
        if self.is_empty():
            return None
        val = self.tail.val
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return val

    def peek_front(self):
        return self.head.val if self.head else None

    def peek_back(self):
        return self.tail.val if self.tail else None
```

Edge cases to test
- Empty deque: removals return `None` (or raise — decide and document).
- Single-item deque: both `head` and `tail` must be updated to `None` after removal.

---

Tips & interview notes
- When solving sliding-window problems, store indices (not values) in the deque so you can check window bounds cheaply.
- In Python, prefer the built-in `deque` for correctness and speed unless the exercise explicitly asks for a manual implementation.
- Keep your `MyDeque` methods O(1) and handle 0/1 element cases first — it's where many bugs hide.

---
