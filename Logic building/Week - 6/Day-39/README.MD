Day 39 — Stack Applications

Date: November 1, 2025
Topic: Stacks & Queues (Stack Applications)

📚 Purpose

Today is about moving from basic stack theory (using list.append/pop) to solving complex problems using specific stack patterns.

Pattern 1: The Monotonic Stack

Pattern 2: The Two-Stack Design

🎯 TL;DR

Monotonic Stack: A stack kept in (usually) decreasing order. It's the key to all "Next Greater Element" problems. It's the "sister" pattern to the Monotonic Deque.

Two-Stack Design: A classic "design" problem. Use a main_stack for all data and a min_stack to track the current minimum, allowing for a O(1) getMin() operation.

Key Insight: The "chutiyapaa" in these problems is any solution that uses a nested loop (O(N^2)) or a min() function (O(N)). The correct patterns are always O(N) or O(1).

🎨 Pattern 1: Monotonic Stack — "Next Greater Element I" (Medium)

💡 Core Idea ("The Line of Waiters")

The goal is to find the first number to the right of an element that is greater.

Brute-Force (The $O(M \times N)$ Trap): Looping through nums1, then nums2, then a third loop to find the answer. This is too slow.

Optimal (The $O(M + N)$ Solution): We find the "next greater element" for every number in nums2 in one single pass.

We use two tools:

stack (a list): Holds "waiters"—numbers that are waiting for their next greater element to appear.

answers_map (a dict): Stores the (key: value) pair of (waiter: answer).

🧠 The 3 Rules (For each num in nums2)

Process "Waiters" (from TOP):

Logic: If the new num is bigger than the "waiter" on top of the stack, that waiter has found its answer.

Code: while stack and num > stack[-1]:

waiter = stack.pop()

answers_map[waiter] = num

Add New "Waiter" (to TOP):

Logic: After processing all the smaller waiters, the new num is now also a waiter.

Code: stack.append(num)

Handle Leftovers (After Loop):

Logic: Any "waiter" still in the stack never found an answer.

Code: while stack: answers_map[stack.pop()] = -1

📝 Implementation (LeetCode 496)

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 1. Setup our tools
        stack = []         # For "waiters"
        answers_map = {}   # For "waiter: answer" pairs

        # 2. Loop through nums2 to fill the map
        for num in nums2:
            # Rule 1: Process waiters
            while stack and num > stack[-1]:
                waiter = stack.pop()
                answers_map[waiter] = num
            
            # Rule 2: Add new waiter
            stack.append(num)

        # 3. Handle leftovers
        while stack:
            waiter = stack.pop()
            answers_map[waiter] = -1
            
        # 4. Build the final result
        result_list = []
        for num in nums1:
            result_list.append(answers_map[num])
            
        return result_list


⏱️ Complexity

Time: O(M + N) — $O(N)$ to build the map (amortized) and $O(M)$ to build the result.

Space: O(N) — For the answers_map and the stack.

🎨 Pattern 2: Two-Stack Design — "Min Stack" (Medium)

💡 Core Idea (O(1) getMin)

This is a design problem. We must build a stack where push, pop, top, AND getMin are all $O(1)$ (constant time).

Brute-Force (The $O(N)$ Trap): Using min(self.data) for getMin(). This is an $O(N)$ loop and is too slow.

Optimal (The $O(1)$ Solution): We must always know the minimum. We do this by using two stacks.

main_stack: Holds all the numbers.

min_stack: A helper stack. The top of this stack (min_stack[-1]) is always the current minimum for the entire main_stack.

🧠 The 3 Rules (The Core Logic)

Rule 1: push(val)

Always main_stack.append(val).

Only min_stack.append(val) if:

The min_stack is empty (if not self.min_stack...)

OR val <= self.min_stack[-1] (it's a new min, or a duplicate min)

Rule 2: pop()

item = main_stack.pop().

Only min_stack.pop() if:

The item we just popped is equal to the current minimum (if item == self.min_stack[-1]).

Rule 3: getMin()

This is now the easy part: return self.min_stack[-1].

📝 Implementation (LeetCode 155)

class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        
        # This is the most important line in the class
        # It handles the empty case AND the new-min/duplicate-min case
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Check if main_stack is empty to prevent crashes
        if self.main_stack:
            item = self.main_stack.pop()
            
            # Keep the stacks in sync
            # Check if min_stack is *not* empty AND the item was the min
            if self.min_stack and item == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        return None # Or raise an error

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None # Or raise an error


⏱️ Complexity

Time: O(1) for all operations (push, pop, top, getMin).

Space: O(N) — In the worst case ([5, 4, 3, 2, 1]), both stacks grow to size N.

🎓 Interview Tips

Monotonic Stack: This pattern is for "Next Greater/Smaller" problems. The stack holds "waiters," and the map stores answers.

Two-Stack Design: This is for "Get-Min/Max in O(1)" problems. The key is the push logic: val <= min_stack[-1]. The "or equal to" (<=) is critical for handling duplicate minimums.

Safety First: Always check if a stack is empty (if stack:) before calling pop() or peeking (stack[-1]) to avoid IndexError crashes.