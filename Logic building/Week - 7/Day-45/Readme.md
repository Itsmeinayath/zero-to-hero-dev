# Day 45 — Backtracking Basics 🔙

**Topic**: Subsets Pattern (Include/Exclude)

---

## 📚 Overview

Today is the **most important conceptual leap**. We're using our **Recursion tool** (Day 43) to build our first **Backtracking pattern**.

**Key Insight**: Backtracking is NOT a new, magic concept. It's just **"Recursive Looping"** to explore all possible choices.

---

## 🎯 TL;DR - The Golden Rule

### The Three Steps

```
1. CHOOSE   → Add item to current path
2. EXPLORE  → Make recursive call
3. UNCHOOSE → Remove item (backtrack!)
```

### Visual Representation

```
Current Path: [1]
              ↓
         CHOOSE 2
              ↓
Current Path: [1, 2]
              ↓
         EXPLORE (recurse)
              ↓
         UNCHOOSE 2
              ↓
Current Path: [1]  ← Back to try next choice!
```

---

## 💡 Core Concept: What is Backtracking?

**Simple Definition**: A `for` loop inside a recursive function.

### The Maze Analogy

```
You're in a maze:
1. Try path A → Dead end? → Backtrack
2. Try path B → Dead end? → Backtrack  
3. Try path C → Success!

Same with subsets:
1. Try including number → Explore
2. Backtrack (remove it)
3. Try excluding number → Explore
```

---

## 🧠 Two Patterns We Learned

| Pattern | Problem | Technique |
|---------|---------|-----------|
| **Include/Exclude** | Subsets I | Two recursive calls per number |
| **Sort & Skip** | Subsets II | Prune duplicate branches |

---

## ⚠️ CRITICAL Rule

**Always use `.copy()` when saving results!**

```python
# ❌ WRONG - saves reference
result.append(current_subset)

# ✅ CORRECT - saves a copy
result.append(current_subset.copy())
```

**Why?** Without `.copy()`, all your subsets will be empty at the end because they all point to the same list that gets cleared!


---

## 🎨 Pattern 1: Subsets (LeetCode 78)

**The "Include/Exclude" Pattern**

### Problem Statement

> Given an array `nums` of unique integers, return all possible subsets.

**Example**:
```
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

---

### 🌳 Visual: Decision Tree for [1, 2, 3]

```
                        []
                       /  \
                 Include  Exclude
                   1        1
                  /          \
              [1]              []
             /   \            /   \
        Include Exclude  Include Exclude
          2       2        2       2
         /         \      /         \
     [1,2]        [1]   [2]         []
     /   \        /  \  /  \       /  \
    Inc  Exc    Inc Exc Inc Exc  Inc Exc
    3     3     3   3   3   3    3   3
   /       \    |   |   |   |    |   |
[1,2,3] [1,2] [1,3][1][2,3][2] [3] []

✅ Result: 8 subsets = 2³ (all combinations)
```

---

### 📝 Implementation (Include/Exclude)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_subset = []  # Our "current path" notepad

        def backtrack(index):
            # Base Case: We've made a decision for all numbers
            if index == len(nums):
                # CRITICAL: Must use .copy()!
                result.append(current_subset.copy())
                return
            
            # --- Path 1: INCLUDE nums[index] ---
            # 1. CHOOSE
            current_subset.append(nums[index])
            # 2. EXPLORE
            backtrack(index + 1)
            # 3. UNCHOOSE (the backtrack!)
            current_subset.pop()
            
            # --- Path 2: EXCLUDE nums[index] ---
            # We choose nothing, just explore without it
            backtrack(index + 1)
        
        backtrack(0)  # Start at index 0
        return result
```

---

### 🔍 Step-by-Step Trace: `nums = [1, 2]`

```
Step 1: backtrack(0), current = []
        ├─ CHOOSE 1 → current = [1]
        │  └─ backtrack(1), current = [1]
        │     ├─ CHOOSE 2 → current = [1, 2]
        │     │  └─ backtrack(2) → BASE CASE → save [1, 2] ✅
        │     │     UNCHOOSE 2 → current = [1]
        │     └─ backtrack(2) → BASE CASE → save [1] ✅
        │  UNCHOOSE 1 → current = []
        └─ backtrack(1), current = []
           ├─ CHOOSE 2 → current = [2]
           │  └─ backtrack(2) → BASE CASE → save [2] ✅
           │     UNCHOOSE 2 → current = []
           └─ backtrack(2) → BASE CASE → save [] ✅

Result: [[], [1], [1, 2], [2]]
```

---

### ⏱️ Complexity Analysis

- **Time**: **O(N × 2ⁿ)**
  - Generate 2ⁿ subsets (each element: include or exclude)
  - Each subset takes O(N) to copy
  - Total: O(N × 2ⁿ)

- **Space**: **O(N)**
  - `current_subset`: O(N) max size
  - Call stack depth: O(N)
  - Result list not counted
  - Total: O(N)

---

## 🎨 Pattern 2: Subsets II (LeetCode 90)

**The "Sort & Skip" Pattern for Duplicates**

### Problem Statement

> Given an array `nums` that may contain duplicates, return all possible unique subsets.

**Example**:
```
Input: nums = [1, 2, 2]
Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]
```

---

### 💡 The Duplicate Problem

**Without pruning**:
```
Input: [1, 2, 2]

Bad output (with duplicates):
[[], [1], [1,2], [1,2,2], [2], [2,2], [1,2], [1,2,2], [2], [2,2]]
                                        ↑________________↑
                                        Duplicates! ❌
```

**Why?** Both 2's create identical branches.

---

### 🔧 The "Sort & Skip" Solution

**Two steps**:

1. **SORT** → Groups duplicates together: `[1, 2, 2]`
2. **SKIP** → Skip duplicate at same recursion level

### Visual: Pruning Duplicates

```
After sorting: [1, 2, 2]

                    []
                   /|\
                  1 2 2'  ← Skip 2'! (duplicate at same level)
                 /  |
               [1] [2]
               /|   |
              2 2'  2'  ← Skip 2'!
             /      
          [1,2]   [2,2]
            |       |
            2'      (done)
            |
        [1,2,2]

✅ Pruned! Only explore unique branches.
```

---

### 📝 Implementation (Sort & Skip)

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_subset = []
        
        # --- STEP 1: SORT ---
        # Groups duplicates together
        nums.sort()
        
        def backtrack(start_index):
            # Save current path (every call adds a subset)
            result.append(current_subset.copy())
            
            # Exploration loop
            for i in range(start_index, len(nums)):
                
                # --- STEP 2: SKIP (The pruning!) ---
                # Skip if:
                # 1. Not first element in this loop (i > start_index)
                # 2. Same as previous (nums[i] == nums[i-1])
                if i > start_index and nums[i] == nums[i-1]:
                    continue  # Skip this duplicate branch!
                
                # --- Golden Rule ---
                # 1. CHOOSE
                current_subset.append(nums[i])
                # 2. EXPLORE
                backtrack(i + 1)
                # 3. UNCHOOSE
                current_subset.pop()
        
        backtrack(0)
        return result
```

---

### 🔍 Step-by-Step Trace: `nums = [1, 2, 2]`

```
After sort: [1, 2, 2]

Step 1: backtrack(0), current = []
        Save [] ✅
        Loop i=0,1,2:
        
        i=0 (nums[0]=1):
        ├─ CHOOSE 1 → current = [1]
        │  └─ backtrack(1), current = [1]
        │     Save [1] ✅
        │     Loop i=1,2:
        │     
        │     i=1 (nums[1]=2):
        │     ├─ CHOOSE 2 → current = [1, 2]
        │     │  └─ backtrack(2), current = [1, 2]
        │     │     Save [1, 2] ✅
        │     │     Loop i=2:
        │     │     
        │     │     i=2 (nums[2]=2):
        │     │     ├─ CHOOSE 2 → current = [1, 2, 2]
        │     │     │  └─ backtrack(3) → Save [1, 2, 2] ✅
        │     │     └─ UNCHOOSE → current = [1, 2]
        │     └─ UNCHOOSE → current = [1]
        │     
        │     i=2: SKIP! (i > 1 and nums[2] == nums[1]) ⚡
        │  
        │  UNCHOOSE 1 → current = []
        
        i=1 (nums[1]=2):
        ├─ CHOOSE 2 → current = [2]
        │  └─ backtrack(2), current = [2]
        │     Save [2] ✅
        │     Loop i=2:
        │     
        │     i=2 (nums[2]=2):
        │     └─ CHOOSE 2 → current = [2, 2]
        │        └─ backtrack(3) → Save [2, 2] ✅
        │  
        │  UNCHOOSE 2 → current = []
        
        i=2: SKIP! (i > 0 and nums[2] == nums[1]) ⚡

Result: [[], [1], [1,2], [1,2,2], [2], [2,2]]
```

---

### ⏱️ Complexity Analysis

- **Time**: **O(N × 2ⁿ)**
  - O(N log N) to sort
  - Generate 2ⁿ subsets
  - Each subset takes O(N) to copy
  - Total: O(N log N) + O(N × 2ⁿ) → **O(N × 2ⁿ)**

- **Space**: **O(N)**
  - `current_subset`: O(N)
  - Call stack: O(N)
  - Total: O(N)

---

## 📊 Pattern Comparison

| Aspect | Include/Exclude | Sort & Skip |
|--------|-----------------|-------------|
| **Use Case** | Unique elements | Duplicates allowed |
| **Structure** | Two recursive calls | One loop with recursion |
| **Pruning** | None needed | Skip duplicates |
| **Preprocessing** | None | Sort array first |
| **When to use** | Simpler problems | When duplicates exist |

---

## 🎓 The Backtracking Template

```python
def backtrack(start_index, current_path):
    # 1. Save current state (if needed)
    result.append(current_path.copy())
    
    # 2. Explore all choices
    for i in range(start_index, len(choices)):
        
        # 3. Pruning (optional - skip invalid choices)
        if should_skip(i):
            continue
        
        # 4. CHOOSE
        current_path.append(choices[i])
        
        # 5. EXPLORE (recurse)
        backtrack(i + 1, current_path)
        
        # 6. UNCHOOSE (backtrack!)
        current_path.pop()
```

---

## 🔑 Key Takeaways

1. **Backtracking = Recursion + Loop** to explore all choices
2. **Golden Rule**: Choose → Explore → Unchoose
3. **Always use `.copy()`** when saving to result
4. **Include/Exclude**: Two paths per element (simpler)
5. **Sort & Skip**: Prune duplicates with one check
6. **Time is always O(N × 2ⁿ)** - must generate all subsets
7. **Space is O(N)** - current path + call stack

---
