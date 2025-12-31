# Day 44 — Fibonacci: Brute Force to Optimal

**Topic**: Recursion & Memoization (Dynamic Programming Introduction)

---

## 📚 Overview

Today we solve the **Fibonacci problem** using three approaches:
1. 🐢 **Brute Force** — Naive recursion (exponential time)
2. 🚀 **Memoization** — Top-Down DP (linear time)
3. ⚡ **Iterative** — Bottom-Up DP (linear time, constant space)

---

## 🎯 The Fibonacci Sequence

**Definition**: `fib(n) = fib(n-1) + fib(n-2)`

**Sequence**: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34...`

**Base Cases**:
- `fib(0) = 0`
- `fib(1) = 1`

---

## 🐢 Solution 1: Brute Force (The "Naive Recursion" Trap)

This is the "obvious" solution — just translate the math rule directly into code.

### 💡 The Problem: Overlapping Subproblems

This solution is a **"chutiyapaa" trap**. It's simple, but **disastrously slow**.

**Why?** Because we recalculate the same values over and over!

### 🌳 Recursion Tree for `fib(5)`

```
                    fib(5)
                   /      \
              fib(4)      fib(3)
             /     \      /     \
        fib(3)   fib(2) fib(2) fib(1)
        /    \    /   \  /   \
    fib(2) fib(1) f(1) f(0) f(1) f(0)
    /   \
 fib(1) fib(0)

🔴 REDUNDANT CALCULATIONS:
   - fib(3) calculated 2 times
   - fib(2) calculated 3 times
   - fib(1) calculated 5 times
   - fib(0) calculated 3 times

Total function calls: 15 calls for just fib(5)! 💀
```

### 📊 Call Count Explosion

| n | Function Calls |
|---|----------------|
| 5 | 15 |
| 10 | 177 |
| 20 | 21,891 |
| 30 | 2,692,537 |
| 40 | 331,160,281 |

**Result**: O(2ⁿ) exponential growth! ❌

---

### 📝 Pseudocode

```
Function fib_brute_force(n):
    // 1. Base Cases (The "Intern")
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    // 2. Recursive Case (The "Delegation")
    // ⚠️ This is the slow part - recalculates everything!
    return fib_brute_force(n - 1) + fib_brute_force(n - 2)
```

---

### 💻 Python Implementation

```python
class Solution:
    def fib_brute_force(self, n: int) -> int:
        """
        Brute force recursive Fibonacci.
        WARNING: Exponential time complexity!
        """
        # 1. Base Cases
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        # 2. Recursive Case (The "chutiyapaa" part)
        # This will be recalculated millions of times
        return self.fib_brute_force(n - 1) + self.fib_brute_force(n - 2)
```

---

### ⏱️ Complexity Analysis

- **Time**: **O(2ⁿ)** (Exponential) 💀
  - The recursion tree roughly doubles in size for every n
  - For `fib(40)`, you'll wait forever!
  - **Time Limit Exceeded** on LeetCode

- **Space**: **O(N)** (Linear)
  - Call stack depth is N (e.g., `fib(5) → fib(4) → fib(3) → fib(2) → fib(1)`)
  - Each recursive call uses one stack frame

---## 🚀 Solution 2: Memoization (The "Cache" Fix)

This is the **main lesson** of today! We fix the "Overlapping Subproblems" by **caching** our answers.

**Also called**: "Top-Down Dynamic Programming"

---

### 💡 The Aha Moment: Trade Space for Time

We create a `memo = {}` (dictionary/hash map) to store results:
- **First call** to `fib(n)`: Do the hard work, save result
- **Second call** to `fib(n)`: Return saved result instantly (O(1))

This **"prunes"** (cuts off) all duplicate branches from our tree!

---

### 🌳 Before Memoization: `fib(5)` (15 calls)

```
                    fib(5)
                   /      \
              fib(4)      fib(3)  ← fib(3) called AGAIN!
             /     \      /     \
        fib(3)   fib(2) fib(2) fib(1)
        /    \    /   \  /   \
    fib(2) fib(1) f(1) f(0) f(1) f(0)
    /   \
 fib(1) fib(0)

❌ WASTEFUL: 15 function calls
```

### 🌳 After Memoization: `fib(5)` (9 calls)

```
                    fib(5)
                   /      \
              fib(4)      fib(3) ✅ CACHED! (returns instantly)
             /     \
        fib(3)   fib(2) ✅ CACHED!
        /    \
    fib(2) fib(1) ✅ CACHED!
    /   \
 fib(1) fib(0)

✅ OPTIMIZED: Only 9 function calls!
   Each value calculated ONCE, then reused.

Memo contents after fib(5):
{
  0: 0,
  1: 1,
  2: 1,
  3: 2,
  4: 3,
  5: 5
}
```

### 📊 Performance Comparison

| n | Brute Force Calls | Memoization Calls | Speedup |
|---|-------------------|-------------------|----------|
| 5 | 15 | 9 | 1.7x |
| 10 | 177 | 19 | 9.3x |
| 20 | 21,891 | 39 | 561x |
| 30 | 2,692,537 | 59 | 45,636x |
| 40 | 331,160,281 | 79 | 4,191,649x 🚀 |

---

### 📝 Pseudocode

```
// 1. Create a "memo pad" (a hash map)
memo = {}

Function fib_better(n):
    // 2. Check the memo FIRST! (Most important step)
    if n in memo:
        return memo[n]  ← O(1) instant return!
        
    // 3. Check Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    // 4. Do the hard work (only happens ONCE per n)
    result = fib_better(n - 1) + fib_better(n - 2)
    
    // 5. SAVE the result before returning
    memo[n] = result
    return result
```

---

### 💻 Python Implementation

```python
class Solution:
    def __init__(self):
        # Create the 'memo' (our cache) for the instance
        self.memo = {}
    
    def fib_better(self, n: int) -> int:
        """
        Memoized (Top-Down DP) Fibonacci.
        Time: O(N), Space: O(N)
        """
        # 1. Check the memo FIRST!
        if n in self.memo:
            return self.memo[n]  # ✅ Instant return!
            
        # 2. Base Cases
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        # 3. Do the hard work (only happens once per n)
        result = self.fib_better(n - 1) + self.fib_better(n - 2)
        
        # 4. SAVE the result
        self.memo[n] = result
        return result
```

**Alternative with `@lru_cache` decorator**:

```python
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)  # Python does memoization for us!
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

---

### ⏱️ Complexity Analysis

- **Time**: **O(N)** (Linear) 🚀
  - We calculate `fib(i)` **exactly once** for each i from 0 to n
  - All duplicate calls are O(1) dictionary lookups
  - Total: N calculations + N lookups ≈ O(2N) → O(N)

- **Space**: **O(N)** (Linear)
  - **Call Stack**: O(N) — maximum depth is still N
  - **Memo Dictionary**: O(N) — stores N key-value pairs
  - Total: O(N) + O(N) = O(2N) → O(N)

---## ⚡ Solution 3: Iterative (The "Optimal" Solution)

This is the **true optimal solution**! It achieves **O(N) time** but fixes the **O(N) space** problem.

**Also called**: "Bottom-Up Dynamic Programming"

---

### 💡 The Key Insight: Why Use Recursion at All?

We know:
- `fib(5)` needs `fib(4)` and `fib(3)`
- `fib(4)` needs `fib(3)` and `fib(2)`
- `fib(3)` needs `fib(2)` and `fib(1)`

**Observation**: We can calculate from **bottom-up** instead of **top-down**!

---

### 🔄 Approach Comparison

| Approach | Direction | Method | Stack Frames |
|----------|-----------|--------|-------------|
| Brute Force | Top-Down | Recursion | O(N) |
| Memoization | Top-Down | Recursion + Cache | O(N) |
| **Iterative** | **Bottom-Up** | **Loop** | **O(1)** ✅ |

---

### 🌳 Before Iterative: Top-Down Thinking

```
To calculate fib(5), we think:

    fib(5) = ?
       ↓
   needs fib(4) and fib(3)
       ↓
   fib(4) = ?
       ↓
   needs fib(3) and fib(2)
       ↓
   fib(3) = ?
   ...

❌ Requires recursion (call stack)
❌ Requires memoization (dictionary)
```

### 🌳 After Iterative: Bottom-Up Building

```
We already know the base:
  fib(0) = 0
  fib(1) = 1

Now just BUILD UP using a loop:

Step 1:  a=0, b=1  → fib(2) = 0+1 = 1
Step 2:  a=1, b=1  → fib(3) = 1+1 = 2
Step 3:  a=1, b=2  → fib(4) = 1+2 = 3
Step 4:  a=2, b=3  → fib(5) = 2+3 = 5 ✅

✅ No recursion needed!
✅ No memo dictionary needed!
✅ Just 2 variables (a, b) sliding forward!
```

### 🎯 Visual: The "Sliding Window" Technique

```
Calculating fib(6):

i=0:  [0, 1, _, _, _, _, _]
       ↑  ↑
       a  b

i=2:  [0, 1, 1, _, _, _, _]  ← 0+1=1
          ↑  ↑
          a  b (slid right!)

i=3:  [0, 1, 1, 2, _, _, _]  ← 1+1=2
             ↑  ↑
             a  b (slid right!)

i=4:  [0, 1, 1, 2, 3, _, _]  ← 1+2=3
                ↑  ↑
                a  b

i=5:  [0, 1, 1, 2, 3, 5, _]  ← 2+3=5
                   ↑  ↑
                   a  b

i=6:  [0, 1, 1, 2, 3, 5, 8]  ← 3+5=8
                      ↑  ↑
                      a  b (answer!)

Only need 'a' and 'b' — no array needed!
```

---

### 📝 Pseudocode

```
Function fib_optimal(n):
    // Handle base cases
    if n == 0: return 0
    if n == 1: return 1
    
    // 1. Initialize our two starting numbers
    a = 0  // This represents fib(i-2)
    b = 1  // This represents fib(i-1)
    
    // 2. Loop from 2 up to n
    for i from 2 to n:
        // 3. Calculate the next fib number
        current_fib = a + b
        
        // 4. "Slide" our variables one step to the right
        a = b
        b = current_fib
        
    // 5. After the loop, 'b' holds the final answer
    return b
```

---

### 💻 Python Implementation

```python
class Solution:
    def fib_optimal(self, n: int) -> int:
        """
        Iterative (Bottom-Up DP) Fibonacci.
        Time: O(N), Space: O(1) ✅ OPTIMAL!
        """
        # 1. Base Cases
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        # 2. Initialize our two "bottom-up" variables
        a = 0  # This is fib(0)
        b = 1  # This is fib(1)
        
        # 3. Loop from 2 up to and including n
        for i in range(2, n + 1):
            # 4. Calculate the next fib number
            current_fib = a + b
            
            # 5. "Slide" our variables
            a = b
            b = current_fib
            
        # 6. 'b' now holds the N-th fib number
        return b
```

**Even more concise with Python tuple unpacking**:

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b  # Pythonic "slide" in one line!
        
        return b
```

---

### ⏱️ Complexity Analysis

- **Time**: **O(N)** (Linear) 🚀
  - Single `for` loop that runs N times
  - Each iteration does O(1) work (addition and assignment)
  - Total: O(N)

- **Space**: **O(1)** (Constant) ⭐ **THE BIG WIN!**
  - Only 3 variables (`a`, `b`, `current_fib`) — constant space!
  - No call stack (no recursion)
  - No memo dictionary
  - Space usage doesn't grow with N

---

## 📊 Final Comparison: All Three Solutions

| Solution | Time | Space | Method | Best For |
|----------|------|-------|--------|----------|
| **Brute Force** | O(2ⁿ) 💀 | O(N) | Recursion | Never use! |
| **Memoization** | O(N) 🚀 | O(N) | Top-Down DP | Interview explanation |
| **Iterative** | O(N) 🚀 | **O(1)** ⭐ | Bottom-Up DP | Production code |

---

## 🎓 Self-Test Questions

### Question 1
**Why is the "naive" solution (Brute Force) so slow?**

<details>
<summary>Click for answer</summary>

Because of **overlapping subproblems**. The same Fibonacci numbers are calculated multiple times:
- `fib(3)` calculated 2 times
- `fib(2)` calculated 3 times
- `fib(1)` calculated 5 times

This creates an exponential O(2ⁿ) time complexity.
</details>

### Question 2
**What is "Memoization"? What tool do we use?**

<details>
<summary>Click for answer</summary>

**Memoization** is a technique where we **cache** (save) the results of expensive function calls and return the cached result when the same inputs occur again.

**Tool**: We use a **dictionary (hash map)** to store `{n: result}` pairs.

This turns overlapping subproblems into O(1) lookups!
</details>

### Question 3
**In our memoized function, what is the VERY FIRST thing we do?**

<details>
<summary>Click for answer</summary>

**Check the memo FIRST!**

```python
if n in self.memo:
    return self.memo[n]  # Instant return!
```

This is the most important step — it prevents recalculation by returning cached results immediately.
</details>

---

## 🔑 Key Takeaways

1. **Brute Force** = O(2ⁿ) exponential disaster
2. **Memoization** = Trade space for time (O(N) both)
3. **Iterative** = Best of both worlds (O(N) time, O(1) space)
4. **Always check memo first** when using memoization
5. **Bottom-up eliminates recursion overhead** for optimal space

---

