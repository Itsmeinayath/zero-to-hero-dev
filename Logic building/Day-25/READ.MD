- **Day 25 (Thu): Sorting**
    - **Theory (0.5 hr)**:
        - Review bubble, selection, insertion sort.
        - **Video**: NeetCode’s “Sorting Recap” (15 min) ([YouTube](https://www.youtube.com/watch?v=JU767SDMDvA&t=300s)).
        - **Article**: GFG’s “Sorting Algorithms” (15 min) ([Link](https://www.geeksforgeeks.org/sorting-algorithms/)).
    - **Practice (2.5 hr)**:
        - **Problem 1**: LeetCode: Merge Intervals ([Link](https://leetcode.com/problems/merge-intervals/)).
            - **Brute Force**: Check all pairs (O(n²)).
            - **Better**: Sort and merge (O(n log n)).
            - **Optimal**: Same, clean merging (O(n log n)).
            - **Pseudocode**:
                
                ```
                Input: intervals
                Sort intervals by start time
                Initialize result with first interval
                For each interval:
                    If overlaps with last result: Merge
                    Else: Add to result
                Return result
                ```
                
            - **Logic Exercise**: Draw interval merging.
        - **Problem 2**: GFG: Sort Array by Parity ([Link](https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/)).
            - **Brute Force**: New arrays for even/odd (O(n) space).
            - **Better**: Two pointers in-place (O(1) space).
            - **Optimal**: Same, clean swaps (O(n)).
            - **Pseudocode**:
                
                ```
                Input: array nums
                Initialize left = 0, right = len(nums)-1
                While left < right:
                    If nums[left] odd and nums[right] even: Swap
                    If nums[left] even: Increment left
                    If nums[right] odd: Decrement right
                Return nums
                ```
                
            - **Logic Exercise**: Visualize swaps