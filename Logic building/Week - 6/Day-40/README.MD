# Day 40 — Queue Applications

**Topic**: Stacks & Queues (Queue Applications)

---

## 📚 Purpose

This guide covers two classic "design" problems that test a deep understanding of FIFO (Queue) vs. LIFO (Stack) principles.

- **Pattern 1**: The "Two-Stack Queue" (Simulating FIFO with LIFO tools)
- **Pattern 2**: The "Sliding Time Window" (A classic deque use case)

**Key Concept**: Amortized O(1) Time

---

## 🎯 TL;DR

**Two-Stack Queue**: Use `stack_in` for all push operations. Use `stack_out` for all pop/peek operations. Only transfer from in to out when `stack_out` is empty. This gives Amortized O(1) performance.

**Sliding Time Window**: Use a deque (not a list!) to efficiently manage a data window with a variable size (like time).

**The Trap**: Using a list and re-scanning it (`for p in self.pings...`) is O(N) per call and will TLE (Time Limit Exceeded). The deque solution is Amortized O(1) per call.

---

## 🎨 Pattern 1: Implement Queue Using Stacks (LeetCode 232)

💡 Core Idea (FIFO using LIFO)

This is a "design" brain-teaser.

**Goal**: Build a FIFO (Queue) behavior.

**Tools**: Only LIFO (Stack) tools.

**The mismatch**:
- Queue (Goal): `enqueue(1), enqueue(2), enqueue(3)`. `dequeue()` must return 1.
- Stack (Tool): `push(1), push(2), push(3)`. `pop()` returns 3.

We use two stacks to reverse the order.

- **`stack_in`**: The "inbox." All `push(x)` calls go here. (Fast, O(1))
- **`stack_out`**: The "outbox." All `pop()` and `peek()` calls come from here.

### 🧠 The "Amortized Transfer" Logic

**`push(x)`**: Always `stack_in.append(x)`. This is O(1).

**`pop()` / `peek()`**:
1. Check if `stack_out` is empty.
2. If `stack_out` is empty: `while stack_in: -> stack_out.append(stack_in.pop())`. This is the O(N) transfer that reverses the order.
3. If `stack_out` is not empty, we skip the transfer.
4. Return `stack_out.pop()` or `stack_out[-1]`.

This is **"Amortized O(1)"** because the slow O(N) transfer only happens rarely. Most calls are just a fast O(1) pop from `stack_out`.

---

### 📝 Implementation (Refactored for DRY)

We use a private helper `_transfer_if_needed()` to avoid repeating code.

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your two stacks here.
        stack_in: The "inbox"
        stack_out: The "outbox"
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue. O(1)
        """
        self.stack_in.append(x)

    def _transfer_if_needed(self) -> None:
        """
        Private helper.
        If stack_out is empty, it transfers all elements
        from stack_in to stack_out, reversing them.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        Amortized O(1).
        """
        # 1. Call the helper. It will fill stack_out if needed.
        self._transfer_if_needed()
        
        # 2. Now we can safely pop from stack_out.
        return self.stack_out.pop() if self.stack_out else None

    def peek(self) -> int:
        """
        Get the front element.
        Amortized O(1).
        """
        # 1. Call the helper. It will fill stack_out if needed.
        self._transfer_if_needed()
        
        # 2. Now we can safely peek at stack_out.
        return self.stack_out[-1] if self.stack_out else None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty. O(1).
        The queue is empty if *both* stacks are empty.
        """
        return not self.stack_in and not self.stack_out
```

---

### ⏱️ Complexity

- **push Time**: O(1)
- **pop/peek Time**: Amortized O(1)
- **Space**: O(N) (to hold all elements in the stacks)

---

## 🎨 Pattern 2: Sliding Time Window — "Number of Recent Calls" (LeetCode 933)

💡 Core Idea (FIFO for a Time Window)

We need to count pings in the range `[t - 3000, t]`.

**The "Chutiyapaa" (Trap)**: Using a list.
- `self.pings.append(t)` (fast, O(1)).
- `for p in self.pings: ...` (slow, O(N) per call).
- This re-scans all 1 million old pings every time. It will TLE.

**The "Aha!" Moment (FIFO)**:
- New pings (t) are added to the **BACK** of a line.
- Old, expired pings (< t - 3000) are removed from the **FRONT**.
- This is a perfect FIFO problem. The correct tool is a **deque**.

### 🧠 The 3-Step Logic

For every `ping(t)`:

1. **Add New "Ticket" (to BACK)**: `self.tickets.append(t)`
2. **Find "Cutoff"**: `cutoff = t - 3000`
3. **Clean "Old Tickets" (from FRONT)**:
   ```python
   while self.tickets and self.tickets[0] < cutoff:
       self.tickets.popleft()
   ```
4. **Return Count**: The answer is just the size of the deque.
   ```python
   return len(self.tickets)
   ```

---

### 📝 Implementation (LeetCode 933)

```python
from collections import deque

class RecentCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        We use a deque as a fast FIFO queue for our "tickets".
        """
        self.tickets = deque()

    def ping(self, t: int) -> int:
        """
        1. Add the new timestamp `t` to the back.
        2. Remove all old timestamps from the front.
        3. Return the new size.
        """
        
        # 1. Add the new "ticket" to the back
        self.tickets.append(t)
        
        # 2. Find the "cutoff" time
        cutoff = t - 3000
        
        # 3. Clean all old tickets from the front
        # This is the optimal, amortized O(1) logic.
        while self.tickets and self.tickets[0] < cutoff:
            self.tickets.popleft()
        
        # 4. The size of the deque *is* the answer
        return len(self.tickets)
```

---

### ⏱️ Complexity

- **Time**: Amortized O(1)
  - Every ping is `append()`ed once and `popleft()`ed at most once. The average cost is constant.
- **Space**: O(W)
  - The deque size is limited by the window W (3000). It does not grow to N (1 million). This is effectively constant O(1) space.

---

