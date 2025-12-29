Climbing Stairs


🎯 Purpose

To wake up the "Logic Building" muscle after a break. We revisit the core pattern of Dynamic Programming using a simple example.

🎨 Pattern: Decision at Step N

The core insight is working backwards:
"I am at the top (Step N). How did I get here?"

There are only two last moves possible:

From N-1 (1 step jump)

From N-2 (2 step jump)

Therefore: Ways(N) = Ways(N-1) + Ways(N-2)

🛠️ Solutions

1. Naive Recursion (Bad)

Builds a massive tree of duplicate calculations.

Time: O(2^n)

Space: O(n)

2. Memoization (Better)

Stores the result of each step so we calculate it only once.

Time: O(n)

Space: O(n)

3. Iterative (Optimal)

We only need the last two values to calculate the next one. We don't need to store the whole history.

Time: O(n)

Space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1
