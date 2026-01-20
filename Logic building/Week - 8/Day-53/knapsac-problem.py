# Function knapSack(W, wt, val, n):

# 1. Create a 2D table 'dp' with (n + 1) rows and (W + 1) columns.
#    - Initialize all with 0.

# 2. Outer Loop: Iterate 'i' from 1 to n (For every item).
# 3. Inner Loop: Iterate 'w' from 1 to W (For every possible weight capacity).

# 4. The Logic Check:
#    - Choice A (Pick): Can I fit this item? (if wt[i-1] <= w)
#         - If yes: Value is val[i-1] + value from remaining weight (dp[i-1][w - wt[i-1]]).
#    - Choice B (Skip): Value is whatever we had with previous items (dp[i-1][w]).
#    - dp[i][w] = max(Choice A, Choice B).

# 5. Return dp[n][W].