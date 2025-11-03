# Day 40 — Queue Applications# Day 40 — Queue Applications

   

**Date**: November 3, 2025  **Topic**: Stacks & Queues (Queue Applications, Two-Stack Queue, Sliding Time Window)

**Topic**: Stacks & Queues (Queue Applications, Two-Stack Queue, Sliding Time Window)

## 📚 Purpose

## 📚 Purpose

Master queue implementation patterns and real-world queue applications:

Master queue implementation patterns and real-world queue applications:- **Pattern 1**: Two-Stack Queue (Build FIFO using LIFO tools)

- **Pattern 1**: Two-Stack Queue (Build FIFO using LIFO tools)- **Pattern 2**: Sliding Time Window (Efficient time-based filtering with deque)

- **Pattern 2**: Sliding Time Window (Efficient time-based filtering with deque)

---

---

## 🎯 TL;DR

## 🎯 TL;DR

**Two-Stack Queue**: Build a queue using two stacks (`stack_in` for enqueue, `stack_out` for dequeue). Transfer elements lazily for amortized O(1) operations.

**Two-Stack Queue**: Build a queue using two stacks (`stack_in` for enqueue, `stack_out` for dequeue). Transfer elements lazily for amortized O(1) operations.

**Sliding Time Window**: Use a deque to efficiently maintain a time-based sliding window. Add new items to back, remove expired items from front — amortized O(1).

**Sliding Time Window**: Use a deque to efficiently maintain a time-based sliding window. Add new items to back, remove expired items from front — amortized O(1).

**Key Insight**: Both patterns avoid the O(N) trap (nested loops or full scans) by using smart data structure choices and lazy operations.

**Key Insight**: Both patterns avoid the O(N) trap (nested loops or full scans) by using smart data structure choices and lazy operations.

---

---

## 🎨 Pattern 1: Two-Stack Queue — "Implement Queue using Stacks"

## 🎨 Pattern 1: Two-Stack Queue — "Implement Queue using Stacks"

### 💡 Core Idea (The "Inbox/Outbox" Pattern)

### 💡 Core Idea (The "Inbox/Outbox" Pattern)

**Design Challenge**: Build a FIFO (queue) using only LIFO (stack) tools.

**Design Challenge**: Build a FIFO (queue) using only LIFO (stack) tools.

**Naive Approach**: Single stack doesn't work

**Naive Approach**: Single stack doesn't work- `push(1), push(2)` → stack = `[1, 2]` (top at right)

- `push(1), push(2)` → stack = `[1, 2]` (top at right)- `pop()` returns 2 ❌ (should return 1 for FIFO)

- `pop()` returns 2 ❌ (should return 1 for FIFO)

**Optimal Solution**: Use **two stacks**

**Optimal Solution**: Use **two stacks**1. **`stack_in`**: "Inbox" — all `push` operations go here

1. **`stack_in`**: "Inbox" — all `push` operations go here2. **`stack_out`**: "Outbox" — all `pop`/`peek` operations come from here

2. **`stack_out`**: "Outbox" — all `pop`/`peek` operations come from here

### 🧠 The Amortized O(1) Transfer Magic

### 🧠 The Amortized O(1) Transfer Magic

This is the core logic that makes it efficient:

This is the core logic that makes it efficient:

#### `push(x)` — Always Fast

#### `push(x)` — Always Fast- Simply: `stack_in.append(x)` → **O(1)**

- Simply: `stack_in.append(x)` → **O(1)**

#### `pop()` / `peek()` — Lazy Transfer

#### `pop()` / `peek()` — Lazy Transfer1. Check if `stack_out` is empty

1. Check if `stack_out` is empty2. If empty, transfer **all** elements from `stack_in` to `stack_out`

2. If empty, transfer **all** elements from `stack_in` to `stack_out`   - This reverses the order: `[1, 2, 3]` (top) → `[3, 2, 1]` (top)

   - This reverses the order: `[1, 2, 3]` (top) → `[3, 2, 1]` (top)   - Now the "front" of queue (1) is at top of `stack_out`

   - Now the "front" of queue (1) is at top of `stack_out`3. Pop/peek from `stack_out`

3. Pop/peek from `stack_out`

**Why Amortized O(1)?**

**Why Amortized O(1)?**- The transfer is O(N) but happens **rarely**

- The transfer is O(N) but happens **rarely**- Each element is transferred at most once

- Each element is transferred at most once- Most operations are just a single pop/peek → O(1)

- Most operations are just a single pop/peek → O(1)

### 📝 Implementation (LeetCode 232)

### 📝 Implementation (LeetCode 232)

```python

```pythonclass MyQueue:

class MyQueue:    """

    """    Queue implementation using two stacks.

    Queue implementation using two stacks.    Uses lazy transfer for amortized O(1) operations.

    Uses lazy transfer for amortized O(1) operations.    """

    """        self.stack_in = []

        self.stack_out = []

    def __init__(self):

        self.stack_in = []   # Inbox for push operations    def push(self, x: int) -> None:

        self.stack_out = []  # Outbox for pop/peek operations        # Always push to the "inbox"

        self.stack_in.append(x)

    def push(self, x: int) -> None:

        """Add element to the back of queue - O(1)."""    def _transfer_if_needed(self) -> None:

        # Always push to the "inbox"        # This is a private helper to keep our code DRY

        self.stack_in.append(x)        # (Don't Repeat Yourself)

        

    def _transfer_if_needed(self) -> None:        # Only transfer if the "outbox" is empty

        """        if not self.stack_out:

        Private helper to transfer elements from in to out.            while self.stack_in:

        Only transfers when outbox is empty (lazy evaluation).                # Pop from in, push to out, reversing the order

        """                self.stack_out.append(self.stack_in.pop())

        # Only transfer if the "outbox" is empty

        if not self.stack_out:    def pop(self) -> int:

            while self.stack_in:        # Fill the "outbox" if it's empty

                # Pop from in, push to out → reverses order        self._transfer_if_needed()

                self.stack_out.append(self.stack_in.pop())        

        # Pop from the "outbox"

    def pop(self) -> int:        return self.stack_out.pop() if self.stack_out else None

        """Remove and return element from front - Amortized O(1)."""

        # Fill the "outbox" if it's empty    def peek(self) -> int:

        self._transfer_if_needed()        # Fill the "outbox" if it's empty

                self._transfer_if_needed()

        # Pop from the "outbox"        

        return self.stack_out.pop() if self.stack_out else None        # Peek at the top of the "outbox"

        return self.stack_out[-1] if self.stack_out else None

    def peek(self) -> int:

        """Get front element without removing - Amortized O(1)."""    def empty(self) -> bool:

        # Fill the "outbox" if it's empty        # The queue is empty ONLY if *both* stacks are empty

        self._transfer_if_needed()        return not self.stack_in and not self.stack_out

        Complexitypush Time: $O(1)$pop/peek Time: Amortized $O(1)$Space: $O(N)$2. Problem 2: LeetCode: Number of Recent Calls (Easy)Analysis & LogicThis is a classic "Sliding Time Window" problem. We need to count pings in the range [t - 3000, t].The "Chutiyapaa" (Trap): Using a list.self.pings.append(t) (fast, $O(1)$).for p in self.pings: ... (slow, $O(N)$ per call).This re-scans all 1 million old pings every time. It's a "Time Limit Exceeded" solution.Optimal (The $O(1)$ "Aha!" Moment): This is a FIFO problem.New pings (t) are added to the BACK.Old pings (expired tickets) are removed from the FRONT.The perfect tool is a deque.The 3-Step LogicFor every ping(t):Add New "Ticket" (to BACK): self.tickets.append(t)Find "Cutoff": cutoff = t - 3000Clean "Old Tickets" (from FRONT):while self.tickets and self.tickets[0] < cutoff:self.tickets.popleft()Return Count: After cleaning, every ticket in the deque is valid.return len(self.tickets)Final Solution CodePythonfrom collections import deque

        # Peek at the top of the "outbox"

        return self.stack_out[-1] if self.stack_out else Noneclass RecentCounter:



    def empty(self) -> bool:    def __init__(self):

        """Check if queue is empty - O(1)."""        # Use a deque as a fast FIFO queue

        # Queue is empty ONLY if *both* stacks are empty        self.tickets = deque()

        return not self.stack_in and not self.stack_out

    def ping(self, t: int) -> int:

        

# Test        # 1. Add the new "ticket" to the back

if __name__ == '__main__':        self.tickets.append(t)

    q = MyQueue()        

    q.push(1)        # 2. Find the "cutoff" time

    q.push(2)        cutoff = t - 3000

    print(q.peek())   # 1        

    print(q.pop())    # 1        # 3. Clean all old tickets from the front

    print(q.empty())  # False        while self.tickets and self.tickets[0] < cutoff:

    print(q.pop())    # 2            self.tickets.popleft()

    print(q.empty())  # True        

```        # 4. The size of the deque *is* the answer

        return len(self.tickets)

### ⏱️ ComplexityComplexityTime: Amortized $O(1)$Every ping is append()ed once and popleft()ed at most once. The average cost is constant.Space: $O(W)$The deque size is limited by the window W (3000). It does not grow to $N$ (1 million). This is effectively constant space.

- **Time**:
  - `push`: O(1)
  - `pop`/`peek`: **Amortized O(1)** (each element transferred at most once)
  - `empty`: O(1)
- **Space**: O(N) for N elements

### 🎯 Visual Trace

```
Operation Sequence:

push(1):
  stack_in = [1]
  stack_out = []

push(2):
  stack_in = [1, 2]
  stack_out = []

push(3):
  stack_in = [1, 2, 3]
  stack_out = []

pop():
  Transfer needed! (stack_out is empty)
  Transfer: stack_in [1,2,3] → stack_out [3,2,1]
  After transfer:
    stack_in = []
    stack_out = [3, 2, 1]
  Pop from stack_out → return 1
  stack_out = [3, 2]

pop():
  No transfer (stack_out has items)
  Pop from stack_out → return 2
  stack_out = [3]

push(4):
  stack_in = [4]
  stack_out = [3]

pop():
  No transfer (stack_out has items)
  Pop from stack_out → return 3
  stack_out = []

pop():
  Transfer needed!
  Transfer: stack_in [4] → stack_out [4]
  Pop from stack_out → return 4
```

### 🔑 Key Insight

Each element follows this journey:
1. Pushed to `stack_in` (1 operation)
2. Transferred to `stack_out` (1 operation)
3. Popped from `stack_out` (1 operation)

**Total**: 3 operations per element across its lifetime → **Amortized O(1)**

---

## 🎨 Pattern 2: Sliding Time Window — "Number of Recent Calls"

### 💡 Core Idea (The "Ticket Window" Pattern)

**Problem**: Count pings in the time range `[t - 3000, t]`.

**Naive Approach** (O(N) Trap): Using a list
```python
self.pings.append(t)  # O(1)
for p in self.pings:  # O(N) - scans all pings every time!
    if t - 3000 <= p <= t:
        count += 1
```
- Re-scans all 1 million old pings every call → **Time Limit Exceeded**

**Optimal Solution** (O(1) Amortized): This is a FIFO problem!
- New pings (t) added to **BACK**
- Old expired pings removed from **FRONT**
- Perfect tool: **`deque`**

### 🧠 The 4-Step Logic

For every `ping(t)`:

1. **Add New "Ticket"** (to BACK): `self.tickets.append(t)`
2. **Find "Cutoff"**: `cutoff = t - 3000`
3. **Clean "Old Tickets"** (from FRONT):
   ```python
   while self.tickets and self.tickets[0] < cutoff:
       self.tickets.popleft()
   ```
4. **Return Count**: After cleaning, all tickets in deque are valid
   ```python
   return len(self.tickets)
   ```

### 📝 Implementation (LeetCode 933)

```python
from collections import deque

class RecentCounter:
    """
    Counter for requests in the last 3000ms.
    Uses deque for efficient sliding time window.
    """

    def __init__(self):
        # Use a deque as a fast FIFO queue
        self.tickets = deque()

    def ping(self, t: int) -> int:
        """
        Record a new request at time t and return count of requests
        in the range [t-3000, t].
        
        Args:
            t: Current timestamp in milliseconds
            
        Returns:
            Number of requests in the last 3000ms
        """
        # 1. Add the new "ticket" to the back
        self.tickets.append(t)
        
        # 2. Find the "cutoff" time
        cutoff = t - 3000
        
        # 3. Clean all old tickets from the front
        while self.tickets and self.tickets[0] < cutoff:
            self.tickets.popleft()
        
        # 4. The size of the deque *is* the answer
        return len(self.tickets)


# Test
if __name__ == '__main__':
    counter = RecentCounter()
    print(counter.ping(1))     # 1 (requests: [1])
    print(counter.ping(100))   # 2 (requests: [1, 100])
    print(counter.ping(3001))  # 3 (requests: [1, 100, 3001])
    print(counter.ping(3002))  # 3 (requests: [100, 3001, 3002])
                               # 1 is expired (< 3002-3000=2)
```

### ⏱️ Complexity

- **Time**: **Amortized O(1)**
  - Every ping is `append()`ed once and `popleft()`ed at most once
  - Average cost per operation is constant
- **Space**: **O(W)** where W = window size (3000ms)
  - Deque size limited by window, not total requests
  - Even with 1 million pings, max size ≈ 3000 items

### 🎯 Visual Trace

```
Window = 3000ms

ping(1):
  tickets = [1]
  cutoff = 1 - 3000 = -2999
  No cleanup needed
  return 1

ping(100):
  tickets = [1, 100]
  cutoff = 100 - 3000 = -2900
  No cleanup needed
  return 2

ping(3001):
  tickets = [1, 100, 3001]
  cutoff = 3001 - 3000 = 1
  Cleanup: 1 >= 1, keep it
  return 3

ping(3002):
  tickets = [1, 100, 3001, 3002]
  cutoff = 3002 - 3000 = 2
  Cleanup: 1 < 2, remove it
  tickets = [100, 3001, 3002]
  return 3

ping(6500):
  tickets = [100, 3001, 3002, 6500]
  cutoff = 6500 - 3000 = 3500
  Cleanup: 100 < 3500, remove
           3001 < 3500, remove
           3002 < 3500, remove
  tickets = [6500]
  return 1
```

### 🔑 Why Deque is Perfect

| Operation | List | Deque |
|-----------|------|-------|
| Add to back | O(1) | O(1) |
| Remove from front | O(N) ❌ | O(1) ✅ |
| Memory | Contiguous | Efficient chunks |

For sliding windows, **always use deque** for O(1) removals from front.

---

## 🎓 Interview Tips

1. **Two-Stack Queue Pattern**:
   - Use lazy transfer (only when `stack_out` is empty)
   - Remember: queue empty = **both** stacks empty
   - Amortized analysis: each element moved at most once

2. **Sliding Time Window Pattern**:
   - Use `deque` for FIFO with efficient front removal
   - Add new items to back, remove expired from front
   - Window size limits space (not total elements)

3. **Common Mistakes**:
   - Using list for sliding window (O(N) `list.pop(0)`)
   - Transferring on every pop (should be lazy)
   - Forgetting to check both stacks for empty queue

4. **Amortized O(1) Explained**:
   - Individual operation might be O(N)
   - But averaged over many operations = O(1)
   - Each element processed constant times total

---

## 📝 Practice Problems

| Problem | Difficulty | Pattern | Link |
|---------|-----------|---------|------|
| Implement Queue using Stacks | Easy | Two-Stack Queue | [LeetCode 232](https://leetcode.com/problems/implement-queue-using-stacks/) |
| Number of Recent Calls | Easy | Sliding Time Window | [LeetCode 933](https://leetcode.com/problems/number-of-recent-calls/) |
| Implement Stack using Queues | Easy | Two-Queue Stack | [LeetCode 225](https://leetcode.com/problems/implement-stack-using-queues/) |
| Moving Average from Data Stream | Easy | Sliding Window | [LeetCode 346](https://leetcode.com/problems/moving-average-from-data-stream/) |

---

## 🚀 Run the Code

Save and test the implementations:

```bash
# Test Two-Stack Queue
python day-40-queue-using-stacks.py

# Test Sliding Time Window
python day-40-recent-counter.py
```

Or test interactively:

```python
python -i day-40-queue-using-stacks.py
>>> q = MyQueue()
>>> q.push(1)
>>> q.push(2)
>>> q.pop()
1
```

---

**Made with ❤️ for interview prep**
