## Day 12 – Array Manipulation & In-Place Techniques
Timebox: ~3 hours (Concept 45m • Core problems 60–75m • Extensions 30m • JS/Refactor 15–20m • Reflection 5–10m)  
Commit: `Day 12: Array Manipulation`  
Objective: Master in-place array updates (write/read pointers, backfill merges, stable vs unstable operations) to reduce extra space and clarify mutation patterns.

### Session Overview
Pattern Focus: In-place modification using minimal extra memory (O(1)) via pointer strategies.  
Outputs Today:
- Reusable templates: (a) two-pointer read/write, (b) reverse fill merge, (c) partition filter, (d) stable compaction.
- Implementations: remove duplicates (sorted), merge sorted in-place, remove element, move zeros, rotate, two-sum contrast (why not always manipulate).
- Complexity table (cost of shifting vs backfill).
- Pitfall checklist for index corruption and overwrites.

Primary Problems (LeetCode IDs): 26, 88, 27, 283, 189 (optional), 905 (parity partition), 1089 (duplicate zeros – stretching variant).

### Learning Outcomes
- Differentiate traversal vs compaction vs partition patterns
- Use forward write index safely without data loss
- Merge sorted arrays from end to avoid O(m+n) extra memory
- Identify when stable order matters and adjust algorithm
- Produce complexity reasoning for each mutation

---
## 1. Quick Start Templates
Two-pointer Compaction (keep elements matching predicate keep(x)):
```python
write = 0
for read, val in enumerate(arr):
    if keep(val):
        arr[write] = val
        write += 1
return write
```

Backwards Merge (two sorted arrays A (m) + B (n) into A sized m+n):
```python
i, j, k = m-1, n-1, m+n-1
while j >= 0:
    if i >= 0 and A[i] > B[j]:
        A[k] = A[i]; i -= 1
    else:
        A[k] = B[j]; j -= 1
    k -= 1
```

Stable Partition (move all zeros to end keeping order): use compaction + fill.

Rotate Right by k (cyclic reversal method): reverse whole, reverse first k, reverse remainder.

---
## 2. Core Concepts
Concept | Summary | Why It Matters
--------|---------|---------------
Compaction | Overwrite unwanted entries with wanted ones | O(1) space filter
Backfill Merge | Fill from back to prevent overwriting unprocessed items | Avoid extra array
Partition (unstable) | Swap unwanted front with wanted end | Faster when order unimportant
Stability | Preserving original relative order | Some problems require it (move zeros)
Index Safety | Reads must not rely on overwritten data | Choose direction accordingly

Complexity Reminder: Insert/remove at arbitrary index in array => shift O(n). Rewriting in one pass keeps O(n) time; repeated deletions naive → O(n^2).

---
## 3. Problem 1 – Remove Duplicates from Sorted Array (LC 26)
Keep first instance of each sorted run.
```python
def remove_duplicates(nums):
    if not nums: return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write-1]:
            nums[write] = nums[read]
            write += 1
    return write

arr = [1,1,2,2,3]
k = remove_duplicates(arr)
assert k == 3 and arr[:k] == [1,2,3]
```
Time O(n), Space O(1).  
Invariant: nums[:write] has unique elements processed so far.

---
## 4. Problem 2 – Merge Sorted Array (LC 88)
Reason for backward fill: forward would overwrite future needed values.
```python
def merge(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]; i -= 1
        else:
            nums1[k] = nums2[j]; j -= 1
        k -= 1

a = [1,2,3,0,0,0]
merge(a,3,[2,5,6],3)
assert a == [1,2,2,3,5,6]
```
Time O(m+n), Space O(1).

---
## 5. Problem 3 – Remove Element (LC 27)
Remove all instances of val; order may change? (Spec: order can change, but stable also fine.)
Stable compaction version:
```python
def remove_element(nums, val):
    write = 0
    for x in nums:
        if x != val:
            nums[write] = x
            write += 1
    return write

arr = [3,2,2,3]
k = remove_element(arr,3)
assert k == 2 and sorted(arr[:k]) == [2,2]
```
Time O(n) / Space O(1).

---
## 6. Problem 4 – Move Zeroes (LC 283)
Stable: compress non-zero then fill remainder with zeros.
```python
def move_zeroes(nums):
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0

arr = [0,1,0,3,12]
move_zeroes(arr)
assert arr == [1,3,12,0,0]
```
Time O(n). Non-zero writes ≤ non-zero count (optimal minimal overwrites).

---
## 7. Problem 5 – Rotate Array Right by k (LC 189)
Use triple reverse (stable within rotation definition). k %= n.
```python
def rotate(nums, k):
    n = len(nums)
    if n == 0: return
    k %= n
    def rev(l,r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    rev(0,n-1); rev(0,k-1); rev(k,n-1)

arr = [1,2,3,4,5,6,7]
rotate(arr,3)
assert arr == [5,6,7,1,2,3,4]
```
Time O(n) / Space O(1).

---
## 8. Bonus – Parity Partition (LC 905 style)
Unstable swap to group even front, odd back.
```python
def parity_partition(nums):
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] % 2 == 0:
            l += 1
        elif nums[r] % 2 == 1:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    return nums

arr = [3,1,2,4]
res = parity_partition(arr)
assert set(res[:2]) == {2,4}
```
Time O(n) / Space O(1). Order not preserved.

---
## 9. Decision Guide
Goal | Pattern | Template
-----|---------|---------
Filter keep subset stable | Compaction | forward read/write
Filter, order irrelevant | Partition swap | two ends swap
Merge sorted into buffer end | Backfill | backwards pointers
Shift zeros/end markers | Compaction + fill | two passes
Rotate | Reverse segments | triple reverse
Duplicate stretch (LC 1089) | Reverse/backward expansion | backward second pass

---
## 10. Complexity Cheat Sheet
Operation | Worst Time | Space | Notes
----------|-----------|-------|------
Single pass compaction | O(n) | O(1) | Minimal writes
Backwards merge | O(m+n) | O(1) | Prevents overwrite
Naive repeated pop(0) | O(n^2) | O(1) | Avoid; shift cost each time
Rotate by reversing | O(n) | O(1) | 3 reversals
Parity partition | O(n) | O(1) | Unstable

---
## 11. Pitfalls & Fixes
Pitfall | Cause | Fix
--------|-------|----
Overwriting unread values | Forward fill when future needed | Switch to backward or temp
Extra allocations | Using new list for simple compaction | Use write index
Too many writes | Swapping zeros repeatedly | Two-phase compaction
Wrong k rotation | Not k%=n | Normalize k first
Forgot stability | Used swap partition for move zeroes | Use compaction

---
## 12. Mini Exercises (Pick 3)
1. LC 1089 Duplicate Zeros (simulate extra slot backwards)  
2. Remove all occurrences of value but return modified slice (Python)  
3. Implement left rotation by k using same reverse trick  
4. Compact only first occurrence of each element in unsorted array (use set)  
5. Write parity partition stable version (two-pass)  

---
## 13. JavaScript Snippets
```js
// Remove duplicates (sorted)
function removeDuplicates(nums){
  if(!nums.length) return 0;
  let write=1;
  for(let i=1;i<nums.length;i++){
    if(nums[i] !== nums[write-1]) nums[write++] = nums[i];
  }
  return write;
}

// Merge sorted arrays (in-place)
function merge(nums1, m, nums2, n){
  let i=m-1, j=n-1, k=m+n-1;
  while(j>=0){
    if(i>=0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
    else nums1[k--] = nums2[j--];
  }
}

// Move zeroes
function moveZeroes(nums){
  let write=0;
  for(const x of nums) if(x!==0) nums[write++] = x;
  while(write < nums.length) nums[write++] = 0;
}
```

---
## 14. Resources
- LeetCode: 26, 88, 27, 283, 189, 905, 1089
- GFG: Array Data Structure overview
- NeetCode: In-place array problems playlist
- Visualizing pointer movement: PythonTutor / JS Tutor

---
## 15. Reflection
Prompts:
1. Which pattern (compaction, backfill, partition) felt most natural? Why?
2. Did you accidentally overwrite any needed values? How did you catch it?
3. One sentence rule to detect backfill need tomorrow?

Sample Log: “Practiced compaction & backfill; merged without extra space; clarified stable vs unstable partitions; normalized k in rotations.”

---

End of Day 12 guide.
