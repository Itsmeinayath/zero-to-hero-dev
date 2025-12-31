
"""
Nth Fibonacci Number - Dynamic Programming Approaches
======================================================

This module demonstrates different approaches to calculate the Nth Fibonacci number:
1. Tabulation (Bottom-Up DP) - O(n) time, O(n) space
2. Space-Optimized (Two Variables) - O(n) time, O(1) space

Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
Formula: F(n) = F(n-1) + F(n-2), where F(0) = 0, F(1) = 1
"""


def nth_fibonacci_tabulation(n):
    """
    Calculate the Nth Fibonacci number using Tabulation (Bottom-Up DP).
    
    Approach:
    - Create an array to store all Fibonacci numbers from 0 to n
    - Build the solution iteratively from bottom (F(0)) to top (F(n))
    - Each position stores the result to avoid recalculation
    
    Time Complexity: O(n) - single loop from 2 to n
    Space Complexity: O(n) - array of size n+1
    
    Args:
        n (int): The position in Fibonacci sequence (0-indexed)
    
    Returns:
        int: The Nth Fibonacci number
    
    Example:
        >>> nth_fibonacci_tabulation(10)
        55
        >>> nth_fibonacci_tabulation(0)
        0
        >>> nth_fibonacci_tabulation(1)
        1
    """
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 1:
        return n
    
    # Create DP table to store results
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    # Build table bottom-up: F(i) = F(i-1) + F(i-2)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]


def nth_fibonacci_optimized(n):
    """
    Calculate the Nth Fibonacci number using Space-Optimized approach.
    
    Approach:
    - Only keep track of the last two Fibonacci numbers
    - At each step, calculate current and shift the window
    - No need to store the entire sequence
    
    Time Complexity: O(n) - single loop from 2 to n
    Space Complexity: O(1) - only two variables
    
    Args:
        n (int): The position in Fibonacci sequence (0-indexed)
    
    Returns:
        int: The Nth Fibonacci number
    
    Example:
        >>> nth_fibonacci_optimized(10)
        55
        >>> nth_fibonacci_optimized(5)
        5
    """
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 1:
        return n
    
    # Initialize: prev2 = F(0), prev1 = F(1)
    prev2, prev1 = 0, 1
    
    # Calculate from F(2) to F(n)
    for i in range(2, n + 1):
        curr = prev1 + prev2  # F(i) = F(i-1) + F(i-2)
        prev2 = prev1         # Shift window: F(i-2) = F(i-1)
        prev1 = curr          # Shift window: F(i-1) = F(i)
    
    return prev1


def nth_fibonacci_optimized_clean(n):
    """
    Space-optimized Fibonacci using tuple unpacking (Pythonic way).
    
    Same complexity as nth_fibonacci_optimized but cleaner syntax.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    
    return prev1


def compare_approaches():
    """Demonstrate and compare both approaches."""
    print("=" * 60)
    print("Fibonacci Number Calculation - Comparison")
    print("=" * 60)
    
    test_cases = [0, 1, 5, 10, 15, 20]
    
    print(f"\n{'n':<5} {'Tabulation':<15} {'Optimized':<15} {'Match':<10}")
    print("-" * 60)
    
    for n in test_cases:
        result_tab = nth_fibonacci_tabulation(n)
        result_opt = nth_fibonacci_optimized(n)
        match = "✓" if result_tab == result_opt else "✗"
        
        print(f"{n:<5} {result_tab:<15} {result_opt:<15} {match:<10}")
    
    print("\n" + "=" * 60)
    print("Space Complexity Comparison:")
    print("-" * 60)
    print("Tabulation:        O(n) - stores entire array")
    print("Optimized:         O(1) - stores only 2 variables")
    print("\nFor large n (e.g., n=1000000), optimized is preferred!")
    print("=" * 60)


def print_fibonacci_sequence(n):
    """Print the first n Fibonacci numbers."""
    print(f"\nFirst {n} Fibonacci numbers:")
    sequence = []
    
    for i in range(n):
        sequence.append(nth_fibonacci_optimized(i))
    
    print(sequence)


if __name__ == "__main__":
    # Example 1: Calculate specific Fibonacci numbers
    print("\n📊 Example 1: Specific Fibonacci Numbers")
    print("-" * 60)
    for n in [10, 15, 20]:
        result = nth_fibonacci_optimized(n)
        print(f"F({n}) = {result}")
    
    # Example 2: Print Fibonacci sequence
    print("\n📊 Example 2: Fibonacci Sequence")
    print("-" * 60)
    print_fibonacci_sequence(15)
    
    # Example 3: Compare approaches
    print("\n📊 Example 3: Approach Comparison")
    compare_approaches()
    
    # Example 4: Large number test
    print("\n📊 Example 4: Large Number Test")
    print("-" * 60)
    n = 100
    result = nth_fibonacci_optimized(n)
    print(f"F({n}) = {result}")
    print(f"This would be impossible with naive recursion (2^{n} operations)!")
    print("=" * 60)
