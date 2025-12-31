# Day 48 — Recursion Recap & DP Bridge 🌉

**Date**: November 21, 2025  
**Topic**: Backtracking & Memoization

---

## 📚 Overview

Today we covered **two important patterns**:

1. **Backtracking** - Generate all possibilities (Letter Combinations)
2. **Dynamic Programming** - Optimize recursion with storage (Subset Sum)

---

## 🎯 TL;DR - Pattern Comparison

| Pattern | Problem | Goal | Approach |
|---------|---------|------|----------|
| **Backtracking** | Letter Combinations | Generate ALL outputs | DFS branching |
| **DP** | Subset Sum | Answer YES/NO question | Memoization/Tabulation |

---

## 🎨 Pattern 1: Letter Combinations (LeetCode 17)

**The Task**: Given a phone number, generate all possible letter combinations.

### Phone Keypad Mapping

```
┌─────┬─────┬─────┐
│  1  │  2  │  3  │
│     │ abc │ def │
├─────┼─────┼─────┤
│  4  │  5  │  6  │
│ ghi │ jkl │ mno │
├─────┼─────┼─────┤
│  7  │  8  │  9  │
│pqrs │ tuv │wxyz │
├─────┼─────┼─────┤
│  *  │  0  │  #  │
└─────┴─────┴─────┘
```

---

### 🌳 Visual: Decision Tree for "23"

```
Input: digits = "23"
Mapping: 2 → "abc", 3 → "def"

                    ""
                   /|\
                  / | \
                 /  |  \
                a   b   c      ← First digit (2)
               /|\  /|\  /|\
              d e f d e f d e f  ← Second digit (3)
              |   |   |   |   |
             ad ae af bd be bf cd ce cf  ← RESULTS!

✅ 9 combinations = 3 × 3 = 3²
```

---

### 🔍 Step-by-Step Trace: digits = "23"

```
backtrack(0, "")
├─ char='a': backtrack(1, "a")
│  ├─ char='d': backtrack(2, "ad") → SAVE "ad" ✅
│  ├─ char='e': backtrack(2, "ae") → SAVE "ae" ✅
│  └─ char='f': backtrack(2, "af") → SAVE "af" ✅
│
├─ char='b': backtrack(1, "b")
│  ├─ char='d': backtrack(2, "bd") → SAVE "bd" ✅
│  ├─ char='e': backtrack(2, "be") → SAVE "be" ✅
│  └─ char='f': backtrack(2, "bf") → SAVE "bf" ✅
│
└─ char='c': backtrack(1, "c")
   ├─ char='d': backtrack(2, "cd") → SAVE "cd" ✅
   ├─ char='e': backtrack(2, "ce") → SAVE "ce" ✅
   └─ char='f': backtrack(2, "cf") → SAVE "cf" ✅

Result: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

### 📝 Implementation

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Phone keypad mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        
        def backtrack(i, cur_str):
            # Base Case: Built complete string
            if i == len(digits):
                result.append(cur_str)
                return
            
            # Try each letter for current digit
            for char in phone_map[digits[i]]:
                # No explicit "unchoose" needed - string is immutable!
                backtrack(i + 1, cur_str + char)
        
        backtrack(0, "")
        return result
```

**Key Points**:
- ✅ No explicit UNCHOOSE (strings are immutable in Python)
- ✅ Each digit branches to 3-4 letters
- ✅ Base case: when index equals digits length

---

### ⏱️ Complexity

- **Time**: **O(4ⁿ × N)**
  - Each digit has up to 4 letters (7, 9)
  - N digits → 4^N combinations
  - Each combination takes O(N) to build
  - Total: O(4ⁿ × N)

- **Space**: **O(N)**
  - Recursion depth = N
  - (Not counting output)

---

## 🎨 Pattern 2: Subset Sum (GeeksforGeeks)

**The Task**: Can we pick a subset that sums to target?

### Problem Statement

```
Input: arr = [3, 34, 4, 12, 5, 2], target = 9
Output: True (3 + 4 + 2 = 9 or 4 + 5 = 9)
```

---

### 💡 The Three Approaches

| Approach | Time | Space | Method |
|----------|------|-------|--------|
| **Brute Force** | O(2ⁿ) 💀 | O(N) | Try all subsets |
| **Memoization** | O(N × T) ✅ | O(N × T) | Cache (index, target) |
| **Tabulation** | O(N × T) ✅ | O(N × T) | Build DP table |

Where N = array length, T = target value

---

### 🌳 Visual: Decision Tree for arr=[3,4,2], target=5

```
                    (i=0, t=5)
                    "Can we make 5?"
                   /              \
            Include 3           Exclude 3
               ↓                    ↓
          (i=1, t=2)            (i=1, t=5)
         "Make 2?"              "Make 5?"
         /       \              /       \
    Inc 4      Exc 4       Inc 4      Exc 4
      ↓          ↓           ↓          ↓
  (i=2,t=-2) (i=2,t=2)   (i=2,t=1)  (i=2,t=5)
     ❌       "Make 2?"   "Make 1?"  "Make 5?"
  (negative)  /     \     /     \    /     \
           Inc 2  Exc 2 Inc 2 Exc 2 Inc 2  Exc 2
             ↓      ↓     ↓     ↓     ↓      ↓
          t=0 ✅  t=2❌  t=-1❌ t=1❌ t=3❌  t=5❌
          
Found! Path: Include 3 → Exclude 4 → Include 2 = 3+2 = 5 ✅
```

---

### 🎯 Complete Recursion Tree Example

**Problem**: `arr = [5, 10, 12, 13, 15, 18]`, `target = 30`

```
Complete exploration showing all branches:

                            (0, 13)
                           x₁ = 1
                          /        \
                    (5, 68)        (0, 73)
                    x₂ = 1          x₂ = 1
                   /      \
            (16, 58)    (5, 68)
            x₃ = 1       x₃ = 0
           /      \
      (21, 46)  (15, 48)
      x₄ = 1     x₄ = 0
     /      \
(19, 33) (27, 33)
   B      x₅ = 1
         /      \
    (43, 18) (27, 33)
       B      x₅ = 0
             /      \
        (28, 33) (15, 33)
        x₆ = 1    x₆ = 0
       /      \
   (43, 18) (30, 18) ✅
      B        B

Legend:
• (sum, remaining) at each node
• xᵢ = 1 means include element i
• xᵢ = 0 means exclude element i
• B means dead branch (backtrack)
• ✅ means target reached

Solution found: x = [1, 1, 0, 0, 1, 0]
Selected elements: arr[0]=5, arr[1]=10, arr[4]=15
Sum: 5 + 10 + 15 = 30 ✅

Constraint: Σ(wᵢ × xᵢ) ≤ m (where m = 30)
```

**Key Observations**:
- Each level explores Include (left) or Exclude (right)
- Dead branches (B) occur when sum exceeds target
- Multiple paths may lead to solution
- Backtracking prunes invalid branches early

---

### 🔍 DP Table Visualization: arr=[3,4,2], target=5

```
Building table bottom-up:

        Target →
        0   1   2   3   4   5
      ┌───┬───┬───┬───┬───┬───┐
i=0   │ T │ F │ F │ F │ F │ F │  (empty set: only sum 0 possible)
      ├───┼───┼───┼───┼───┼───┤
i=1   │ T │ F │ F │ T │ F │ F │  (with [3]: can make 0 or 3)
(3)   ├───┼───┼───┼───┼───┼───┤
i=2   │ T │ F │ F │ T │ T │ F │  (with [3,4]: can make 0,3,4,7)
(4)   ├───┼───┼───┼───┼───┼───┤
i=3   │ T │ F │ T │ T │ T │ T │  (with [3,4,2]: can make 0,2,3,4,5,6...)
(2)   └───┴───┴───┴───┴───┴───┘
                            ↑
                          dp[3][5] = True ✅

Logic for each cell:
dp[i][t] = dp[i-1][t]              (exclude current)
         OR dp[i-1][t - arr[i-1]]  (include current)
```

---

### 📝 Implementation (Tabulation - Optimal)

```python
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        
        # dp[i][t] = "Can we make sum t using first i elements?"
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Base Case: Sum 0 is always possible (empty subset)
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the table
        for i in range(1, n + 1):
            for t in range(1, target + 1):
                
                # Can we include current element?
                if arr[i-1] <= t:
                    # Include OR Exclude current element
                    dp[i][t] = dp[i-1][t - arr[i-1]] or dp[i-1][t]
                else:
                    # Too big to include, must exclude
                    dp[i][t] = dp[i-1][t]
        
        return dp[n][target]
```

**Key Points**:
- ✅ `dp[i][0] = True` → Empty subset makes sum 0
- ✅ Include: `dp[i-1][t - arr[i-1]]` → Use remaining sum
- ✅ Exclude: `dp[i-1][t]` → Skip current element
- ✅ Final answer at `dp[n][target]`

---

### 📝 Alternative: Memoization (Top-Down)

```python
class Solution:
    def isSubsetSum(self, arr, target):
        memo = {}
        
        def solve(i, remaining):
            # Base Cases
            if remaining == 0:
                return True
            if i >= len(arr) or remaining < 0:
                return False
            
            # Check memo
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            # Include OR Exclude
            result = (solve(i + 1, remaining - arr[i]) or 
                     solve(i + 1, remaining))
            
            memo[(i, remaining)] = result
            return result
        
        return solve(0, target)
```

---

### ⏱️ Complexity

**Tabulation (Optimal)**:
- **Time**: **O(N × Target)**
- **Space**: **O(N × Target)** for DP table

**Space Optimized** (using 1D array):
- **Space**: **O(Target)** - only keep previous row!

---

## 📊 Pattern Comparison

| Aspect | Letter Combinations | Subset Sum |
|--------|---------------------|------------|
| **Goal** | Generate ALL outputs | Answer YES/NO |
| **Method** | Backtracking (DFS) | Dynamic Programming |
| **Overlapping?** | No | Yes (same (i,t) computed multiple times) |
| **Memoization?** | Not needed | Essential for efficiency |
| **Time** | O(4ⁿ) | O(N × Target) |
| **Output** | List of strings | Boolean |

---

## 🔑 Key Takeaways

1. **Backtracking** = Generate ALL possibilities (no optimization)
2. **DP** = Optimize by storing subproblem results
3. **Phone Letters**: Each digit branches independently (no overlap)
4. **Subset Sum**: Same (index, target) pairs repeat → Use memoization!
5. **Tabulation** eliminates recursion stack overflow risk
6. **Include/Exclude** pattern works for both!

---
 