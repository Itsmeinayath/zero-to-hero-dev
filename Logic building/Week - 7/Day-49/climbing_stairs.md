# 🪜 Climbing Stairs - LeetCode Problem 70

## 📋 Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb **1 step** or **2 steps**. In how many distinct ways can you climb to the top?

### Examples

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

---

## 💡 Core Pattern: Dynamic Programming

### The Key Insight

At any step `n`, you can only arrive from:
- Step `n-1` (taking 1 step)
- Step `n-2` (taking 2 steps)

Therefore: **Ways(n) = Ways(n-1) + Ways(n-2)**

This is the **Fibonacci sequence**! 🎯

---

## 🛠️ Solution Approaches

### 1️⃣ Naive Recursion (❌ Inefficient)

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    return climbStairs(n-1) + climbStairs(n-2)
```

- **Time Complexity**: O(2^n) - exponential!
- **Space Complexity**: O(n) - recursion stack
- **Problem**: Massive duplicate calculations

---

### 2️⃣ Memoization (✅ Better)

```python
def climbStairs(n: int) -> int:
    memo = {}
    
    def helper(n):
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = helper(n-1) + helper(n-2)
        return memo[n]
    
    return helper(n)
```

- **Time Complexity**: O(n)
- **Space Complexity**: O(n) - memo dictionary + recursion stack
- **Improvement**: Each step calculated only once

---

### 3️⃣ Iterative with Two Variables (⭐ Optimal)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one 
            one = one + two 
            two = temp
        return one
```

**Alternative Clean Version:**
```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1
```

- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - only two variables!
- **Why Optimal**: We only need the last two values to compute the next

---

## 🔍 Step-by-Step Walkthrough (n=5)

| Step | one | two | Calculation |
|------|-----|-----|-------------|
| Init | 1   | 1   | -           |
| i=0  | 2   | 1   | one=1+1     |
| i=1  | 3   | 2   | one=2+1     |
| i=2  | 5   | 3   | one=3+2     |
| i=3  | 8   | 5   | one=5+3     |

**Result**: 8 ways to climb 5 stairs

---

## 🧠 Why This Works

The pattern emerges from the **Principle of Optimality**:
- To reach step `n`, you **must** have been at `n-1` or `n-2`
- Total ways = Sum of ways to reach those previous states
- We build the solution from bottom-up

---

## 📊 Complexity Comparison

| Approach     | Time    | Space | Notes                    |
|--------------|---------|-------|--------------------------|
| Recursion    | O(2^n)  | O(n)  | Too slow for large n     |
| Memoization  | O(n)    | O(n)  | Good balance             |
| Iterative    | O(n)    | O(1)  | ⭐ **Best solution**     |

---

## 🎓 Key Takeaways

1. **Recognize the pattern**: Many DP problems boil down to "how many ways to reach state N?"
2. **Work backwards**: Think about the last move that got you to the target
3. **Optimize space**: Often you don't need to store all previous results
4. **Fibonacci in disguise**: This problem IS the Fibonacci sequence!

---

## 🔗 Related Problems

- Fibonacci Number (LeetCode 509)
- Min Cost Climbing Stairs (LeetCode 746)
- House Robber (LeetCode 198)
- Decode Ways (LeetCode 91)

---

## 💻 Implementation Notes

### Your Current Solution
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one 
            one = one + two 
            two = temp
        return one
```

**Analysis:**
- ✅ O(1) space complexity
- ✅ O(n) time complexity
- ✅ Handles edge cases (n=1 returns 1)
- 💡 Could use tuple unpacking for cleaner code: `one, two = one + two, one`

---

**Date**: Day 49 | Week 7  
**Topic**: Dynamic Programming  
**Difficulty**: Easy  
**Status**: ✅ Solved
