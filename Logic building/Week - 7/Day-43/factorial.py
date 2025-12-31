# Here we are solving the factorial of a number using recursion
# First lets understand what is factorial
# Factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# It is denoted by n! and is defined as:
#  factorial means n! = n × (n - 1) × (n - 2) × ... × 1
# For example, 5! = 5 × 4 × 3 × 2 × 1 = 120
#  here the n = 5  , 5! = 5(5-1)! = 5 * 4! , 4! = 4(4-1)! = 4 * 3! , 3! = 3(3-1)! = 3 * 2! , 2! = 2(2-1)! = 2 * 1! , 1! = 1(1-1)! = 1 * 0! , and we know that 0! = 1

class Solution:
    def factorial(self, n:int) -> int:

        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
        
# Example usage:
solution = Solution()
number = 5
result = solution.factorial(number)
print(f"The factorial of {number} is {result}")
