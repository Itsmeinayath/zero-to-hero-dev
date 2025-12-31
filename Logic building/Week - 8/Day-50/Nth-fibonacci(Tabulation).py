
def nth_fibonacci(n):
    if n <= 1 or n == 0:
        return n
    
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n ]

# Example usage:
n = 10
print(f"The {n}th Fibonacci number is: {nth_fibonacci(n)}")


#   using only variables
def nth_fibonacci_optimized(n):
    if n <= 1 
        return n
    prev2, prev1 = 0, 1

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
