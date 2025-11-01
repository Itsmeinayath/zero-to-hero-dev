# Day 39 — Stack Applications

**Date**: November 1, 2025  
**Topic**: Stacks & Queues (Stack Applications)

## 📚 Purpose

Today is about moving from basic stack theory to solving complex problems using specific stack patterns:
- **Pattern 1**: Monotonic Stack (Next Greater Element)
- **Pattern 2**: Two-Stack Design (Min Stack with O(1) operations)

---

## 🎯 TL;DR

**Monotonic Stack**: A stack kept in (usually) decreasing order — the key pattern for all "Next Greater Element" problems. The "sister" pattern to Monotonic Deque.

**Two-Stack Design**: Classic design problem using `main_stack` for data and `min_stack` to track current minimum, enabling O(1) `getMin()`.

**Key Insight**: Avoid nested loops O(N²) or `min()` function O(N). Correct patterns are always **O(N)** or **O(1)**.

---

## 🎨 Pattern 1: Monotonic Stack — "Next Greater Element I"

### 💡 Core Idea ("The Line of Waiters")

**Goal**: Find the first number to the right of an element that is greater.

**Brute-Force** (O(M × N) Trap): Triple nested loops — too slow.

**Optimal** (O(M + N) Solution): Find "next greater element" for every number in `nums2` in one pass.

### 🛠️ The Two Tools

1. **`stack`** (list): Holds "waiters" — numbers waiting for their next greater element
2. **`answers_map`** (dict): Stores `{waiter: answer}` pairs

### 🧠 The 3 Rules (For each `num` in `nums2`)

#### Rule 1: Process "Waiters" (from TOP)

**Logic**: If the new `num` is bigger than the "waiter" on top, that waiter found its answer.

```python
while stack and num > stack[-1]:
    waiter = stack.pop()
    answers_map[waiter] = num
```

#### Rule 2: Add New "Waiter" (to TOP)

**Logic**: After processing smaller waiters, the new `num` is now also a waiter.

```python
stack.append(num)
```

#### Rule 3: Handle Leftovers (After Loop)

**Logic**: Any "waiter" still in the stack never found an answer.

```python
while stack:
    answers_map[stack.pop()] = -1
```

### 📝 Implementation (LeetCode 496)

```python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find next greater element for each number in nums1 from nums2.
        
        Args:
            nums1: Query array (subset of nums2)
            nums2: Full array to search in
            
        Returns:
            List where result[i] is the next greater element for nums1[i]
        """
        # 1. Setup our tools
        stack = []         # For "waiters"
        answers_map = {}   # For "waiter: answer" pairs

        # 2. Loop through nums2 to fill the map
        for num in nums2:
            # Rule 1: Process waiters
            while stack and num > stack[-1]:
                waiter = stack.pop()
                answers_map[waiter] = num
            
            # Rule 2: Add new waiter
            stack.append(num)

        # 3. Handle leftovers
        while stack:
            waiter = stack.pop()
            answers_map[waiter] = -1
            
        # 4. Build the final result from nums1
        result_list = []
        for num in nums1:
            result_list.append(answers_map[num])
            
        return result_list


# Test
if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
    # Output: [-1, 3, -1]
    # Explanation: 
    # - 4: no greater element → -1
    # - 1: next greater is 3
    # - 2: no greater element → -1
```

### ⏱️ Complexity

- **Time**: O(M + N)
  - O(N) to build the map (each element pushed/popped once — amortized)
  - O(M) to build the result array
- **Space**: O(N) for `answers_map` and `stack`

### 🎯 Visual Trace

```
nums2 = [1, 3, 4, 2]

Step 1: num=1
  stack=[] → append(1) → stack=[1]

Step 2: num=3
  3 > 1 → pop 1, answers_map[1]=3
  stack=[] → append(3) → stack=[3]

Step 3: num=4
  4 > 3 → pop 3, answers_map[3]=4
  stack=[] → append(4) → stack=[4]

Step 4: num=2
  2 < 4 → just append(2) → stack=[4,2]

Leftovers: stack=[4,2]
  answers_map[4]=-1, answers_map[2]=-1

Final map: {1:3, 3:4, 4:-1, 2:-1}
```

---

## 🎨 Pattern 2: Two-Stack Design — "Min Stack"

### 💡 Core Idea (O(1) getMin)

**Design Problem**: Build a stack where `push`, `pop`, `top`, AND `getMin` are all **O(1)**.

**Brute-Force** (O(N) Trap): Using `min(self.data)` for `getMin()` — too slow.

**Optimal** (O(1) Solution): Always know the minimum using **two stacks**.

### �️ The Two Stacks

1. **`main_stack`**: Holds all the numbers
2. **`min_stack`**: Helper stack where `min_stack[-1]` is always the current minimum of `main_stack`

### 🧠 The 3 Rules (Core Logic)

#### Rule 1: `push(val)`

- **Always** `main_stack.append(val)`
- **Only** `min_stack.append(val)` if:
  - `min_stack` is empty (`if not self.min_stack...`)
  - **OR** `val <= min_stack[-1]` (new min or duplicate min)

> ⚠️ **Critical**: Use `<=` not `<` to handle duplicate minimums!

#### Rule 2: `pop()`

- `item = main_stack.pop()`
- **Only** `min_stack.pop()` if:
  - The `item` we just popped equals the current minimum (`if item == min_stack[-1]`)

#### Rule 3: `getMin()`

- Easy part: `return min_stack[-1]`

### 📝 Implementation (LeetCode 155)

```python
class MinStack:
    """
    Stack with O(1) push, pop, top, and getMin operations.
    """

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """Push element onto stack."""
        self.main_stack.append(val)
        
        # This is the most important line in the class
        # Handles empty case AND new-min/duplicate-min case
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Remove top element from stack."""
        # Check if main_stack is empty to prevent crashes
        if self.main_stack:
            item = self.main_stack.pop()
            
            # Keep the stacks in sync
            # Check if min_stack is not empty AND item was the min
            if self.min_stack and item == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """Get the top element without removing."""
        if self.main_stack:
            return self.main_stack[-1]
        return None  # Or raise an error

    def getMin(self) -> int:
        """Retrieve the minimum element in O(1)."""
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Or raise an error


# Test
if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())  # -3
    stack.pop()
    print(stack.top())     # 0
    print(stack.getMin())  # -2
```

### ⏱️ Complexity

- **Time**: O(1) for all operations (`push`, `pop`, `top`, `getMin`)
- **Space**: O(N)
  - `main_stack` takes O(N)
  - `min_stack` in worst case `[5, 4, 3, 2, 1]` also takes O(N)

### 🎯 Visual Trace

```
Operation Sequence:
push(-2) → main=[−2], min=[−2]
push(0)  → main=[−2,0], min=[−2]      (0 > -2, don't push to min)
push(-3) → main=[−2,0,−3], min=[−2,−3] (−3 < -2, push to min)
getMin() → return -3                   (min_stack[-1])
pop()    → main=[−2,0], min=[−2]       (popped -3, also pop from min)
top()    → return 0                    (main_stack[-1])
getMin() → return -2                   (min_stack[-1])
```

### 🔑 Why `<=` is Critical

Consider this sequence: `push(1), push(1), pop()`

- **With `<=`**: `min_stack = [1, 1]` → After pop: `min_stack = [1]` ✅
- **With `<`**: `min_stack = [1]` → After pop: `min_stack = []` ❌ (Lost minimum!)

---

---

## 🎓 Interview Tips

1. **Monotonic Stack**: For "Next Greater/Smaller" problems
   - Stack holds "waiters"
   - Map/dict stores answers
   - Process from top to bottom

2. **Two-Stack Design**: For "Get-Min/Max in O(1)" problems
   - Key is the push logic: `val <= min_stack[-1]`
   - The `<=` (not `<`) is critical for duplicate minimums
   - Keep stacks synchronized on pop

3. **Safety First**: Always check empty before operations
   - `if stack:` before `pop()` or `stack[-1]`
   - Prevents `IndexError` crashes

4. **Common Mistakes**:
   - Forgetting to handle duplicate minimums (`<=` vs `<`)
   - Not syncing both stacks in pop operation
   - Not checking for empty stack before peek/pop

---

## 📝 Practice Problems

| Problem | Difficulty | Pattern | Link |
|---------|-----------|---------|------|
| Next Greater Element I | Easy | Monotonic Stack | [LeetCode 496](https://leetcode.com/problems/next-greater-element-i/) |
| Next Greater Element II | Medium | Monotonic Stack | [LeetCode 503](https://leetcode.com/problems/next-greater-element-ii/) |
| Min Stack | Medium | Two-Stack Design | [LeetCode 155](https://leetcode.com/problems/min-stack/) |
| Daily Temperatures | Medium | Monotonic Stack | [LeetCode 739](https://leetcode.com/problems/daily-temperatures/) |
| Largest Rectangle in Histogram | Hard | Monotonic Stack | [LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

---

## 🚀 Run the Code

Save either implementation and test:

```bash
# For Next Greater Element
python day-39-monotonic-stack.py

# For Min Stack
python day-39-min-stack.py
```

Or test interactively:

```python
python -i day-39-min-stack.py
>>> stack = MinStack()
>>> stack.push(5)
>>> stack.push(3)
>>> stack.getMin()
3
```

---

**Made with ❤️ for interview prep**
