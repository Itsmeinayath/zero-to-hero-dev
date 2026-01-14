# 💰 Day 52: Coin Change - Unbounded Knapsack

## 🎯 The Core Concept

**Unbounded Knapsack** = Each item can be used **unlimited times**

```
Making $11 with coins [$1, $2, $5]

┌─────────────────────────────────┐
│  Can I use $5 coin? YES         │
│  ├─ Use it → Need $6 more       │
│  │  Can I use $5 again? YES!    │
│  │  ├─ Use it → Need $1 more    │
│  │  │  Use $1 → DONE! ✓         │
│  │  Result: $5 + $5 + $1 = 3 coins
└─────────────────────────────────┘
```

**Key Difference:**
- **0/1 Knapsack:** Use each item ONCE (House Robber)
- **Unbounded:** Use each item UNLIMITED times (Coin Change)

---

## 📋 Problem: Coin Change (LeetCode 322)

**Given:**
- `coins[]` = coin denominations
- `amount` = target sum

**Find:** Fewest coins needed to make the amount (return `-1` if impossible)

**Examples:**

| Input | Output | Explanation |
|-------|--------|-------------|
| `coins=[1,2,5], amount=11` | `3` | 5+5+1 |
| `coins=[2], amount=3` | `-1` | Impossible |
| `coins=[1], amount=0` | `0` | No coins needed |

---

## 1️⃣ Coin Change (LeetCode 322)

### 🎯 Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount. If that amount cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an **infinite number** of each kind of coin.

**Examples:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: Cannot make 3 with only 2-denomination coins

Input: coins = [1], amount = 0
Output: 0
Explanation: 0 coins needed to make amount 0
```

---

## 💡 Approach Evolution

### ❌ Approach 1: Brute Force Recursion

**Logic:** Try every coin at every step and recurse.

```python
def coinChange_recursive(coins, amount):
    def helper(remaining):
        # Base cases
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        
        # Try every coin
        min_coins = float('inf')
        for coin in coins:
            result = helper(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        return min_coins
    
    result = helper(amount)
    return result if result != float('inf') else -1
```

**Complexity:**
- **Time:** O(amount^n) - Exponential! Each call branches n times
- **Space:** O(amount) - Recursion depth

**Problem:** Massive duplication. For `amount=11, coins=[1,2,5]`, we calculate `helper(6)` multiple times.

---

### ✅ Approach 2: Memoization (Top-Down DP)

**Logic:** Add a cache to remember results.

```python
def coinChange_memoization(coins, amount):
    memo = {}
    
    def helper(remaining):
        # Check cache first
        if remaining in memo:
            return memo[remaining]
        
        # Base cases
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        
        # Try every coin
        min_coins = float('inf')
        for coin in coins:
            result = helper(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        # Cache the result
        memo[remaining] = min_coins
        return min_coins
    
    result = helper(amount)
    return result if result != float('inf') else -1
```

**Complexity:**
- **Time:** O(amount × n) - Each subproblem solved once
- **Space:** O(amount) - Memo dict + recursion stack

**Improvement:** Eliminates duplicate work!

---

### ⭐ Approach 3: Tabulation (Bottom-Up DP) - OPTIMAL

**Logic:** Build solution from 0 to amount iteratively.

```python
def coinChange(coins, amount):
    # dp[i] = minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins needed for amount 0
    dp[0] = 0
    
    # Build table for each amount from 1 to target
    for i in range(1, amount + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:  # Can use this coin
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result
    return dp[amount] if dp[amount] != float('inf') else -1
```

**Complexity:**
- **Time:** O(amount × n) - Two nested loops
- **Space:** O(amount) - DP array only (no recursion!)

**Why Optimal:** Cleaner logic, no recursion overhead, easier to debug.

---

## 🔍 Step-by-Step Walkthrough

### Example: coins = [1, 2, 5], amount = 11

**DP Table Construction:**

| Amount | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|--------|---|---|---|---|---|---|---|---|---|---|----|----|
| Initial | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| After coin=1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| After coin=2 | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 |
| After coin=5 | 0 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2 | **3** |

**Detailed Trace for amount=11:**

1. **Coin = 1:**
   - `dp[11] = min(∞, dp[10] + 1) = min(∞, 10 + 1) = 11`

2. **Coin = 2:**
   - `dp[11] = min(11, dp[9] + 1) = min(11, 5 + 1) = 6`

3. **Coin = 5:**
   - `dp[11] = min(6, dp[6] + 1) = min(6, 2 + 1) = 3` ✅

**Answer:** 3 coins (5 + 5 + 1)

---

## 🎨 Visual: Why dp[i - coin] + 1?

```
Making amount 7 with coins [1,2,5]:

Decision Tree:
                amount = 7
         ┌─────────┼─────────┐
      use $1    use $2    use $5
         ↓         ↓         ↓
    need $6    need $5    need $2
  (6 coins)   (1 coin)   (1 coin)
      
dp[7] = min(
  dp[6] + 1 = 3 + 1 = 4  ← Use $1 coin
  dp[5] + 1 = 1 + 1 = 2  ← Use $2 coin ✓
  dp[2] + 1 = 1 + 1 = 2  ← Use $5 coin ✓
)

Result: 2 coins
Path 1: $5 + $2 = $7 ✓
Path 2: $2 + $2 + $2 + $1 = $7 (but uses 4 coins)
```

**Formula Breakdown:**
```
dp[i - coin] + 1
    ↑          ↑
    │          └─ The coin we just used
    │
    └─ Minimum coins needed for remaining amount
```

---

## 🎨 Pseudocode Template

```
function coinChange(coins, amount):
    // Step 1: Initialize DP table
    dp = array of size (amount + 1)
    fill dp with infinity
    dp[0] = 0  // Base case
    
    // Step 2: Build table for each amount
    for i from 1 to amount:
        for each coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    // Step 3: Return result
    if dp[amount] == infinity:
        return -1  // Cannot make this amount
    else:
        return dp[amount]
```

---

## 🛑 Common Pitfalls

### 1. Wrong Initialization
❌ **Wrong:**
```python
dp = [0] * (amount + 1)  # All zeros!
```

✅ **Correct:**
```python
dp = [float('inf')] * (amount + 1)
dp[0] = 0  # Only base case is 0
```

**Why?** We're looking for minimum. If initialized to 0, `min(0, anything) = 0` always!

---

### 2. Forgetting Boundary Check
❌ **Wrong:**
```python
for coin in coins:
    dp[i] = min(dp[i], dp[i - coin] + 1)  # What if coin > i?
```

✅ **Correct:**
```python
for coin in coins:
    if coin <= i:  # Check first!
        dp[i] = min(dp[i], dp[i - coin] + 1)
```

---

### 3. Wrong Return Condition
❌ **Wrong:**
```python
return dp[amount]  # Returns infinity if impossible!
```

✅ **Correct:**
```python
return dp[amount] if dp[amount] != float('inf') else -1
```

---

### 4. Off-by-One in Array Size
❌ **Wrong:**
```python
dp = [float('inf')] * amount  # Missing amount itself!
```

✅ **Correct:**
```python
dp = [float('inf')] * (amount + 1)  # Need indices 0 to amount
```

---

## 🎯 Logic Exercise: Trace Yourself!

**Given:** `coins = [1, 2, 5], amount = 11`

Fill in this table by hand:

| Amount | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|--------|---|---|---|---|---|---|---|---|---|---|----|----|
| dp[i] | 0 | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |

**Process:**
1. For each amount i (1 to 11)
2. For each coin (1, 2, 5)
3. If coin ≤ i: `dp[i] = min(dp[i], dp[i-coin] + 1)`

**Coin Selection for amount=11:**
- Could use: 11×1 = 11 coins
- Could use: 5+2+2+2 = 4 coins
- **Best:** 5+5+1 = 3 coins ✅

---

## 2️⃣ Practice Problem: Minimum Coins (GFG)

### Problem Variation

**Same concept, different presentation:**
- Given denominations: `V = [25, 10, 5]`
- Make amount: `amount = 30`
- Find: Minimum coins needed

**Solution using same template:**

```python
def minCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example
V = [25, 10, 5]
amount = 30
print(minCoins(V, amount))  # Output: 2 (25 + 5)
```

**E🎯 The Unbounded Knapsack Template

```python
def unbounded_knapsack_pattern(items, target):
    """
    Universal template for unbounded knapsack problems
    """
    # Initialize: Use infinity for MIN problems, 0 for MAX problems
    dp = [float('inf')] * (target + 1)  # or [0] for maximization
    dp[0] = 0  # Base case
    
    # For each target value
    for i in range(1, target + 1):
        # Try each item (can reuse unlimited times)
        for item in items:
            if item <= i:
                dp[i] = min(dp[i], dp[i - item] + 1)  # or max() for maximization
    
    return dp[target] if dp[target] != float('inf') else -1
```

**Visual: Loop Structure**
```
amount →  1    2    3    4    5    6   ...  11
         ───────────────────────────────────────
coin=$1  │ dp[1]=min(all coin choices)
coin=$2  │      dp[2]=min(all coin choices)
coin=$5  │           dp[3]=min(all coin choices)
         │                ...
                                    dp[11]=answer
```

---

## 📊 Key Patterns Summary

| Aspect | Detail |
|--------|--------|
| **Pattern** | Unbounded Knapsack (unlimited reuse) |
| **Recurrence** | `dp[i] = min(dp[i], dp[i-coin] + 1)` for all coins |
| **Time** | O(amount × n) where n = number of coins |
| **Space** | O(amount) |
| **Initialization** | `dp[0]=0`, rest `infinity` |
| **Loop Order** | Outer: amounts, Inner: coins |

---

## 📚 Resources

**Watch (20 min):**
- [Tushar Roy - Coin Change](https://www.youtube.com/watch?v=Y0ZqKpToTic)

**Read (20 min):**
- [GeeksforGeeks - Coin Change](https://www.geeksforgeeks.org/coin-change-dp-7/)

**Practice More:**
- LeetCode 518: Coin Change II (count combinations)
- LeetCode 983: Minimum Cost For Tickets

---


