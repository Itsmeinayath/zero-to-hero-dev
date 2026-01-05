# 1. Handle edge case: If nums is empty, return 0. 
#    If len(nums) == 1, return nums[0].
# 2. Create a 'dp' array of size n.
# 3. Seed the Base Cases:
#    - dp[0] = nums[0]
#    - dp[1] = max(nums[0], nums[1])
# 4. Loop from index 2 to n-1:
#    - dp[i] = max( taking current + i-2,  skipping current (taking i-1) )
# 5. Return the last element of dp.

class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2 , len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
    
# example usage:
solution = Solution()
print(solution.rob([1,2,3,1]))  # Output: 4
# 1. Handle edge case: If nums is empty, return 0.
print(solution.rob([2,7,9,3,1]))  # Output: 12
# which elements to rob to get the maximum amount without alerting the police.
print(solution.rob([]))
    # Output: 0
print(solution.rob([1]))
