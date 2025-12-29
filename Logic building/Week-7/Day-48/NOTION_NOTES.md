# Day 48 - Recursion Recap & DP Bridge - Detailed Notion Notes


---

## 🎯 Learning Objectives

By the end of this lesson, you should be able to:
1. ✅ Distinguish between Backtracking and DP use cases
2. ✅ Implement phone keypad letter combinations
3. ✅ Solve Subset Sum using 3 different approaches
4. ✅ Recognize when to use memoization vs tabulation
5. ✅ Understand Include/Exclude decision pattern

---

## 🧠 Core Concepts

### 1. Backtracking vs Dynamic Programming

**When to use Backtracking:**
- Need to generate ALL possible solutions
- No overlapping subproblems
- Output is a list/collection of results
- Examples: Permutations, Combinations, Letter Combinations

**When to use Dynamic Programming:**
- Need to find ONE optimal solution or answer YES/NO
- Has overlapping subproblems (same state computed multiple times)
- Can cache intermediate results
- Examples: Fibonacci, Subset Sum, Coin Change, LCS

**Key Difference:**
```
Backtracking: Explore ALL paths → Generate complete solution set
DP: Optimize ONE path → Find best/valid solution efficiently
```

---

## 📱 Problem 1: Letter Combinations of a Phone Number

### Problem Description

**LeetCode 17**: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

**Phone Mapping:**
```
2: abc    3: def
4: ghi    5: jkl    6: mno
7: pqrs   8: tuv    9: wxyz
```

**Examples:**
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "2"
Output: ["a","b","c"]

Input: digits = ""
Output: []
```

---

### Why Backtracking?

**No Overlapping Subproblems:**
- Each digit is independent
- Digit "2" always maps to "abc" regardless of previous choices
- No repeated computation of same states
- Must generate ALL combinations → Can't optimize with memoization

**Decision Tree Structure:**
- Each level = one digit
- Each branch = one letter choice for that digit
- Depth = number of digits
- Total combinations = product of choices per digit

---

### Visual Explanation

#### Phone Keypad Layout
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
│     │  +  │     │
└─────┴─────┴─────┘
```

#### Decision Tree for "23"
```
Level 0:              ""
                     /│\
                    / │ \
Level 1:           a  b  c       ← Digit "2" choices
                  /|\ /|\ /|\
Level 2:         d e f d e f d e f  ← Digit "3" choices
                 │ │ │ │ │ │ │ │ │
Results:        ad ae af bd be bf cd ce cf
```

**Tree Properties:**
- **Height**: Number of digits (2 in this case)
- **Branching Factor**: 3-4 (letters per digit)
- **Total Leaves**: 3 × 3 = 9 combinations
- **Time Complexity**: O(4^n × n) where n = length of digits

---

### Step-by-Step Execution

**Input**: `digits = "23"`

```
Call Stack Visualization:

Step 1: backtrack(0, "")
        │
        ├─ Try 'a' from "2"
        │  └─ backtrack(1, "a")
        │     │
        │     ├─ Try 'd' from "3"
        │     │  └─ backtrack(2, "ad")
        │     │     └─ i == len(digits) → SAVE "ad" ✅
        │     │
        │     ├─ Try 'e' from "3"
        │     │  └─ backtrack(2, "ae")
        │     │     └─ i == len(digits) → SAVE "ae" ✅
        │     │
        │     └─ Try 'f' from "3"
        │        └─ backtrack(2, "af")
        │           └─ i == len(digits) → SAVE "af" ✅
        │
        ├─ Try 'b' from "2"
        │  └─ backtrack(1, "b")
        │     │
        │     ├─ Try 'd' from "3" → SAVE "bd" ✅
        │     ├─ Try 'e' from "3" → SAVE "be" ✅
        │     └─ Try 'f' from "3" → SAVE "bf" ✅
        │
        └─ Try 'c' from "2"
           └─ backtrack(1, "c")
              │
              ├─ Try 'd' from "3" → SAVE "cd" ✅
              ├─ Try 'e' from "3" → SAVE "ce" ✅
              └─ Try 'f' from "3" → SAVE "cf" ✅

Final Result: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

### Implementation Details

#### Python Solution
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: empty input
        if not digits:
            return []
        
        # Phone keypad mapping
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_string):
            # Base Case: We've processed all digits
            if index == len(digits):
                result.append(current_string)
                return
            
            # Get letters for current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Try each letter
            for letter in letters:
                # Recurse with next digit
                # Note: String concatenation creates new string (immutable)
                # So no explicit "unchoose" needed!
                backtrack(index + 1, current_string + letter)
        
        # Start backtracking
        backtrack(0, "")
        return result
```

#### Key Implementation Notes

**Why No Explicit Unchoose?**
- Strings in Python are **immutable**
- `current_string + letter` creates a NEW string
- Original `current_string` remains unchanged
- Each recursive call has its own copy
- No need to manually "pop" or "remove"

**Alternative with List (Requires Unchoose):**
```python
def backtrack(index, current_list):
    if index == len(digits):
        result.append(''.join(current_list))
        return
    
    for letter in phone_map[digits[index]]:
        current_list.append(letter)  # CHOOSE
        backtrack(index + 1, current_list)  # EXPLORE
        current_list.pop()  # UNCHOOSE (needed for lists!)
```

---

### Complexity Analysis

#### Time Complexity: O(4^n × n)
- **4^n**: Each digit has up to 4 letters (digits 7 and 9)
- **n**: Each combination takes O(n) time to build/copy
- For "23": 3 × 3 = 9 combinations, each of length 2 → O(9 × 2) = O(18)
- For "7777": 4^4 = 256 combinations, each of length 4 → O(256 × 4) = O(1024)

#### Space Complexity: O(n)
- **Call stack**: O(n) depth (one level per digit)
- **Current string**: O(n) length
- **Output not counted** in space complexity analysis
- Total auxiliary space: O(n)

---

### Common Pitfalls & Tips

❌ **Mistake 1**: Including digits 0 and 1
```python
# Wrong - 0 and 1 don't have letters
phone_map = {"0": "", "1": "", "2": "abc", ...}
```

❌ **Mistake 2**: Forgetting empty input check
```python
# This will return [""] instead of []
if not digits:
    return []  # Must check this!
```

✅ **Tip 1**: Strings are immutable - no unchoose needed  
✅ **Tip 2**: Use dictionary for O(1) lookup of letters  
✅ **Tip 3**: Base case checks `index == len(digits)`  
✅ **Tip 4**: Can also use BFS (iterative) approach with queue

---

## 🎒 Problem 2: Subset Sum Problem

### Problem Description

**GeeksforGeeks**: Given a set of non-negative integers and a target value, determine if there exists a subset whose sum equals the target.

**Examples:**
```
Input: arr = [3, 34, 4, 12, 5, 2], target = 9
Output: True
Explanation: 3 + 4 + 2 = 9 or 4 + 5 = 9

Input: arr = [3, 34, 4, 12, 5, 2], target = 30
Output: False
Explanation: No subset sums to 30

Input: arr = [1, 2, 3], target = 6
Output: True
Explanation: 1 + 2 + 3 = 6
```

---

### Why Dynamic Programming?

**Has Overlapping Subproblems:**
- Same (index, remaining_sum) computed multiple times
- Example: `solve(2, 5)` might be reached via:
  - Include arr[0], Include arr[1]
  - Exclude arr[0], Include arr[1]
- Memoization prevents recalculation

**Optimal Substructure:**
- Problem breaks down into smaller subproblems
- `canMakeSum(i, target)` depends on:
  - `canMakeSum(i+1, target)` (exclude current)
  - `canMakeSum(i+1, target - arr[i])` (include current)

---

### The Three Approaches

#### Approach 1: Brute Force (Naive Recursion)

**Idea**: Try all 2^n subsets

**Pseudocode:**
```
function canMakeSum(index, remaining):
    if remaining == 0:
        return True  // Found valid subset!
    if index >= n or remaining < 0:
        return False  // Invalid state
    
    // Include current element OR Exclude it
    return canMakeSum(index+1, remaining - arr[index]) OR
           canMakeSum(index+1, remaining)
```

**Complexity:**
- Time: O(2^n) - exponential
- Space: O(n) - recursion depth

**Why It's Slow:**
- Recalculates same states repeatedly
- No caching of results
- Example: For n=20, checks 1,048,576 subsets!

---

#### Approach 2: Memoization (Top-Down DP)

**Idea**: Cache results using (index, remaining) as key

**Pseudocode:**
```
memo = {}

function canMakeSum(index, remaining):
    if remaining == 0:
        return True
    if index >= n or remaining < 0:
        return False
    
    // Check cache first!
    if (index, remaining) in memo:
        return memo[(index, remaining)]
    
    // Compute and cache
    result = canMakeSum(index+1, remaining - arr[index]) OR
             canMakeSum(index+1, remaining)
    
    memo[(index, remaining)] = result
    return result
```

**Complexity:**
- Time: O(n × target) - each state computed once
- Space: O(n × target) - memo + recursion stack

**Why It's Better:**
- Each unique (index, remaining) computed once
- Subsequent calls are O(1) lookup
- Massive speedup for large inputs

---

#### Approach 3: Tabulation (Bottom-Up DP)

**Idea**: Build 2D table iteratively

**Table Definition:**
- `dp[i][t]` = "Can we make sum `t` using first `i` elements?"
- Rows: Elements (0 to n)
- Columns: Target values (0 to target)

**Recurrence Relation:**
```
dp[i][t] = dp[i-1][t]                    // Exclude arr[i-1]
        OR dp[i-1][t - arr[i-1]]         // Include arr[i-1]
           (if arr[i-1] <= t)
```

**Complexity:**
- Time: O(n × target) - fill entire table
- Space: O(n × target) - 2D table

**Why It's Optimal:**
- No recursion stack overhead
- Iterative approach (no stack overflow)
- Easy to optimize space to O(target)

---

### Visual Explanation - Decision Tree

#### Example: arr=[3, 4, 2], target=5

```
                        (i=0, remaining=5)
                       "Can make 5?"
                      /              \
               Include 3            Exclude 3
                    ↓                    ↓
              (i=1, r=2)            (i=1, r=5)
             "Can make 2?"         "Can make 5?"
             /          \          /          \
        Inc 4        Exc 4    Inc 4        Exc 4
          ↓            ↓        ↓            ↓
    (i=2, r=-2)  (i=2, r=2) (i=2, r=1)  (i=2, r=5)
        ❌         ✓ Path 1    ✓ Path 2      ❌

Path 1 (Include 3, Exclude 4, Include 2):
  └─ (i=2, r=2)
     Include 2 → (i=3, r=0) ✅ SUCCESS!
     Selected: [3, 2] → 3+2 = 5 ✅

Path 2 (Exclude 3, Include 4, Include 2):
  └─ (i=2, r=1)
     Include 2 → (i=3, r=-1) ❌ FAIL
     Exclude 2 → (i=3, r=1) ❌ FAIL
```

**Overlapping Subproblems Example:**
```
(i=2, r=2) appears multiple times in different branches
Without memoization: Computed repeatedly
With memoization: Computed once, cached, reused
```

---

### Complete Tree Example (From Whiteboard)

**Problem**: `arr = [5, 10, 12, 13, 15, 18]`, `target = 30`

```
Full Recursion Tree:

                            (0, 13) [x₁=1]
                           /              \
                    (5, 68)              (0, 73)
                    [x₂=1]               [x₂=1]
                   /        \
            (16, 58)      (5, 68)
            [x₃=1]        [x₃=0]
           /      \
      (21, 46)  (15, 48)
      [x₄=1]     [x₄=0]
     /      \
(19, 33) (27, 33)
   B      [x₅=1]
         /      \
    (43, 18) (27, 33)
       B      [x₅=0]
             /      \
        (28, 33) (15, 33)
        [x₆=1]    [x₆=0]
       /      \
   (43, 18) (30, 18) ← TARGET! ✅
      B        B

Legend:
• Each node: (current_sum, remaining_target)
• xᵢ = 1: Include element i
• xᵢ = 0: Exclude element i  
• B: Dead branch (backtrack)
• ✅: Solution found

Solution: x = [1, 1, 0, 0, 1, 0]
Elements selected: arr[0]=5, arr[1]=10, arr[4]=15
Sum: 5 + 10 + 15 = 30 ✅
```

**Key Observations:**
1. Binary tree structure (Include/Exclude at each step)
2. Many branches pruned early (marked with B)
3. Sum tracked at each node
4. Multiple paths may exist (early termination possible)
5. Constraint: Σ(wᵢ × xᵢ) ≤ m where m=30

---

### DP Table Visualization

#### Building Table for arr=[3, 4, 2], target=5

```
Step-by-Step Table Construction:

Initial State:
        0   1   2   3   4   5
      ┌───┬───┬───┬───┬───┬───┐
i=0   │ T │ F │ F │ F │ F │ F │  Empty set
      └───┴───┴───┴───┴───┴───┘

After processing arr[0]=3:
        0   1   2   3   4   5
      ┌───┬───┬───┬───┬───┬───┐
i=0   │ T │ F │ F │ F │ F │ F │
i=1   │ T │ F │ F │ T │ F │ F │  Can make 0 or 3
      └───┴───┴───┴───┴───┴───┘

After processing arr[1]=4:
        0   1   2   3   4   5
      ┌───┬───┬───┬───┬───┬───┐
i=0   │ T │ F │ F │ F │ F │ F │
i=1   │ T │ F │ F │ T │ F │ F │
i=2   │ T │ F │ F │ T │ T │ F │  Can make 0,3,4,7
      └───┴───┴───┴───┴───┴───┘

After processing arr[2]=2:
        0   1   2   3   4   5
      ┌───┬───┬───┬───┬───┬───┐
i=0   │ T │ F │ F │ F │ F │ F │
i=1   │ T │ F │ F │ T │ F │ F │
i=2   │ T │ F │ F │ T │ T │ F │
i=3   │ T │ F │ T │ T │ T │ T │  Can make 0,2,3,4,5,6,7,9
      └───┴───┴───┴───┴───┴───┘
                            ↑
                     dp[3][5] = True ✅
```

**Cell Calculation Example:**
```
For dp[3][5] (can make 5 using [3,4,2]):

arr[2] = 2, target = 5

Option 1: Include 2
  → Check dp[2][5-2] = dp[2][3] = True ✓
  
Option 2: Exclude 2
  → Check dp[2][5] = False ✗

Result: True OR False = True ✅
```

---

### Implementation - Tabulation (Optimal)

```python
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        
        # Create DP table
        # dp[i][t] = Can we make sum t using first i elements?
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Base Case: Sum 0 is always possible with empty subset
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the table bottom-up
        for i in range(1, n + 1):
            for t in range(1, target + 1):
                
                # Can we include current element?
                if arr[i-1] <= t:
                    # Option 1: Include arr[i-1]
                    include = dp[i-1][t - arr[i-1]]
                    # Option 2: Exclude arr[i-1]
                    exclude = dp[i-1][t]
                    # Take OR of both options
                    dp[i][t] = include or exclude
                else:
                    # Element too large, must exclude
                    dp[i][t] = dp[i-1][t]
        
        # Final answer
        return dp[n][target]
```

**Line-by-Line Explanation:**

```python
dp = [[False] * (target + 1) for _ in range(n + 1)]
```
- Creates (n+1) × (target+1) table
- Extra row for "0 elements" base case
- All initialized to False

```python
for i in range(n + 1):
    dp[i][0] = True
```
- Base case: Sum 0 always possible (empty subset)
- First column all True

```python
if arr[i-1] <= t:
```
- Only include if element ≤ remaining target
- arr[i-1] because dp uses 1-based indexing

```python
include = dp[i-1][t - arr[i-1]]
```
- If we include arr[i-1], can we make (t - arr[i-1]) with previous elements?

```python
exclude = dp[i-1][t]
```
- If we exclude arr[i-1], can we make t with previous elements?

```python
dp[i][t] = include or exclude
```
- If EITHER option works, answer is True

---

### Implementation - Memoization (Top-Down)

```python
class Solution:
    def isSubsetSum(self, arr, target):
        memo = {}
        
        def solve(index, remaining):
            # Base Case 1: Found exact sum
            if remaining == 0:
                return True
            
            # Base Case 2: Invalid state
            if index >= len(arr) or remaining < 0:
                return False
            
            # Check memo cache
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            
            # Try including current element
            include = solve(index + 1, remaining - arr[index])
            
            # Try excluding current element
            exclude = solve(index + 1, remaining)
            
            # Cache and return
            result = include or exclude
            memo[(index, remaining)] = result
            return result
        
        return solve(0, target)
```

**When to Use Memoization vs Tabulation:**

**Use Memoization When:**
- ✅ Recursive thinking is more natural
- ✅ Not all states needed (sparse computation)
- ✅ Want to maintain recursion structure

**Use Tabulation When:**
- ✅ Need all states anyway
- ✅ Want to avoid recursion overhead
- ✅ Easier to optimize space (1D array)
- ✅ Better cache locality

---

### Space Optimization (1D Array)

```python
def isSubsetSum_SpaceOptimized(arr, target):
    # Only need previous row, not entire table!
    dp = [False] * (target + 1)
    dp[0] = True  # Base case
    
    # Process each element
    for num in arr:
        # Traverse right to left (important!)
        for t in range(target, num - 1, -1):
            if dp[t - num]:
                dp[t] = True
    
    return dp[target]
```

**Why Right to Left?**
- Prevents using updated values in same iteration
- Each element should be used only once per row
- Left to right would allow multiple uses

**Space Complexity:**
- Original: O(n × target)
- Optimized: O(target) ✅

---

### Complexity Summary

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(2^n) | O(n) | Too slow, try all subsets |
| Memoization | O(n × T) | O(n × T) | Top-down, recursion stack |
| Tabulation | O(n × T) | O(n × T) | Bottom-up, iterative |
| Space Optimized | O(n × T) | O(T) | 1D array, best space |

---

## 🔄 Pattern Comparison

### Backtracking vs DP Decision Matrix

| Factor | Backtracking | Dynamic Programming |
|--------|--------------|---------------------|
| **Output Type** | ALL solutions | ONE solution/answer |
| **Overlapping?** | No | Yes |
| **Optimization** | None possible | Memoization/Tabulation |
| **Time** | Often exponential | Often polynomial |
| **Example** | Letter Combinations | Subset Sum |
| **When to use** | Generate everything | Find optimal/valid |

### Include/Exclude Pattern

**Both problems use this pattern:**

```python
# At each element, we have 2 choices:

# Choice 1: Include current element
result_include = solve(next_state_with_element)

# Choice 2: Exclude current element  
result_exclude = solve(next_state_without_element)

# Combine results
final_result = combine(result_include, result_exclude)
```

**Letter Combinations:**
- "Include" = pick this letter
- "Exclude" = skip to next letter
- Combine = try all possibilities

**Subset Sum:**
- "Include" = add to sum
- "Exclude" = don't add to sum
- Combine = OR (either path works)

---

## 💡 Key Takeaways

### Must Remember Points

1. **Backtracking** = Generate ALL, no optimization possible
2. **DP** = Find ONE/optimal, use memoization when overlapping exists
3. **Strings are immutable** = No explicit unchoose needed in Python
4. **Include/Exclude** is a universal recursive pattern
5. **Tabulation** avoids recursion stack issues
6. **Space can often be optimized** from 2D to 1D

### Problem Recognition

**Use Backtracking when you see:**
- "Find all..."
- "Generate all..."
- "List all combinations/permutations..."

**Use DP when you see:**
- "Is it possible to..."
- "Maximum/Minimum..."
- "Count number of ways..."
- Same subproblems computed multiple times

---

## 📝 Practice Problems

### Backtracking Practice
1. **Permutations** (LeetCode 46)
2. **Combination Sum** (LeetCode 39)
3. **Generate Parentheses** (LeetCode 22)
4. **Palindrome Partitioning** (LeetCode 131)

### DP Practice
1. **Coin Change** (LeetCode 322)
2. **Partition Equal Subset Sum** (LeetCode 416)
3. **0/1 Knapsack** (Classic)
4. **Longest Common Subsequence** (LeetCode 1143)

---

## 🎯 Interview Tips

### For Letter Combinations

**What interviewers look for:**
- ✅ Handle edge cases (empty string)
- ✅ Efficient mapping structure (dict)
- ✅ Clean recursive implementation
- ✅ Understand why no unchoose needed
- ✅ Explain time/space complexity

**Common follow-ups:**
- "How would you do this iteratively?"
- "What if some digits have no letters?"
- "Can you optimize space further?"

### For Subset Sum

**What interviewers look for:**
- ✅ Start with brute force, then optimize
- ✅ Explain overlapping subproblems
- ✅ Implement both memoization and tabulation
- ✅ Discuss space optimization
- ✅ Handle edge cases (empty array, zero target)

**Common follow-ups:**
- "How would you print the actual subset?"
- "What if we need count of subsets, not just yes/no?"
- "Can you do this in O(target) space?"

---

## 🔧 Debugging Checklist

### Letter Combinations
- [ ] Empty input returns empty list (not [""])
- [ ] Only digits 2-9 in phone_map
- [ ] Base case checks `index == len(digits)`
- [ ] Each digit processed exactly once
- [ ] No off-by-one errors

### Subset Sum
- [ ] Base case: remaining == 0 returns True
- [ ] Base case: negative remaining returns False
- [ ] Table dimensions correct: (n+1) × (target+1)
- [ ] First column (sum=0) all True
- [ ] Array indexing: dp[i] uses arr[i-1]
- [ ] Include check: `arr[i-1] <= t` before accessing

---

## 📊 Time Complexity Cheat Sheet

```
Letter Combinations:
├─ Best/Worst/Average: O(4^n × n)
├─ Space: O(n) recursion depth
└─ Note: Must generate all, can't optimize

Subset Sum:
├─ Brute Force: O(2^n) time, O(n) space
├─ Memoization: O(n × target) time, O(n × target) space
├─ Tabulation: O(n × target) time, O(n × target) space
└─ Optimized: O(n × target) time, O(target) space ✅
```

---

## 🎓 Further Reading

### Recommended Resources
1. **Dynamic Programming Patterns** - GeeksforGeeks
2. **Backtracking Algorithm** - Wikipedia
3. **LeetCode Discuss** - Pattern recognition threads
4. **CLRS Chapter 15** - Dynamic Programming fundamentals

### Related Topics
- Knapsack variants (0/1, unbounded, fractional)
- State space tree exploration
- Memoization vs Tabulation trade-offs
- Space-time complexity optimization

---

**End of Detailed Notes**

*These notes cover everything you need to master Day 48 concepts. Copy directly to Notion for structured learning!*
