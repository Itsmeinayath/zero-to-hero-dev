# Day 46 — Backtracking Applications 🔄

**Topic**: Permutations & Combination Sum

---

## 📚 Overview

Today we applied the **"Golden Rule"** of Backtracking (Choose → Explore → Unchoose) to two classic combinatorial problems:

1. **Permutations** - Order matters, pick each once
2. **Combination Sum** - Order doesn't matter, reuse allowed

---

## 🎯 TL;DR - Key Differences

| Problem | Question | Order | Reuse | Tracking |
|---------|----------|-------|-------|----------|
| **Permutations** | "Which unused number goes here?" | ✅ Matters | ❌ No | `used[]` array |
| **Combination Sum** | "Include or exclude this number?" | ❌ Doesn't matter | ✅ Yes | `start_index` |

---

## 💡 Core Concepts

### Permutations vs Combinations

```
Permutations [1,2,3]:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
         ↑ Order matters! [1,2,3] ≠ [3,2,1]

Combinations [1,2,3]:
[1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], []
         ↑ Order doesn't matter! [1,2] = [2,1]
```

### The "Unchoose" Magic

**Critical**: `.pop()` undoes our choice to explore the next branch!

```
current = [1, 2]
          ↓ CHOOSE 3
current = [1, 2, 3] → Explore this path
          ↓ UNCHOOSE 3 (pop!)
current = [1, 2] → Ready to try next choice!
```

---

## 🎨 Pattern 1: Permutations (LeetCode 46)

**The Decision**: "Which **unused** number goes in the current slot?"

### Problem Statement

> Given an array `nums` of distinct integers, return all possible permutations.

**Example**:
```
Input: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

---

### 🌳 Visual: Decision Tree for [1, 2, 3]

```
                        []
                       / | \
                      1  2  3
                     /   |   \
                  [1]   [2]   [3]
                 / \    / \    / \
                2   3  1   3  1   2
               /     \ |   | |   |
            [1,2]  [1,3][2,1][2,3][3,1][3,2]
              |      |   |   |   |   |
              3      2   3   1   2   1
              |      |   |   |   |   |
          [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]

✅ 6 permutations = 3! (factorial)
Each level: fewer choices (used array prevents reuse)
```

---

### 🔍 Step-by-Step Trace: `nums = [1, 2]`

```
used = [False, False]

Step 1: current = []
        Loop i=0,1:
        
        i=0 (nums[0]=1, not used):
        ├─ CHOOSE 1 → used[0]=True, current=[1]
        │  └─ backtrack(), current=[1]
        │     Loop i=0,1:
        │     
        │     i=0: SKIP (used[0]=True) ⚠️
        │     
        │     i=1 (nums[1]=2, not used):
        │     ├─ CHOOSE 2 → used[1]=True, current=[1,2]
        │     │  └─ backtrack() → FULL! Save [1,2] ✅
        │     │     UNCHOOSE 2 → used[1]=False, current=[1]
        │     
        │  UNCHOOSE 1 → used[0]=False, current=[]
        
        i=1 (nums[1]=2, not used):
        ├─ CHOOSE 2 → used[1]=True, current=[2]
        │  └─ backtrack(), current=[2]
        │     Loop i=0,1:
        │     
        │     i=0 (nums[0]=1, not used):
        │     ├─ CHOOSE 1 → used[0]=True, current=[2,1]
        │     │  └─ backtrack() → FULL! Save [2,1] ✅
        │     │     UNCHOOSE 1 → used[0]=False, current=[2]
        │     
        │     i=1: SKIP (used[1]=True) ⚠️
        │  
        │  UNCHOOSE 2 → used[1]=False, current=[]

Result: [[1,2], [2,1]]
```

---

### 📝 Implementation

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_perm = []
        used = [False] * len(nums)  # Track which indices are used
        
        def backtrack():
            # Base Case: Built a complete permutation
            if len(current_perm) == len(nums):
                result.append(current_perm.copy())
                return
            
            # Try each number
            for i in range(len(nums)):
                # Skip if already used in current path
                if used[i]:
                    continue
                
                # --- Golden Rule ---
                # 1. CHOOSE
                used[i] = True
                current_perm.append(nums[i])
                
                # 2. EXPLORE
                backtrack()
                
                # 3. UNCHOOSE
                current_perm.pop()
                used[i] = False
        
        backtrack()
        return result
```

**Key Points**:
- ✅ `used[]` array prevents picking same number twice
- ✅ Try **all** unused numbers at each position
- ✅ Order matters: [1,2] ≠ [2,1]
- ✅ Base case: when path length equals array length

---

### ⏱️ Complexity Analysis

- **Time**: **O(N × N!)**
  - Generate N! permutations
  - Each permutation takes O(N) to copy
  - Total: O(N × N!)

- **Space**: **O(N)**
  - `current_perm`: O(N)
  - `used`: O(N)
  - Call stack: O(N) depth
  - Total: O(N)

---

## 🎨 Pattern 2: Combination Sum (LeetCode 39)

**The Decision**: "Include this number (stay here) OR Exclude (move next)?"

### Problem Statement

> Given an array `candidates` and a target, return all unique combinations where the sum equals target. You may reuse numbers.

**Example**:
```
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2,2,3], [7]]
```

---

### 🌳 Visual: Decision Tree for [2, 3], target = 5

```
                    [] (target=5)
                   /            \
            Include 2          Exclude 2
               ↓                    ↓
          [2] (t=3)            [] (t=5)
          /        \              /      \
    Include 2   Exclude 2   Include 3  Exclude 3
       ↓            ↓            ↓          ↓
   [2,2] (t=1)  [2] (t=3)    [3] (t=2)   [] (t=5)
    /     \       /    \        /    \       (end)
  Inc 2  Exc 2  Inc 3 Exc 3  Inc 3 Exc
   ↓       ↓     ↓      ↓      ↓
[2,2,2] [2,2]  [2,3]  [2]   [3,3]
(t=-1)  (t=1)  (t=0)  (t=3) (t=-1)
  ❌      ❌     ✅     ...    ❌

Result: [[2,2,2], [2,3]] (only sum = 5)

Note: We stay at index i when including to allow reuse!
```

---

### 🔍 Step-by-Step Trace: `candidates = [2, 3], target = 5`

```
Step 1: backtrack(0, 5), current=[]
        Loop i=0,1:
        
        i=0 (candidates[0]=2):
        ├─ CHOOSE 2 → current=[2]
        │  └─ backtrack(0, 3), current=[2]  ← Pass i=0 (allow reuse!)
        │     Loop i=0,1:
        │     
        │     i=0 (candidates[0]=2):
        │     ├─ CHOOSE 2 → current=[2,2]
        │     │  └─ backtrack(0, 1), current=[2,2]
        │     │     Loop i=0,1:
        │     │     
        │     │     i=0: CHOOSE 2 → current=[2,2,2]
        │     │          backtrack(0, -1) → NEGATIVE! Return ❌
        │     │          UNCHOOSE → current=[2,2]
        │     │     
        │     │     i=1: CHOOSE 3 → current=[2,2,3]
        │     │          backtrack(1, -2) → NEGATIVE! Return ❌
        │     │          UNCHOOSE → current=[2,2]
        │     │
        │     │  UNCHOOSE 2 → current=[2]
        │     
        │     i=1 (candidates[1]=3):
        │     ├─ CHOOSE 3 → current=[2,3]
        │     │  └─ backtrack(1, 0) → TARGET! Save [2,3] ✅
        │     │     UNCHOOSE 3 → current=[2]
        │     
        │  UNCHOOSE 2 → current=[]
        
        i=1 (candidates[1]=3):
        ├─ CHOOSE 3 → current=[3]
        │  └─ backtrack(1, 2), current=[3]
        │     Loop i=1:
        │     
        │     i=1: CHOOSE 3 → current=[3,3]
        │          backtrack(1, -1) → NEGATIVE! Return ❌
        │          UNCHOOSE → current=[3]
        │  
        │  UNCHOOSE 3 → current=[]

Result: [[2,3]]
```

---

### 📝 Implementation

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_combo = []
        
        def backtrack(start_index, current_target):
            # Base Case 1: Found valid combination
            if current_target == 0:
                result.append(current_combo.copy())
                return
            
            # Base Case 2: Exceeded target (prune this branch)
            if current_target < 0:
                return
            
            # Loop from start_index to avoid duplicate combinations
            # e.g., [2,3] and [3,2] are considered the same
            for i in range(start_index, len(candidates)):
                
                # --- Golden Rule ---
                # 1. CHOOSE
                current_combo.append(candidates[i])
                
                # 2. EXPLORE
                # KEY: Pass 'i' (not i+1) to allow reuse of same number!
                backtrack(i, current_target - candidates[i])
                
                # 3. UNCHOOSE
                current_combo.pop()
        
        backtrack(0, target)
        return result
```

**Key Points**:
- ✅ Pass `i` (not `i+1`) to allow **reuse** of same number
- ✅ `start_index` prevents duplicates like [2,3] and [3,2]
- ✅ Two base cases: `target == 0` (success), `target < 0` (fail)
- ✅ Subtract from target as we explore

---

### ⏱️ Complexity Analysis

- **Time**: **O(N^(T/M))**
  - N = number of candidates
  - T = target value
  - M = minimal value in candidates
  - Worst case: exponential tree depth
  - Example: If min=1, target=10 → depth=10

- **Space**: **O(T/M)**
  - Maximum recursion depth = T/M
  - `current_combo` max size = T/M
  - Total: O(T/M)

---

## 📊 Pattern Comparison

| Aspect | Permutations | Combination Sum |
|--------|--------------|-----------------|
| **Order** | Matters ([1,2] ≠ [2,1]) | Doesn't matter ([1,2] = [2,1]) |
| **Reuse** | ❌ Each element once | ✅ Can reuse elements |
| **Tracking** | `used[]` boolean array | `start_index` parameter |
| **Loop** | All indices (0 to N-1) | From `start_index` to N-1 |
| **Recursive call** | `backtrack()` | `backtrack(i, new_target)` |
| **Base case** | Length equals N | Target equals 0 |
| **Results** | N! permutations | Variable combinations |

---

## 🔑 Key Takeaways

1. **Permutations**: Use `used[]` to track picked numbers (order matters)
2. **Combination Sum**: Use `start_index` to avoid duplicates (order doesn't matter)
3. **Reuse trick**: Pass `i` (not `i+1`) to allow same number again
4. **Pruning**: Return early when `target < 0` saves computation
5. **Always `.copy()`**: When saving to result
6. **Unchoose is critical**: `.pop()` and `used[i] = False` enable backtracking

---
