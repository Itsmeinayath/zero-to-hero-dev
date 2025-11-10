# Here we are solving the sum of natural numbers using recursion
# the sum of the first n natural numbers is given by the formula:
# S(n) = n + (n - 1) + (n - 2) + ... + 1
# For example, the sum of the first 5 natural numbers is:
# S(5) = 5 + 4 + 3 + 2 + 1 = 15


class Solution :
    def sumOfNaturalNumbers(self,n:int) -> int:

        if n == 0:
            return 0
        else:
            return n + self.sumOfNaturalNumbers(n-1)

# Example usage:
solution = Solution()
number = 5
result = solution.sumOfNaturalNumbers(number)
print(f"The sum of the first {number} natural numbers is {result}")
