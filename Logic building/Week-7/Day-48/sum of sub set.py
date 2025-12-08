class Solution:
    def get_subset(self, arr, target):
        n = len(arr)
        # 1. Build the DP Table (Same as your code)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        # Base Case: Sum 0 is possible with empty set
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        # If no subset exists, return None
        if not dp[n][target]:
            return None

        # 2. Reverse Trace to find the numbers
        subset = []
        i = n
        current_sum = target

        while i > 0 and current_sum > 0:
            # Check the value in the row ABOVE
            if dp[i-1][current_sum] == True:
                # If the value above is True, we EXCLUDED this number
                # Just move up
                i -= 1
            else:
                # If the value above is False, we INCLUDED this number
                # 1. Add number to our list
                subset.append(arr[i-1])
                # 2. Subtract value from current_sum
                current_sum -= arr[i-1]
                # 3. Move up
                i -= 1
        
        return subset

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    result_subset = solution.get_subset(arr, target)
    if result_subset:
        print(f"Target {target} found with subset: {result_subset}")
    else:
        print(f"No subset sums to {target}")
    
    arr = [5, 10, 12, 13, 15, 18]
    target = 30
    result_subset = solution.get_subset(arr, target)
  
    if result_subset:
        print(f"Target {target} found with subset: {result_subset}")
    else:
        print(f"No subset sums to {target}")