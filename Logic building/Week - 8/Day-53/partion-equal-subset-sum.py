#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        target =total_sum // 2

        dp = {0}
        for num in nums:
            temp_dp = set()
            for num_sum in dp:
                new_sum = num_sum + num
                
                if new_sum ==target:
                    return True
                if new_sum < target:
                    temp_dp.add(new_sum)
        dp.update(temp_dp)
        
# @lc code=end

