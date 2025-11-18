#
# LeetCode 78: Subsets
#
# This is our first Backtracking problem.
# We are using the "Include / Exclude" or
# "Choose / Explore / Unchoose" pattern.
#
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # 1. Setup our main tools
        result = []  # This list holds all the final answers
        current_subset = [] # This list is our "notepad"

        # 2. Define our "Maze Explorer" (the recursive function)
        def backtrack(index):
            
            # 3. Base Case (The "Stopping Condition")
            # If our index is past the end of the array,
            # we have made all our choices.
            if index == len(nums):
                # We found a complete subset. 
                # We MUST add a .copy()
                result.append(current_subset.copy())
                return # Stop exploring this path
            
            
            # --- Path 1: INCLUDE nums[index] ---
            
            # 1. CHOOSE
            current_subset.append(nums[index])
            
            # 2. EXPLORE
            # Go find all subsets starting from the *next* index.
            backtrack(index + 1)
            
            # 3. UNCHOOSE (The "Backtrack" magic!)
            # Pop the number off so we are "clean" for the next path.
            current_subset.pop()
            
            
            # --- Path 2: EXCLUDE nums[index] ---
            
            # 1. CHOOSE (We do nothing to the subset)
            
            # 2. EXPLORE
            # Go find all subsets, *skipping* this number.
            backtrack(index + 1)
        
        # 4. Start the process
        backtrack(0) # Start at the first number (index 0)
        return result
