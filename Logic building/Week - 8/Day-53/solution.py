"""
Day 53: Partition Equal Subset Sum (LeetCode 416)

Problem: Given an integer array nums, return true if you can partition the array 
into two subsets such that the sum of the elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

class Solution:
    # Approach 1: Dynamic Programming (Tabulation) - Most Efficient
    def canPartition(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n * sum/2) where n is length of nums
        Space Complexity: O(sum/2)
        
        Key Insight: If we can partition into two equal subsets, then:
        1. Total sum must be even (otherwise can't divide equally)
        2. We need to find if there's a subset with sum = total_sum / 2
        3. This becomes a 0/1 Knapsack problem
        """
        total_sum = sum(nums)
        
        # If sum is odd, we can't partition into equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[i] represents whether sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True  # sum 0 is always achievable (empty subset)
        
        # For each number in nums
        for num in nums:
            # Traverse from right to left to avoid using same element twice
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
    
    # Approach 2: Dynamic Programming with 2D Array (More Intuitive)
    def canPartition2D(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n * sum/2)
        Space Complexity: O(n * sum/2)
        
        2D DP approach for better understanding
        """
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
    
    # Approach 3: Recursion with Memoization (Top-Down)
    def canPartitionMemo(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n * sum/2)
        Space Complexity: O(n * sum/2) for memo + recursion stack
        """
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        memo = {}
        
        def dfs(index: int, current_sum: int) -> bool:
            # Base cases
            if current_sum == 0:
                return True
            if current_sum < 0 or index >= len(nums):
                return False
            
            # Check memo
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Try including or excluding current number
            include = dfs(index + 1, current_sum - nums[index])
            exclude = dfs(index + 1, current_sum)
            
            memo[(index, current_sum)] = include or exclude
            return memo[(index, current_sum)]
        
        return dfs(0, target)


# Test Cases
def test_partition_equal_subset_sum():
    sol = Solution()
    
    # Test Case 1
    nums1 = [1, 5, 11, 5]
    print(f"Test 1: nums = {nums1}")
    print(f"Output: {sol.canPartition(nums1)}")  # Expected: True
    print(f"Explanation: [1, 5, 5] and [11] both sum to 11\n")
    
    # Test Case 2
    nums2 = [1, 2, 3, 5]
    print(f"Test 2: nums = {nums2}")
    print(f"Output: {sol.canPartition(nums2)}")  # Expected: False
    print(f"Explanation: Cannot partition into equal sum subsets\n")
    
    # Test Case 3
    nums3 = [1, 2, 5]
    print(f"Test 3: nums = {nums3}")
    print(f"Output: {sol.canPartition(nums3)}")  # Expected: False
    print()
    
    # Test Case 4 - Edge case: single element
    nums4 = [1]
    print(f"Test 4: nums = {nums4}")
    print(f"Output: {sol.canPartition(nums4)}")  # Expected: False
    print()
    
    # Test Case 5 - All same numbers
    nums5 = [2, 2, 2, 2]
    print(f"Test 5: nums = {nums5}")
    print(f"Output: {sol.canPartition(nums5)}")  # Expected: True
    print(f"Explanation: [2, 2] and [2, 2] both sum to 4\n")
    
    # Test Case 6 - Large numbers
    nums6 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    print(f"Test 6: Large array with same numbers")
    print(f"Output: {sol.canPartition(nums6)}")  # Expected: True
    print()
    
    # Test Case 7 - Compare all approaches
    nums7 = [1, 5, 11, 5]
    print(f"Test 7: Comparing all approaches with nums = {nums7}")
    print(f"Approach 1 (1D DP): {sol.canPartition(nums7)}")
    print(f"Approach 2 (2D DP): {sol.canPartition2D(nums7)}")
    print(f"Approach 3 (Memoization): {sol.canPartitionMemo(nums7)}")


if __name__ == "__main__":
    test_partition_equal_subset_sum()
