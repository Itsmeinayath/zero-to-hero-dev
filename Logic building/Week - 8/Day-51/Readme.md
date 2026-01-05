# 🏠 Day 51: 1D Dynamic Programming - Constraint Patterns
**"Zero to Hero" DSA Journey - Week 8**

## 🎯 Today's Focus
Building on Day 50's foundation, we tackle problems with **constraints** - where certain choices block other choices.

**Core Pattern:** "Include vs. Exclude" Decision Making

**Problems:**
1. House Robber (LeetCode 198) - Cannot take adjacent elements
2. Min Cost Climbing Stairs (LeetCode 746) - Cost to leave vs. arrive

---

## 📌 Quick Review: The DP Foundation

**Recurrence Relation Pattern:**
```
dp[i] = function_of(dp[i-1], dp[i-2], current_element)
```

All 1D DP problems follow this: Look back at the last 1 or 2 states to decide the current state.

---

## 1️⃣ House Robber (LeetCode 198)
**Pattern:** "Include vs. Exclude" (The Constraint Pattern)

### 🎯 Problem
You are a robber planning to rob houses along a street. Each house has a certain amount of money. **Constraint:** You cannot rob two adjacent houses (alarm system).

**Question:** What is the maximum amount you can rob?

**Example:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1) = 12
```

### 💡 The Logic

At each house `i`, you have **2 choices**:

1. **ROB this house:** Take `nums[i]` + max money from `i-2` (skip previous house)
2. **SKIP this house:** Take max money from `i-1` (take previous result)

**Recurrence Relation:**
```
dp[i] = max(nums[i] + dp[i-2], dp[i-1])
         ↑                      ↑
    Rob current house      Skip current house
    (skip previous)        (take previous max)
```

### 📊 Example Walkthrough (nums = [2,7,9,3,1])

| House | Value | Rob (i-2 + curr) | Skip (i-1) | dp[i] = max |
|-------|-------|------------------|------------|-------------|
| 0 | 2 | - | - | 2 |
| 1 | 7 | 7 | 2 | 7 |
| 2 | 9 | 2+9=11 | 7 | **11** |
| 3 | 3 | 7+3=10 | 11 | **11** |
| 4 | 1 | 11+1=12 | 11 | **12** |

**Answer:** 12

### ✅ Tabulation Solution (O(N) Space)

```python
def rob(nums):
    if not nums: 
        return 0
    if len(nums) == 1: 
        return nums[0]
    
    # Create DP table
    dp = [0] * len(nums)
    
    # Base Cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Fill table: max(rob current + i-2, skip current)
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
    return dp[-1]
```

### ⚡ Space Optimized Solution (O(1) Space)

```python
def rob_optimized(nums):
    if not nums: 
        return 0
    if len(nums) == 1: 
        return nums[0]
    
    # Only need last 2 results
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        curr = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = curr
    
    return prev1
```

**Complexity:**
* **Time:** $O(n)$ - Single pass through array
* **Space:** $O(1)$ - Only 2 variables needed

---

## 2️⃣ Min Cost Climbing Stairs (LeetCode 746)
**Pattern:** "The Troll on the Stairs" - You pay to LEAVE a step, not to arrive.

### 🎯 Problem
You are given an array `cost` where `cost[i]` is the cost of stepping on the `i`th stair. Once you pay the cost, you can climb **1 or 2 steps**.

You can start from step `0` or step `1`. **Find the minimum cost to reach the top** (beyond the last step).

**Example:**
```
Input: cost = [10,15,20]
Output: 15
Explanation: Start at index 1, pay 15, climb 2 steps to the top.
```

### 💡 The Logic

**Key Insight:** You pay the cost to LEAVE a step, not to arrive at it.

**State Definition:**
* `dp[i]` = Minimum cost to ARRIVE at step `i`

**Transition:**
To arrive at step `i`, you came from either:
* Step `i-1`: Pay `cost[i-1]` to leave `i-1` and reach `i`
* Step `i-2`: Pay `cost[i-2]` to leave `i-2` and reach `i`

**Recurrence Relation:**
```
dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
```

**Base Cases:**
* `dp[0] = 0` (start at step 0 is free)
* `dp[1] = 0` (start at step 1 is free)

### 📊 Example Walkthrough (cost = [10,15,20])

| Step | dp[i-1]+cost[i-1] | dp[i-2]+cost[i-2] | dp[i] = min |
|------|-------------------|-------------------|-------------|
| 0 | - | - | 0 (free start) |
| 1 | - | - | 0 (free start) |
| 2 | 0+15=15 | 0+10=10 | **10** |
| 3 (top) | 10+20=30 | 0+15=15 | **15** |

**Answer:** 15 (Start at 1 → Pay 15 → Reach top)

### ✅ Tabulation Solution (O(N) Space)

```python
def minCostClimbingStairs(cost):
    n = len(cost)
    
    # dp[i] = min cost to REACH step i
    dp = [0] * (n + 1)  # Size n+1 to include the "Top"
    
    # Base Cases: Starting at 0 or 1 is free
    dp[0] = 0
    dp[1] = 0
    
    # Build table: min cost to reach each step
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
    return dp[n]
```

### ⚡ Space Optimized Solution (O(1) Space)

```python
def minCostClimbingStairs_optimized(cost):
    n = len(cost)
    
    # Only need last 2 costs
    prev2 = 0  # Cost to reach 2 steps back
    prev1 = 0  # Cost to reach 1 step back
    
    for i in range(2, n + 1):
        # Calculate cost to reach current step
        curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
        
        # Shift variables for next iteration
        prev2 = prev1
        prev1 = curr
        
    return prev1
```

**Complexity:**
* **Time:** $O(n)$ - Single pass through cost array
* **Space:** $O(1)$ - Only 2 variables


## 📊 Day 51 Summary: The Constraint Pattern

| Problem | Constraint | Recurrence Relation | Complexity |
|---------|-----------|---------------------|------------|
| House Robber | Can't rob adjacent houses | `dp[i] = max(nums[i]+dp[i-2], dp[i-1])` | O(n) time, O(1) space |
| Min Cost Stairs | Must pay to leave step | `dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])` | O(n) time, O(1) space |

**Key Insight:** When there's a **constraint** (can't take adjacent, must pay cost), you're always choosing between:
- **Taking** the current element (and skipping the previous)
- **Skipping** the current element (and keeping the previous result)

---

## 🎯 The Universal DP Template

```python
def dp_problem(input_array):
    n = len(input_array)
    
    # Step 1: Handle base cases
    if not input_array:
        return 0
    
    # Step 2: Create DP table (or use variables)
    dp = [0] * (n + 1)  # Or: prev2, prev1 = base_val, base_val
    
    # Step 3: Initialize base cases
    dp[0] = base_case_0
    dp[1] = base_case_1
    
    # Step 4: Fill table using recurrence relation
    for i in range(2, n + 1):
        dp[i] = function_of(dp[i-1], dp[i-2], input_array[i])
    
    # Step 5: Return final answer
    return dp[n]
```
---
**Recurrence Evolution:**
```
Day 51: dp[i] depends on dp[i-1] and dp[i-2] (2 previous states)
Day 52: dp[i] depends on dp[i-coin1], dp[i-coin2], ... (N previous states)
