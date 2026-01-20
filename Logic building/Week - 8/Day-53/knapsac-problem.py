class Solution:
    # Function knapSack(W, wt, val, n):
    def knapSack(self, W, wt, val, n):
        
        # 1. Create a 2D table 'dp'
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # 2. Outer Loop: Iterate 'i' from 1 to n
        for i in range(1, n + 1):
            # 3. Inner Loop: Iterate 'w' from 1 to W
            for w in range(1, W + 1):
                
                # 4. The Logic Check:
                # Choice A: Can I fit this item?
                if wt[i-1] <= w:
                    # Logic: Max of (Picking it vs. Skipping it)
                    pick = val[i-1] + dp[i-1][w - wt[i-1]]
                    skip = dp[i-1][w]
                    dp[i][w] = max(pick, skip)
                    if w == W:  # Print only for the final weight capacity
                        choice = "PICK" if pick >= skip else "SKIP"
                        print(f"Item {i}: wt={wt[i-1]}, val={val[i-1]} | Pick={pick}, Skip={skip} | Choice: {choice}")
                else:
                    # Choice B: I CANNOT fit this item. I must skip it.
                    # Copy value from the row above.
                    dp[i][w] = dp[i-1][w]
                    if w == W:  # Print only for the final weight capacity
                        print(f"Item {i}: wt={wt[i-1]}, val={val[i-1]} | Too heavy (wt > {W}) | Choice: SKIP")
        
        # 5. Return dp[n][W] (OUTSIDE the loops)
        print(f"\nFinal Maximum Value: {dp[n][W]}\n")
        return dp[n][W]
    

# Test Cases

def test_knapSack():
    sol = Solution()
    
    # Test Case 1
    W1 = 50
    wt1 = [10, 20, 30]
    val1 = [60, 100, 120]
    n1 = len(val1)
    assert sol.knapSack(W1, wt1, val1, n1) == 220

    # Test Case 2
    W2 = 10
    wt2 = [5, 4, 6, 3]
    val2 = [10, 40, 30, 50]
    n2 = len(val2)
    assert sol.knapSack(W2, wt2, val2, n2) == 90

    # Test Case 3
    W3 = 0
    wt3 = [1, 2, 3]
    val3 = [10, 20, 30]
    n3 = len(val3)
    assert sol.knapSack(W3, wt3, val3, n3) == 0

    print("All test cases pass")

test_knapSack()