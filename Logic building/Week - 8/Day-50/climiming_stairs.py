# Initialize a "memo" dictionary or array to store results.
memo ={}
# Function climb(n, memo):
def climing_stairs(n,memo):
# 1. Base Case: If n <= 1, return 1.
    if n <= 1:
        return 1
# 2. Check Memory: If n is already in 'memo', return memo[n]. (Don't re-calculate!)
    if n in memo :
        return memo[n]
# 3. Recursive Step:
    result = climing_stairs(n-1, memo) + climing_stairs(n-2, memo)
#    - Result = climb(n-1) + climb(n-2)
# 4. Store Result: Save 'Result' into memo[n].
    memo[n] = result


# 5. Return Result.
    return result