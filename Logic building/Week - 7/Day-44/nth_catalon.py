memo = {}

def catalon(n):
    if n in memo:
     return memo[n]
    if n == 0 or n == 1:
        return 1
    
    result = 0

    for i in range(n):
        result = result + (catalon(i) * catalon(n - 1 - i))

    memo[n] = result
    return result