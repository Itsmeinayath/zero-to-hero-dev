# Day 53: Partition Equal Subset Sum (LeetCode 416)

## 📌 Problem Statement

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.

**LeetCode Link:** [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

---

## 📝 Examples

### Example 1:
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

### Example 2:
```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

---

## 🎯 Key Insights

### 1. **Problem Transformation**
This problem can be transformed into a **Subset Sum Problem**:
- If total sum is **odd**, we can't partition into equal subsets → return `false`
- If total sum is **even**, we need to find if there exists a subset with sum = `total_sum / 2`

### 2. **Why This Works**
If we can find a subset with sum = `total_sum / 2`, then:
- Subset A has sum = `total_sum / 2`
- Remaining elements (Subset B) also have sum = `total_sum / 2`
- Therefore, both subsets are equal!

### 3. **This is a 0/1 Knapsack Variant**
For each number, we have two choices:
- Include it in the subset
- Exclude it from the subset

---

## 💡 Approaches

### Approach 1: Dynamic Programming (1D Array) ⭐ **Most Efficient**

```python
def canPartition(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # sum 0 is always achievable
    
    for num in nums:
        # Traverse from right to left
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]
```

**Time Complexity:** O(n × sum/2)  
**Space Complexity:** O(sum/2)

**Why traverse from right to left?**
- To avoid using the same element twice in a single iteration
- If we go left to right, `dp[i]` might use the same element multiple times

---

### Approach 2: Dynamic Programming (2D Array) - More Intuitive

```python
def canPartition2D(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # dp[i][j] = can we achieve sum j using first i elements
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: sum 0 is always achievable
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(target + 1):
            # Don't include current number
            dp[i][j] = dp[i-1][j]
            
            # Include current number if possible
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
    
    return dp[n][target]
```

**Time Complexity:** O(n × sum/2)  
**Space Complexity:** O(n × sum/2)

---

### Approach 3: Recursion with Memoization

```python
def canPartitionMemo(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    memo = {}
    
    def dfs(index, current_sum):
        if current_sum == 0:
            return True
        if current_sum < 0 or index >= len(nums):
            return False
        
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]
        
        include = dfs(index + 1, current_sum - nums[index])
        exclude = dfs(index + 1, current_sum)
        
        memo[(index, current_sum)] = include or exclude
        return memo[(index, current_sum)]
    
    return dfs(0, target)
```

**Time Complexity:** O(n × sum/2)  
**Space Complexity:** O(n × sum/2) + recursion stack

---

## 🔍 Visual Example

**Input:** `nums = [1, 5, 11, 5]`

```
Total Sum = 22
Target = 11

Step-by-step DP array (1D approach):

Initial: dp = [True, False, False, False, False, False, False, False, False, False, False, False]
                  0     1      2      3      4      5      6      7      8      9     10     11

After num=1:  dp = [True, True, False, False, False, False, False, False, False, False, False, False]
                    ↑     ↑ (0+1)

After num=5:  dp = [True, True, False, False, False, True, True, False, False, False, False, False]
                    ↑     ↑                           ↑(0+5) ↑(1+5)

After num=11: dp = [True, True, False, False, False, True, True, False, False, False, False, True]
                    ↑     ↑                           ↑      ↑                                ↑(0+11)

After num=5:  dp = [True, True, False, False, False, True, True, False, False, False, True, True]
                    ↑     ↑                           ↑      ↑                         ↑(5+5) ↑(6+5)

Result: dp[11] = True ✅
```

---

## 🎨 Pattern Recognition

This problem belongs to:
- **0/1 Knapsack Pattern**
- **Subset Sum Problem**
- **Dynamic Programming**

**Similar Problems:**
- LeetCode 494: Target Sum
- LeetCode 698: Partition to K Equal Sum Subsets
- LeetCode 1049: Last Stone Weight II

---

## ⚡ Optimization Tips

1. **Early Exit:** If sum is odd, immediately return false
2. **Space Optimization:** Use 1D DP instead of 2D
3. **Right-to-Left Traversal:** Prevents using same element twice
4. **Target Pruning:** If target > remaining sum, early exit

---

## 🧪 Test Results

```
Test 1: nums = [1, 5, 11, 5]
Output: True
Explanation: [1, 5, 5] and [11] both sum to 11

Test 2: nums = [1, 2, 3, 5]
Output: False
Explanation: Cannot partition into equal sum subsets

Test 3: nums = [1, 2, 5]
Output: False

Test 4: nums = [1]
Output: False

Test 5: nums = [2, 2, 2, 2]
Output: True
Explanation: [2, 2] and [2, 2] both sum to 4
```

---

## 📚 Learning Points

1. **Problem Transformation:** Converting a partition problem into subset sum
2. **DP State Design:** `dp[i]` represents whether sum `i` is achievable
3. **Space Optimization:** 2D → 1D array optimization
4. **Traversal Direction:** Right-to-left to avoid duplicate usage
5. **Base Case:** Sum 0 is always achievable (empty subset)

---

## 🚀 Complexity Summary

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| 1D DP | O(n × sum/2) | O(sum/2) | **Production** ⭐ |
| 2D DP | O(n × sum/2) | O(n × sum/2) | **Learning** |
| Memoization | O(n × sum/2) | O(n × sum/2) | **Understanding** |

---

**Completed on:** January 19, 2026  
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, 0/1 Knapsack