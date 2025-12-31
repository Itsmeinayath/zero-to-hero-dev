# House Robber Problem

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this street are arranged in a line, and adjacent houses have security systems connected. **It will automatically contact the police if two adjacent houses were broken into on the same night.**

Given an integer array `nums` representing the amount of money in each house, return the **maximum amount of money you can rob tonight without alerting the police**.

---

## Examples

### Example 1:
```
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount = 1 + 3 = 4.
```

### Example 2:
```
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount = 2 + 9 + 1 = 12.
```

### Example 3:
```
Input: nums = [5, 3, 4, 11, 2]
Output: 16
Explanation: Rob house 1 (money = 5) and rob house 4 (money = 11).
             Total amount = 5 + 11 = 16.
```

---

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

---

## Approaches

### Approach 1: Recursion (Brute Force)

#### Intuition
At each house, we have two choices:
1. **Rob this house**: Add current money + max money from houses starting at `i+2`
2. **Skip this house**: Take max money from houses starting at `i+1`

#### Time Complexity: O(2^n)
#### Space Complexity: O(n) - recursion stack

```python
def rob_recursive(nums):
    def helper(i):
        # Base case: no houses left
        if i >= len(nums):
            return 0
        
        # Choice 1: Rob current house
        rob_current = nums[i] + helper(i + 2)
        
        # Choice 2: Skip current house
        skip_current = helper(i + 1)
        
        # Return maximum of both choices
        return max(rob_current, skip_current)
    
    return helper(0)

# Test
print(rob_recursive([1, 2, 3, 1]))  # Output: 4
print(rob_recursive([2, 7, 9, 3, 1]))  # Output: 12
```

---

### Approach 2: Memoization (Top-Down DP)

#### Intuition
The recursive solution has overlapping subproblems. We can cache the results to avoid redundant calculations.

#### Time Complexity: O(n)
#### Space Complexity: O(n)

```python
def rob_memoization(nums):
    memo = {}
    
    def helper(i):
        # Base case
        if i >= len(nums):
            return 0
        
        # Check if already computed
        if i in memo:
            return memo[i]
        
        # Calculate and store in memo
        rob_current = nums[i] + helper(i + 2)
        skip_current = helper(i + 1)
        
        memo[i] = max(rob_current, skip_current)
        return memo[i]
    
    return helper(0)

# Test
print(rob_memoization([1, 2, 3, 1]))  # Output: 4
print(rob_memoization([2, 7, 9, 3, 1]))  # Output: 12
```

---

### Approach 3: Tabulation (Bottom-Up DP)

#### Intuition
Build the solution from bottom-up using an array where `dp[i]` represents the maximum money that can be robbed from houses `0` to `i`.

**Recurrence Relation:**
```
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

#### Time Complexity: O(n)
#### Space Complexity: O(n)

```python
def rob_tabulation(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    
    # Base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Fill the dp array
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    return dp[n-1]

# Test
print(rob_tabulation([1, 2, 3, 1]))  # Output: 4
print(rob_tabulation([2, 7, 9, 3, 1]))  # Output: 12
```

---

### Approach 4: Space Optimized (Optimal Solution)

#### Intuition
We only need the last two values from the DP array, so we can optimize space by using two variables instead of an array.

#### Time Complexity: O(n)
#### Space Complexity: O(1)

```python
def rob_optimized(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]  # dp[i-2]
    prev1 = max(nums[0], nums[1])  # dp[i-1]
    
    for i in range(2, len(nums)):
        current = max(prev1, nums[i] + prev2)
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test
print(rob_optimized([1, 2, 3, 1]))  # Output: 4
print(rob_optimized([2, 7, 9, 3, 1]))  # Output: 12
print(rob_optimized([5, 3, 4, 11, 2]))  # Output: 16
```

---

## Dry Run Example

Let's trace through `nums = [2, 7, 9, 3, 1]` using tabulation:

| Index | nums[i] | dp[i-2] | nums[i] + dp[i-2] | dp[i-1] | dp[i] = max(dp[i-1], nums[i] + dp[i-2]) |
|-------|---------|---------|-------------------|---------|------------------------------------------|
| 0     | 2       | -       | -                 | -       | 2                                        |
| 1     | 7       | -       | -                 | 2       | max(2, 7) = 7                            |
| 2     | 9       | 2       | 9 + 2 = 11        | 7       | max(7, 11) = 11                          |
| 3     | 3       | 7       | 3 + 7 = 10        | 11      | max(11, 10) = 11                         |
| 4     | 1       | 11      | 1 + 11 = 12       | 11      | max(11, 12) = 12                         |

**Result: 12**

---

## Key Insights

1. **Choice at each step**: Rob current house or skip it
2. **Constraint**: Cannot rob two adjacent houses
3. **Optimal Substructure**: Solution depends on solutions to smaller subproblems
4. **Overlapping Subproblems**: Same subproblems are solved multiple times in recursion

---

## Decision Tree Visualization

For `nums = [2, 7, 9, 3, 1]`:

```
                    rob(0)
                   /      \
              2+rob(2)    rob(1)
               /    \      /    \
          2+9+rob(4) 2+rob(3) 7+rob(3) rob(2)
            /   \     /   \    /   \    /   \
         ...   ...  ...  ... ...  ... ...  ...
```

---

## Practice Problems

1. **House Robber II** - Houses arranged in a circle
2. **House Robber III** - Houses arranged in a binary tree
3. **Delete and Earn** - Similar concept with different constraints

---

## Complete Test Code

```python
def house_robber_all_approaches():
    # Test cases
    test_cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [5, 3, 4, 11, 2],
        [2, 1, 1, 2],
        [5],
        [1, 3, 1, 3, 100]
    ]
    
    approaches = {
        "Memoization": rob_memoization,
        "Tabulation": rob_tabulation,
        "Optimized": rob_optimized
    }
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test}")
        for name, func in approaches.items():
            result = func(test)
            print(f"  {name}: {result}")

# Run all tests
house_robber_all_approaches()
```

---

## Summary

| Approach      | Time Complexity | Space Complexity | Best For          |
|---------------|----------------|------------------|-------------------|
| Recursion     | O(2^n)         | O(n)             | Understanding     |
| Memoization   | O(n)           | O(n)             | Top-down thinking |
| Tabulation    | O(n)           | O(n)             | Bottom-up DP      |
| Optimized     | O(n)           | O(1)             | **Production**    |

**Recommended Solution: Space Optimized O(n) time, O(1) space**
