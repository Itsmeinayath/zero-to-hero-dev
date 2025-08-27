## Day 10 – Two-Pointer Technique
Timebox: ~3 hours (Theory 1h • Core problems 90m • Optional JS 30m)  
Commit: `Day 10: Two-Pointer Technique`  
Goal: Recognize when two indices can remove a nested loop and implement classic patterns confidently.

### Learning outcomes
- Identify problems that can shift from O(n^2) brute force to O(n) with two pointers
- Distinguish major pointer pattern families (opposite ends, same direction / slow-fast, partitioning, in-place write)
- Implement: sorted two-sum, move zeroes, reverse string, remove duplicates (sorted)
- Explain time & space complexity succinctly
- Decide when hash map beats two-pointer and vice versa

---
## 1. Pattern Taxonomy (Mental Map)
Pattern | Layout | Typical Use | Example
--------|--------|-------------|--------
Opposite ends | `l=0; r=n-1` move inward | Sorted pair sums, palindromes | Sorted 2-sum
Same direction (slow/fast) | `slow`, `fast` advancing | Removing duplicates, cycle detection | Floyd cycle, list dedupe
Write index | `write`, `read` | In-place filtering/compaction | Move zeroes, remove element
Partition | `left`, `right` swap partitions | Dutch flag / quicksort partition | Even/odd split
Sliding window (variant) | `start`, `end` expand/shrink | Subarray / substring constraints | Longest subarray with k constraint

Heuristic: Ask “Can I maintain a relationship between two positions and move them monotonically without rewinding?” If yes → candidate.

Anti-example: Unsorted Two Sum requiring original indices → hash map usually simpler; two-pointer only works if array sorted (or you are allowed to sort with O(n log n) overhead and adjust if indices not needed pre-sort).

---
## 2. Core Concepts (Concise)
- Movement must be monotonic to guarantee O(n) (each pointer advances at most n steps)
- Termination condition: when pointers cross or fast reaches end
- State carried: often partial result (running sum, last non-zero index, write position)
- In-place transforms require careful order of reads vs writes

Common pitfalls & fixes:
Pitfall | Fix
--------|----
Pointer stuck (infinite loop) | Ensure movement in every branch
Overwriting needed data | Swap only after reading all necessary values
Using two-pointer on unsorted pair-sum | Sort first (loses original indices) or switch to hash map
Off-by-one end conditions | Rehearse with 0/1 length arrays

---
## 3. Problem 1: Two Sum (Sorted Array Variant)
If input is ALREADY sorted you can do O(n) with two pointers. Original LeetCode #1 array is not guaranteed sorted → canonical solution uses hash map (O(n) time, O(n) space). Here we practice the pointer form with sorted input.

Goal: indices (1-based in some variants; we’ll use 0-based) of two numbers that add to target.

Pseudocode:
```
l = 0; r = n-1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return (l, r)
    if s < target: l += 1  # need bigger sum
    else: r -= 1           # need smaller sum
return (-1, -1)
```

Python:
```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1
        else:
            r -= 1
    return []

assert two_sum_sorted([1,2,4,6,10], 8) == [1,2]  # 2+6
```
Complexity: Time O(n), Space O(1).  
When not sorted: use hash map variant (still O(n) time, but O(n) space; pointer version would need sort O(n log n)).

Hash map refresher (unsorted):
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        want = target - x
        if want in seen:
            return [seen[want], i]
        seen[x] = i
    return []
```

---
## 4. Problem 2: Move Zeroes (In-place Compaction)
Goal: Move all 0s to end while preserving relative order of non-zeros.

Pattern: write index / read index (single pass). Swap only when encountering non-zero.

Pseudocode:
```
write = 0
for read in range(n):
    if nums[read] != 0:
        swap(nums[write], nums[read])
        write += 1
```
Python:
```python
def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums

assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
```
Complexity: O(n) time, O(1) extra.  
Stability: Maintains order of non-zeros due to left-to-right pass.

---
## 5. Problem 3: Reverse String (Two Ends)
Classic opposite ends pointer swap.
```python
def reverse_in_place(chars):
    l, r = 0, len(chars)-1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1; r -= 1
    return chars

assert ''.join(reverse_in_place(list('hello'))) == 'olleh'
```
Complexity: O(n) time, O(1) extra.

---
## 6. Problem 4: Remove Duplicates From Sorted Array
Goal: In sorted list keep unique elements at start; return new length (LeetCode #26 style).

Pattern: write pointer for last unique.
```python
def remove_duplicates(nums):
    if not nums: return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write-1]:
            nums[write] = nums[read]
            write += 1
    return write

arr = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(arr)
assert arr[:k] == [0,1,2,3,4]
```
Complexity: O(n) time / O(1) space.

---
## 7. Choosing the Pattern (Decision Guide)
Problem statement talks about... | Candidate
---------------------------------|----------
Pair sum in sorted data | Opposite ends
Filtering / compressing array | Write pointer
Maintaining window constraints | Sliding window (variant of two pointers)
Finding duplicates removal in sorted | Slow/fast or write pointer
Partitioning by predicate | Partition (left/right swapping)
Cycle detection in linked list | Slow/fast (Floyd)

If unsorted + need pair sum indices → Hash map beats two-pointer (unless allowed to sort & lose order).

---
## 8. Common Pitfalls & Fixes
Issue | Example | Fix
------|---------|----
Move both pointers when only one should move | Two-sum sorted increments both on mismatch | Only adjust one side based on comparison
Infinite loop on duplicates | Not advancing when condition equal | Ensure pointer movement each iteration
Accidental extra space solution | Building new array for move zeroes | Use in-place swaps
Losing indices after sort | Sorting original for two-sum | Track original indices or use map

Testing edge cases ALWAYS: empty list, size 1, all zeros, no solution, already unique, already reversed.

---
## 9. Optional JavaScript Rewrites
```js
// Two-sum unsorted (hash map)
function twoSum(nums, target){
  const seen = new Map();
  for (let i=0;i<nums.length;i++){
    const want = target - nums[i];
    if (seen.has(want)) return [seen.get(want), i];
    seen.set(nums[i], i);
  }
  return [];
}

// Move zeroes
function moveZeroes(nums){
  let write=0;
  for (let read=0; read<nums.length; read++){
    if (nums[read] !== 0){
      [nums[write], nums[read]] = [nums[read], nums[write]];
      write++;
    }
  }
  return nums;
}
```

---
## 10. Cheat Sheet
Operation | Time | Space | Notes
----------|------|-------|------
Two-sum sorted | O(n) | O(1) | Needs sorted
Two-sum unsorted (map) | O(n) | O(n) | Keeps original indices
Move zeroes | O(n) | O(1) | Stable non-zero order
Reverse string in-place | O(n) | O(1) | Swap converging
Remove duplicates (sorted) | O(n) | O(1) | Write pointer technique

Template steps (opposite ends):
```
l=0; r=n-1
while l<r:
  # compare / swap / adjust
```

Template steps (write pointer):
```
write=0
for read in range(n):
    if keep_condition(nums[read]):
        nums[write]=nums[read]
        write+=1
```

---
## 11. Mini Exercises (Pick 2–3)
1. Square sorted array then return sorted squares (use opposite ends to merge largest absolute values)
2. Partition array so evens on left odds on right (two pointers swap)
3. Remove all instances of value X in-place (write pointer)
4. Given sorted array and target, return first pair with sum > target (opposite ends modification)
5. Implement palindrome check for a string ignoring non-alphanumerics (opposite ends skip filtering) – revisit Day 9

---
## 12. Reflection
Prompts:
- Which pattern felt most natural today?
- Did you accidentally write an O(n^2) brute force first? How would you spot that earlier next time?
- One heuristic you will apply tomorrow to detect pointer usability faster?

Log example: “Practiced opposite-ends & write-pointer; replaced nested loops with O(n). Clear on when to use hash map instead.”

---
## 13. Preview (Day 11)
Likely next: Sliding window (length / sum constraints) or Hash map + frequency patterns (anagrams / subarray sums). Will build on two-pointer movement logic.

End of Day 10 guide.