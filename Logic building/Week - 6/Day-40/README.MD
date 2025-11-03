# Day 40 — Queue Applications# Day 40 — Queue Applications# Day 40 — Queue Applications# Day 40 — Queue Applications



**Topic**: Queue Applications (Two-Stack Queue, Sliding Time Window)



---**Topic**: Stacks & Queues (Queue Applications, Two-Stack Queue, Sliding Time Window)**Topic**: Stacks & Queues (Queue Applications, Two-Stack Queue, Sliding Time Window)



## 📚 Purpose



Master queue implementation patterns and real-world applications:---



- **Pattern 1**: Two-Stack Queue — Build FIFO using LIFO stacks

- **Pattern 2**: Sliding Time Window — Efficient time-based filtering## 📚 Purpose



---Master queue implementation patterns and real-world queue applications:



## 🎯 TL;DRMaster queue implementation patterns and real-world queue applications:



**Two-Stack Queue**: Use two stacks (`stack_in` for push, `stack_out` for pop). Transfer lazily for amortized O(1).- **Pattern 1**: Two-Stack Queue (Build FIFO using LIFO tools)



**Sliding Time Window**: Use deque to maintain time-based window. Add to back, remove expired from front — amortized O(1).- **Pattern 2**: Sliding Time Window (Efficient time-based filtering with deque)Master queue implementation patterns and real-world queue applications:- **Pattern 1**: Two-Stack Queue (Build FIFO using LIFO tools)



---



## 🎨 Pattern 1: Two-Stack Queue---- **Pattern 1**: Two-Stack Queue (Build FIFO using LIFO tools)- **Pattern 2**: Sliding Time Window (Efficient time-based filtering with deque)



### 💡 Core Idea



**Challenge**: Build a FIFO queue using only LIFO stacks.## 🎯 TL;DR- **Pattern 2**: Sliding Time Window (Efficient time-based filtering with deque)



**Solution**: Use two stacks

- `stack_in` → all push operations

- `stack_out` → all pop/peek operations**Two-Stack Queue**: Build a queue using two stacks (`stack_in` for enqueue, `stack_out` for dequeue). Transfer elements lazily for amortized O(1) operations.---



**Key**: Transfer elements lazily (only when `stack_out` is empty)



### 📝 Implementation**Sliding Time Window**: Use a deque to efficiently maintain a time-based sliding window. Add new items to back, remove expired items from front — amortized O(1).---



```python

class MyQueue:

    def __init__(self):**Key Insight**: Both patterns avoid the O(N) trap (nested loops or full scans) by using smart data structure choices and lazy operations.## 🎯 TL;DR

        self.stack_in = []

        self.stack_out = []



    def push(self, x: int) -> None:---## 🎯 TL;DR

        self.stack_in.append(x)



    def _transfer_if_needed(self) -> None:

        if not self.stack_out:## 🎨 Pattern 1: Two-Stack Queue — "Implement Queue using Stacks"**Two-Stack Queue**: Build a queue using two stacks (`stack_in` for enqueue, `stack_out` for dequeue). Transfer elements lazily for amortized O(1) operations.

            while self.stack_in:

                self.stack_out.append(self.stack_in.pop())



    def pop(self) -> int:### 💡 Core Idea (The "Inbox/Outbox" Pattern)**Two-Stack Queue**: Build a queue using two stacks (`stack_in` for enqueue, `stack_out` for dequeue). Transfer elements lazily for amortized O(1) operations.

        self._transfer_if_needed()

        return self.stack_out.pop() if self.stack_out else None



    def peek(self) -> int:**Design Challenge**: Build a FIFO (queue) using only LIFO (stack) tools.**Sliding Time Window**: Use a deque to efficiently maintain a time-based sliding window. Add new items to back, remove expired items from front — amortized O(1).

        self._transfer_if_needed()

        return self.stack_out[-1] if self.stack_out else None



    def empty(self) -> bool:**Naive Approach**: Single stack doesn't work**Sliding Time Window**: Use a deque to efficiently maintain a time-based sliding window. Add new items to back, remove expired items from front — amortized O(1).

        return not self.stack_in and not self.stack_out

```- `push(1), push(2)` → stack = `[1, 2]` (top at right)



### ⏱️ Complexity- `pop()` returns 2 ❌ (should return 1 for FIFO)**Key Insight**: Both patterns avoid the O(N) trap (nested loops or full scans) by using smart data structure choices and lazy operations.



- **Time**: Push O(1), Pop/Peek Amortized O(1)

- **Space**: O(N)

**Optimal Solution**: Use **two stacks****Key Insight**: Both patterns avoid the O(N) trap (nested loops or full scans) by using smart data structure choices and lazy operations.

### 🎯 Visual Trace

1. **`stack_in`**: "Inbox" — all `push` operations go here

```

push(1), push(2), push(3):2. **`stack_out`**: "Outbox" — all `pop`/`peek` operations come from here---

  stack_in = [1, 2, 3]

  stack_out = []



pop():### 🧠 The Amortized O(1) Transfer Magic---

  Transfer: [1,2,3] → stack_out = [3,2,1]

  Pop from stack_out → return 1

  

pop():This is the core logic that makes it efficient:## 🎨 Pattern 1: Two-Stack Queue — "Implement Queue using Stacks"

  stack_out = [3] → return 2

```



---#### `push(x)` — Always Fast## 🎨 Pattern 1: Two-Stack Queue — "Implement Queue using Stacks"



## 🎨 Pattern 2: Sliding Time Window- Simply: `stack_in.append(x)` → **O(1)**



### 💡 Core Idea### 💡 Core Idea (The "Inbox/Outbox" Pattern)



**Problem**: Count requests in last 3000ms.#### `pop()` / `peek()` — Lazy Transfer



**Naive**: Scan entire list every time → O(N)1. Check if `stack_out` is empty### 💡 Core Idea (The "Inbox/Outbox" Pattern)



**Optimal**: Use deque (FIFO)2. If empty, transfer **all** elements from `stack_in` to `stack_out`

- Add new pings to back

- Remove expired from front   - This reverses the order: `[1, 2, 3]` (top) → `[3, 2, 1]` (top)**Design Challenge**: Build a FIFO (queue) using only LIFO (stack) tools.

- Amortized O(1)

   - Now the "front" of queue (1) is at top of `stack_out`

### 📝 Implementation

3. Pop/peek from `stack_out`**Design Challenge**: Build a FIFO (queue) using only LIFO (stack) tools.

```python

from collections import deque



class RecentCounter:**Why Amortized O(1)?****Naive Approach**: Single stack doesn't work

    def __init__(self):

        self.tickets = deque()- The transfer is O(N) but happens **rarely**



    def ping(self, t: int) -> int:- Each element is transferred at most once**Naive Approach**: Single stack doesn't work- `push(1), push(2)` → stack = `[1, 2]` (top at right)

        # Add new ping

        self.tickets.append(t)- Most operations are just a single pop/peek → O(1)

        

        # Remove expired- `push(1), push(2)` → stack = `[1, 2]` (top at right)- `pop()` returns 2 ❌ (should return 1 for FIFO)

        cutoff = t - 3000

        while self.tickets and self.tickets[0] < cutoff:### 📝 Implementation (LeetCode 232)

            self.tickets.popleft()

        - `pop()` returns 2 ❌ (should return 1 for FIFO)

        return len(self.tickets)

``````python



### ⏱️ Complexityclass MyQueue:**Optimal Solution**: Use **two stacks**



- **Time**: Amortized O(1) per ping    """

- **Space**: O(W) where W = window size (3000ms)

    Queue implementation using two stacks.**Optimal Solution**: Use **two stacks**1. **`stack_in`**: "Inbox" — all `push` operations go here

### 🎯 Visual Trace

    Uses lazy transfer for amortized O(1) operations.

```

ping(1):    tickets = [1] → return 1    """1. **`stack_in`**: "Inbox" — all `push` operations go here2. **`stack_out`**: "Outbox" — all `pop`/`peek` operations come from here

ping(100):  tickets = [1, 100] → return 2

ping(3001): tickets = [1, 100, 3001] → return 3

ping(3002): cutoff = 2, remove 1 → tickets = [100, 3001, 3002] → return 3

```    def __init__(self):2. **`stack_out`**: "Outbox" — all `pop`/`peek` operations come from here



---        self.stack_in = []   # Inbox for push operations



## 🔑 Key Insights        self.stack_out = []  # Outbox for pop/peek operations### 🧠 The Amortized O(1) Transfer Magic



1. **Two-Stack Queue**: Transfer lazily, not on every operation

2. **Sliding Window**: Deque for O(1) front removal (list is O(N))

3. **Amortized O(1)**: Each element processed constant times total    def push(self, x: int) -> None:### 🧠 The Amortized O(1) Transfer Magic



---        """Add element to the back of queue - O(1)."""



## 📝 Practice Problems        # Always push to the "inbox"This is the core logic that makes it efficient:



| Problem | Difficulty | Link |        self.stack_in.append(x)

|---------|-----------|------|

| Implement Queue using Stacks | Easy | [LeetCode 232](https://leetcode.com/problems/implement-queue-using-stacks/) |This is the core logic that makes it efficient:

| Number of Recent Calls | Easy | [LeetCode 933](https://leetcode.com/problems/number-of-recent-calls/) |

| Implement Stack using Queues | Easy | [LeetCode 225](https://leetcode.com/problems/implement-stack-using-queues/) |    def _transfer_if_needed(self) -> None:

| Moving Average from Data Stream | Easy | [LeetCode 346](https://leetcode.com/problems/moving-average-from-data-stream/) |

        """#### `push(x)` — Always Fast

---

        Private helper to transfer elements from in to out.

**Made with ❤️ for interview prep**

        Only transfers when outbox is empty (lazy evaluation).#### `push(x)` — Always Fast- Simply: `stack_in.append(x)` → **O(1)**

        """

        # Only transfer if the "outbox" is empty- Simply: `stack_in.append(x)` → **O(1)**

        if not self.stack_out:

            while self.stack_in:#### `pop()` / `peek()` — Lazy Transfer

                # Pop from in, push to out → reverses order

                self.stack_out.append(self.stack_in.pop())#### `pop()` / `peek()` — Lazy Transfer1. Check if `stack_out` is empty



    def pop(self) -> int:1. Check if `stack_out` is empty2. If empty, transfer **all** elements from `stack_in` to `stack_out`

        """Remove and return element from front - Amortized O(1)."""

        # Fill the "outbox" if it's empty2. If empty, transfer **all** elements from `stack_in` to `stack_out`   - This reverses the order: `[1, 2, 3]` (top) → `[3, 2, 1]` (top)

        self._transfer_if_needed()

           - This reverses the order: `[1, 2, 3]` (top) → `[3, 2, 1]` (top)   - Now the "front" of queue (1) is at top of `stack_out`

        # Pop from the "outbox"

        return self.stack_out.pop() if self.stack_out else None   - Now the "front" of queue (1) is at top of `stack_out`3. Pop/peek from `stack_out`



    def peek(self) -> int:3. Pop/peek from `stack_out`

        """Get front element without removing - Amortized O(1)."""

        # Fill the "outbox" if it's empty**Why Amortized O(1)?**

        self._transfer_if_needed()

        **Why Amortized O(1)?**- The transfer is O(N) but happens **rarely**

        # Peek at the top of the "outbox"

        return self.stack_out[-1] if self.stack_out else None- The transfer is O(N) but happens **rarely**- Each element is transferred at most once



    def empty(self) -> bool:- Each element is transferred at most once- Most operations are just a single pop/peek → O(1)

        """Check if queue is empty - O(1)."""

        # Queue is empty ONLY if *both* stacks are empty- Most operations are just a single pop/peek → O(1)

        return not self.stack_in and not self.stack_out

### 📝 Implementation (LeetCode 232)



# Test```python

if __name__ == '__main__':class MyQueue:

    q = MyQueue()    """

    q.push(1)    Queue implementation using two stacks.

    q.push(2)    Uses lazy transfer for amortized O(1) operations.

    print(q.peek())   # 1    """

    print(q.pop())    # 1

    print(q.empty())  # False    def __init__(self):

    print(q.pop())    # 2        self.stack_in = []   # Inbox for push operations

    print(q.empty())  # True        self.stack_out = []  # Outbox for pop/peek operations

```

    def push(self, x: int) -> None:

### ⏱️ Complexity        """Add element to the back of queue - O(1)."""

        # Always push to the "inbox"

- **Time**:        self.stack_in.append(x)

  - `push`: O(1)

  - `pop`/`peek`: **Amortized O(1)** (each element transferred at most once)    def _transfer_if_needed(self) -> None:

  - `empty`: O(1)        """

- **Space**: O(N) for N elements        Private helper to transfer elements from in to out.

        Only transfers when outbox is empty (lazy evaluation).

### 🎯 Visual Trace        """

        # Only transfer if the "outbox" is empty

```        if not self.stack_out:

Operation Sequence:            while self.stack_in:

                # Pop from in, push to out → reverses order

push(1):                self.stack_out.append(self.stack_in.pop())

  stack_in = [1]

  stack_out = []    def pop(self) -> int:

        """Remove and return element from front - Amortized O(1)."""

push(2):        # Fill the "outbox" if it's empty

  stack_in = [1, 2]        self._transfer_if_needed()

  stack_out = []        

        # Pop from the "outbox"

push(3):        return self.stack_out.pop() if self.stack_out else None

  stack_in = [1, 2, 3]

  stack_out = []    def peek(self) -> int:

        """Get front element without removing - Amortized O(1)."""

pop():        # Fill the "outbox" if it's empty

  Transfer needed! (stack_out is empty)        self._transfer_if_needed()

  Transfer: stack_in [1,2,3] → stack_out [3,2,1]        

  After transfer:        # Peek at the top of the "outbox"

    stack_in = []        return self.stack_out[-1] if self.stack_out else None

    stack_out = [3, 2, 1]

  Pop from stack_out → return 1    def empty(self) -> bool:

  stack_out = [3, 2]        """Check if queue is empty - O(1)."""

        # Queue is empty ONLY if *both* stacks are empty

pop():        return not self.stack_in and not self.stack_out

  No transfer (stack_out has items)

  Pop from stack_out → return 2

  stack_out = [3]# Test

if __name__ == '__main__':

push(4):    q = MyQueue()

  stack_in = [4]    q.push(1)

  stack_out = [3]    q.push(2)

    print(q.peek())   # 1

pop():    print(q.pop())    # 1

  No transfer (stack_out has items)    print(q.empty())  # False

  Pop from stack_out → return 3    print(q.pop())    # 2

  stack_out = []    print(q.empty())  # True

```

pop():

  Transfer needed!### ⏱️ Complexity

  Transfer: stack_in [4] → stack_out [4]

  Pop from stack_out → return 4- **Time**:

```  - `push`: O(1)

  - `pop`/`peek`: **Amortized O(1)** (each element transferred at most once)

### 🔑 Key Insight  - `empty`: O(1)

- **Space**: O(N) for N elements

Each element follows this journey:

1. Pushed to `stack_in` (1 operation)### 🎯 Visual Trace

2. Transferred to `stack_out` (1 operation)

3. Popped from `stack_out` (1 operation)```

Operation Sequence:

**Total**: 3 operations per element across its lifetime → **Amortized O(1)**

push(1):

---  stack_in = [1]

  stack_out = []

## 🎨 Pattern 2: Sliding Time Window — "Number of Recent Calls"

push(2):

### 💡 Core Idea (The "Ticket Window" Pattern)  stack_in = [1, 2]

  stack_out = []

**Problem**: Count pings in the time range `[t - 3000, t]`.

push(3):

**Naive Approach** (O(N) Trap): Using a list  stack_in = [1, 2, 3]

```python  stack_out = []

self.pings.append(t)  # O(1)

for p in self.pings:  # O(N) - scans all pings every time!pop():

    if t - 3000 <= p <= t:  Transfer needed! (stack_out is empty)

        count += 1  Transfer: stack_in [1,2,3] → stack_out [3,2,1]

```  After transfer:

- Re-scans all 1 million old pings every call → **Time Limit Exceeded**    stack_in = []

    stack_out = [3, 2, 1]

**Optimal Solution** (O(1) Amortized): This is a FIFO problem!  Pop from stack_out → return 1

- New pings (t) added to **BACK**  stack_out = [3, 2]

- Old expired pings removed from **FRONT**

- Perfect tool: **`deque`**pop():

  No transfer (stack_out has items)

### 🧠 The 4-Step Logic  Pop from stack_out → return 2

  stack_out = [3]

For every `ping(t)`:

push(4):

1. **Add New "Ticket"** (to BACK): `self.tickets.append(t)`  stack_in = [4]

2. **Find "Cutoff"**: `cutoff = t - 3000`  stack_out = [3]

3. **Clean "Old Tickets"** (from FRONT):

   ```pythonpop():

   while self.tickets and self.tickets[0] < cutoff:  No transfer (stack_out has items)

       self.tickets.popleft()  Pop from stack_out → return 3

   ```  stack_out = []

4. **Return Count**: After cleaning, all tickets in deque are valid

   ```pythonpop():

   return len(self.tickets)  Transfer needed!

   ```  Transfer: stack_in [4] → stack_out [4]

  Pop from stack_out → return 4

### 📝 Implementation (LeetCode 933)```



```python### 🔑 Key Insight

from collections import deque

Each element follows this journey:

class RecentCounter:1. Pushed to `stack_in` (1 operation)

    """2. Transferred to `stack_out` (1 operation)

    Counter for requests in the last 3000ms.3. Popped from `stack_out` (1 operation)

    Uses deque for efficient sliding time window.

    """**Total**: 3 operations per element across its lifetime → **Amortized O(1)**



    def __init__(self):---

        # Use a deque as a fast FIFO queue

        self.tickets = deque()## 🎨 Pattern 2: Sliding Time Window — "Number of Recent Calls"



    def ping(self, t: int) -> int:### 💡 Core Idea (The "Ticket Window" Pattern)

        """

        Record a new request at time t and return count of requests**Problem**: Count pings in the time range `[t - 3000, t]`.

        in the range [t-3000, t].

        **Naive Approach** (O(N) Trap): Using a list

        Args:```python

            t: Current timestamp in millisecondsself.pings.append(t)  # O(1)

            for p in self.pings:  # O(N) - scans all pings every time!

        Returns:    if t - 3000 <= p <= t:

            Number of requests in the last 3000ms        count += 1

        """```

        # 1. Add the new "ticket" to the back- Re-scans all 1 million old pings every call → **Time Limit Exceeded**

        self.tickets.append(t)

        **Optimal Solution** (O(1) Amortized): This is a FIFO problem!

        # 2. Find the "cutoff" time- New pings (t) added to **BACK**

        cutoff = t - 3000- Old expired pings removed from **FRONT**

        - Perfect tool: **`deque`**

        # 3. Clean all old tickets from the front

        while self.tickets and self.tickets[0] < cutoff:### 🧠 The 4-Step Logic

            self.tickets.popleft()

        For every `ping(t)`:

        # 4. The size of the deque *is* the answer

        return len(self.tickets)1. **Add New "Ticket"** (to BACK): `self.tickets.append(t)`

2. **Find "Cutoff"**: `cutoff = t - 3000`

3. **Clean "Old Tickets"** (from FRONT):

# Test   ```python

if __name__ == '__main__':   while self.tickets and self.tickets[0] < cutoff:

    counter = RecentCounter()       self.tickets.popleft()

    print(counter.ping(1))     # 1 (requests: [1])   ```

    print(counter.ping(100))   # 2 (requests: [1, 100])4. **Return Count**: After cleaning, all tickets in deque are valid

    print(counter.ping(3001))  # 3 (requests: [1, 100, 3001])   ```python

    print(counter.ping(3002))  # 3 (requests: [100, 3001, 3002])   return len(self.tickets)

                               # 1 is expired (< 3002-3000=2)   ```

```

### 📝 Implementation (LeetCode 933)

### ⏱️ Complexity

```python

- **Time**: **Amortized O(1)**from collections import deque

  - Every ping is `append()`ed once and `popleft()`ed at most once

  - Average cost per operation is constantclass RecentCounter:

- **Space**: **O(W)** where W = window size (3000ms)    """

  - Deque size limited by window, not total requests    Counter for requests in the last 3000ms.

  - Even with 1 million pings, max size ≈ 3000 items    Uses deque for efficient sliding time window.

    """

### 🎯 Visual Trace

    def __init__(self):

```        # Use a deque as a fast FIFO queue

Window = 3000ms        self.tickets = deque()



ping(1):    def ping(self, t: int) -> int:

  tickets = [1]        """

  cutoff = 1 - 3000 = -2999        Record a new request at time t and return count of requests

  No cleanup needed        in the range [t-3000, t].

  return 1        

        Args:

ping(100):            t: Current timestamp in milliseconds

  tickets = [1, 100]            

  cutoff = 100 - 3000 = -2900        Returns:

  No cleanup needed            Number of requests in the last 3000ms

  return 2        """

        # 1. Add the new "ticket" to the back

ping(3001):        self.tickets.append(t)

  tickets = [1, 100, 3001]        

  cutoff = 3001 - 3000 = 1        # 2. Find the "cutoff" time

  Cleanup: 1 >= 1, keep it        cutoff = t - 3000

  return 3        

        # 3. Clean all old tickets from the front

ping(3002):        while self.tickets and self.tickets[0] < cutoff:

  tickets = [1, 100, 3001, 3002]            self.tickets.popleft()

  cutoff = 3002 - 3000 = 2        

  Cleanup: 1 < 2, remove it        # 4. The size of the deque *is* the answer

  tickets = [100, 3001, 3002]        return len(self.tickets)

  return 3



ping(6500):# Test

  tickets = [100, 3001, 3002, 6500]if __name__ == '__main__':

  cutoff = 6500 - 3000 = 3500    counter = RecentCounter()

  Cleanup: 100 < 3500, remove    print(counter.ping(1))     # 1 (requests: [1])

           3001 < 3500, remove    print(counter.ping(100))   # 2 (requests: [1, 100])

           3002 < 3500, remove    print(counter.ping(3001))  # 3 (requests: [1, 100, 3001])

  tickets = [6500]    print(counter.ping(3002))  # 3 (requests: [100, 3001, 3002])

  return 1                               # 1 is expired (< 3002-3000=2)

``````



### 🔑 Why Deque is Perfect### ⏱️ Complexity



| Operation | List | Deque |- **Time**: **Amortized O(1)**

|-----------|------|-------|  - Every ping is `append()`ed once and `popleft()`ed at most once

| Add to back | O(1) | O(1) |  - Average cost per operation is constant

| Remove from front | O(N) ❌ | O(1) ✅ |- **Space**: **O(W)** where W = window size (3000ms)

| Memory | Contiguous | Efficient chunks |  - Deque size limited by window, not total requests

  - Even with 1 million pings, max size ≈ 3000 items

For sliding windows, **always use deque** for O(1) removals from front.

### 🎯 Visual Trace

---

```

## 🎓 Interview TipsWindow = 3000ms



1. **Two-Stack Queue Pattern**:ping(1):

   - Use lazy transfer (only when `stack_out` is empty)  tickets = [1]

   - Remember: queue empty = **both** stacks empty  cutoff = 1 - 3000 = -2999

   - Amortized analysis: each element moved at most once  No cleanup needed

  return 1

2. **Sliding Time Window Pattern**:

   - Use `deque` for FIFO with efficient front removalping(100):

   - Add new items to back, remove expired from front  tickets = [1, 100]

   - Window size limits space (not total elements)  cutoff = 100 - 3000 = -2900

  No cleanup needed

3. **Common Mistakes**:  return 2

   - Using list for sliding window (O(N) `list.pop(0)`)

   - Transferring on every pop (should be lazy)ping(3001):

   - Forgetting to check both stacks for empty queue  tickets = [1, 100, 3001]

  cutoff = 3001 - 3000 = 1

4. **Amortized O(1) Explained**:  Cleanup: 1 >= 1, keep it

   - Individual operation might be O(N)  return 3

   - But averaged over many operations = O(1)

   - Each element processed constant times totalping(3002):

  tickets = [1, 100, 3001, 3002]

---  cutoff = 3002 - 3000 = 2

  Cleanup: 1 < 2, remove it

## 📝 Practice Problems  tickets = [100, 3001, 3002]

  return 3

| Problem | Difficulty | Pattern | Link |

|---------|-----------|---------|------|ping(6500):

| Implement Queue using Stacks | Easy | Two-Stack Queue | [LeetCode 232](https://leetcode.com/problems/implement-queue-using-stacks/) |  tickets = [100, 3001, 3002, 6500]

| Number of Recent Calls | Easy | Sliding Time Window | [LeetCode 933](https://leetcode.com/problems/number-of-recent-calls/) |  cutoff = 6500 - 3000 = 3500

| Implement Stack using Queues | Easy | Two-Queue Stack | [LeetCode 225](https://leetcode.com/problems/implement-stack-using-queues/) |  Cleanup: 100 < 3500, remove

| Moving Average from Data Stream | Easy | Sliding Window | [LeetCode 346](https://leetcode.com/problems/moving-average-from-data-stream/) |           3001 < 3500, remove

           3002 < 3500, remove

---  tickets = [6500]

  return 1

## 🚀 Run the Code```



Save and test the implementations:### 🔑 Why Deque is Perfect



```bash| Operation | List | Deque |

# Test Two-Stack Queue|-----------|------|-------|

python day-40-queue-using-stacks.py| Add to back | O(1) | O(1) |

| Remove from front | O(N) ❌ | O(1) ✅ |

# Test Sliding Time Window| Memory | Contiguous | Efficient chunks |

python day-40-recent-counter.py

```For sliding windows, **always use deque** for O(1) removals from front.



Or test interactively:---



```python## 🎓 Interview Tips

python -i day-40-queue-using-stacks.py

>>> q = MyQueue()1. **Two-Stack Queue Pattern**:

>>> q.push(1)   - Use lazy transfer (only when `stack_out` is empty)

>>> q.push(2)   - Remember: queue empty = **both** stacks empty

>>> q.pop()   - Amortized analysis: each element moved at most once

1

```2. **Sliding Time Window Pattern**:

   - Use `deque` for FIFO with efficient front removal

---   - Add new items to back, remove expired from front

   - Window size limits space (not total elements)

**Made with ❤️ for interview prep**

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
