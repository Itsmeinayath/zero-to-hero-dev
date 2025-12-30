# 🔄 Subsets (Powerset) - LeetCode Problem 78

## 📋 Problem Statement

Given an integer array `nums` of **unique** elements, return **all possible subsets** (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Examples

**Example 1:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**
```
Input: nums = [0]
Output: [[],[0]]
```

---

## 💡 Core Pattern: Backtracking & Decision Tree

### The Key Insight

For each element at index `i`, we have **exactly 2 choices**:
1. **Include** it in the current subset
2. **Exclude** it from the current subset

This creates a **binary decision tree** with `2^n` leaf nodes (where n = length of nums).

### The Backtracking Template

```
At each index i:
  1. Make a choice (Include)
  2. Explore (Recurse)
  3. Undo the choice (Backtrack)
  4. Make alternate choice (Exclude)
  5. Explore (Recurse)
```

---

## 🎨 Visual Decision Tree (nums = [1,2,3])

```
                          []
                    /            \
              [1]                   []
            /      \              /      \
        [1,2]      [1]        [2]          []
       /    \     /   \      /   \        /   \
   [1,2,3] [1,2] [1,3] [1]  [2,3] [2]   [3]   []
```

**Each path from root to leaf = one subset**

- **Left branches**: Include current element
- **Right branches**: Exclude current element
- **Total subsets**: 2³ = 8 subsets

---

## 🛠️ Solution: Backtracking with DFS

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        def dfs(i):
            # Base case: reached end of array
            if i >= len(nums):
                res.append(subset.copy())  # ⚠️ MUST copy!
                return
            
            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # BACKTRACK: Undo the include decision
            subset.pop()
            
            # Decision 2: EXCLUDE nums[i]
            dfs(i + 1)
            
        dfs(0)
        return res
```

---

## 🔍 Step-by-Step Walkthrough (nums = [1,2])

| Call Stack | i | subset | Action |
|------------|---|--------|--------|
| dfs(0) | 0 | [] | Include 1 |
| dfs(1) | 1 | [1] | Include 2 |
| dfs(2) | 2 | [1,2] | ✅ Save [1,2] |
| (return) | 1 | [1,2] | Backtrack: pop 2 |
| dfs(2) | 2 | [1] | ✅ Save [1] |
| (return) | 0 | [1] | Backtrack: pop 1 |
| dfs(1) | 1 | [] | Include 2 |
| dfs(2) | 2 | [2] | ✅ Save [2] |
| (return) | 1 | [2] | Backtrack: pop 2 |
| dfs(2) | 2 | [] | ✅ Save [] |

**Result**: `[[], [1], [2], [1,2]]`

---

## ⚠️ Critical Point: Why `subset.copy()`?

```python
# ❌ WRONG - All subsets will be the same!
res.append(subset)

# ✅ CORRECT - Creates a snapshot
res.append(subset.copy())
```

**Reason**: `subset` is modified throughout recursion. Without `.copy()`, all entries in `res` would reference the **same list object**, which ends up empty after all backtracking.

---

## 📊 Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| **Time** | O(n × 2^n) | 2^n subsets, each takes O(n) to copy |
| **Space** | O(n) | Recursion depth (call stack) |
| **Output Size** | O(n × 2^n) | 2^n subsets, average length n/2 |

---

## 🎓 Alternative Approaches

### Approach 2: Iterative (Cascading)

```python
def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res
```

**How it works:**
- Start with `[[]]`
- For each number, add it to all existing subsets
- Example: `[] → [[]] → [[],[1]] → [[],[1],[2],[1,2]]`

**Complexity**: Same O(n × 2^n)

---

### Approach 3: Bit Manipulation

```python
def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    for i in range(2**n):  # 2^n possible subsets
        subset = []
        for j in range(n):
            if i & (1 << j):  # Check if j-th bit is set
                subset.append(nums[j])
        res.append(subset)
    return res
```

**Idea**: Each subset = a binary number (0 to 2^n-1)
- Bit 1 = include element
- Bit 0 = exclude element

---

## 🧠 Why Backtracking Works

1. **State Space**: We explore ALL 2^n combinations
2. **Path Building**: `subset` tracks current path in decision tree
3. **Backtracking**: Undoing choices lets us reuse the same list
4. **DFS**: Depth-first ensures we complete one path before starting another

---

## 🎯 The Backtracking Pattern (Universal Template)

```python
def backtrack(path, choices):
    if base_case:
        result.append(path.copy())
        return
    
    for choice in choices:
        # Make choice
        path.append(choice)
        
        # Explore
        backtrack(path, new_choices)
        
        # Undo choice (Backtrack)
        path.pop()
```

**This pattern applies to:**
- Subsets
- Permutations
- Combinations
- N-Queens
- Sudoku Solver
- Palindrome Partitioning

---

## 🔗 Related Problems

- **Subsets II** (LeetCode 90) - With duplicates
- **Permutations** (LeetCode 46)
- **Combinations** (LeetCode 77)
- **Combination Sum** (LeetCode 39)
- **Letter Case Permutation** (LeetCode 784)

---

## 💡 Common Mistakes to Avoid

1. ❌ Forgetting `subset.copy()` → All results reference same list
2. ❌ Not backtracking → Path never resets for alternate branches
3. ❌ Wrong base case → Missing or duplicate subsets
4. ❌ Mutating result → Not creating new list objects

---

## 📝 Key Takeaways

1. **Binary decisions** naturally lead to backtracking solutions
2. **DFS + Backtracking** = systematic exploration of all paths
3. **Always copy** mutable objects before adding to results
4. **Backtrack pattern** is universal - learn it once, use everywhere
5. **Time complexity** is dominated by output size (2^n subsets)

---

**Date**: Day 49 | Week 7  
**Topic**: Backtracking & Recursion  
**Difficulty**: Medium  
**Pattern**: Decision Tree / DFS  
**Status**: ✅ Solved
