# Day 8 - Arrays (Python / DSA)

Timebox: ~3 hours  
Objective: Understand list (array) fundamentals, apply core operations, and solve two classic array problems efficiently.

## Learning outcomes
- Represent and manipulate ordered data with Python lists
- Use indexing, iteration patterns, and in‑place mutation
- Apply hashing (dict) to reduce time from O(n^2) → O(n)
- Use two‑pointer / write‑index pattern for in‑place deduplication
- State time & space complexity clearly

---
## 1. Theory (~1 hour)
Arrays (Python lists) = ordered, mutable sequences. Zero‑based index.

Core operations (amortized complexity hints):
- Index read/write: arr[i] (O(1))
- Append: arr.append(x) (amortized O(1))
- Pop end: arr.pop() (O(1)); pop front (O(n)) due to shifting
- Length: len(arr) (O(1))
- Membership (naive): x in arr (O(n)) unless using auxiliary set/dict

Iteration patterns:
```python
for x in arr: ...           # values
for i in range(len(arr)): ... # indices
for i, x in enumerate(arr): ... # both
```

When to copy vs modify:
- Copy (arr[:]) when you must preserve original
- In‑place when problem demands O(1) extra space

Hash map (dict) use case:
- Fast key lookup O(1) average; trade space for speed

Two‑pointer/write‑index pattern:
- Maintain separate pointer (k) marking the next write position for a filtered/unique subset while scanning once

Log 3 bullet notes: indexing, hash map benefit, write index idea.

Resources (optional):
- Lists overview (GFG): https://www.geeksforgeeks.org/python-lists/
- Small video primer (Tech With Tim): https://www.youtube.com/watch?v=7e3fF-bkHF0

---
## 2. Practice (~2 hours)
Workflow per problem: Understand → Pseudocode → Code → Tests → Complexity → (Optional) variants.

### Problem 1: Two Sum (LeetCode)
Link: https://leetcode.com/problems/two-sum/
Goal: Return indices of two numbers whose sum == target. Assume exactly one solution (per LeetCode spec) and no reuse of the same element.

Brute force (why we avoid): nested loops O(n^2).
Hash map approach: single pass O(n) time, O(n) space.

Pseudocode:
```
map = {}
for i from 0..n-1:
    need = target - nums[i]
    if need in map: return [map[need], i]
    map[nums[i]] = i
return []  # if no solution (defensive)
```

Python:
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, val in enumerate(nums):
        need = target - val
        if need in seen:
            return [seen[need], i]
        seen[val] = i
    return []  # not expected per problem statement

assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([3,2,4], 6) == [1,2]
assert two_sum([3,3], 6) == [0,1]
```
Complexity: Time O(n), Space O(n).  
Why: One pass + constant average hash lookup.

Variant thoughts:
- If sorted input allowed two‑pointer approach (after sort) → O(n log n) with indices tracking or O(n) if already sorted.

### Problem 2: Remove Duplicates from Sorted Array (LeetCode)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Goal: In place, compress sorted list so each unique appears once; return new length k; first k positions contain uniques.

Pattern: write index k follows last unique; scan with i.

Pseudocode:
```
if nums empty: return 0
k = 1
for i from 1 .. n-1:
    if nums[i] != nums[i-1]:
        nums[k] = nums[i]
        k += 1
return k
```

Python:
```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

arr = [1,1,2]
length = remove_duplicates(arr)
assert length == 2 and arr[:length] == [1,2]
arr2 = [1,1,1]
length2 = remove_duplicates(arr2)
assert length2 == 1 and arr2[:length2] == [1]
arr3: list[int] = []
assert remove_duplicates(arr3) == 0
```
Complexity: Time O(n) single pass; Space O(1) extra.  
Why: Modifies in place; only a few counters.

Edge cases: empty list, all duplicates, all unique, size 1.

### Optional mini exercises
- Merge two sorted arrays (without using sort) → O(m+n)
- Find max and second max in one pass
- Count occurrences of each value using dict
- Reverse list in place with two pointers

---
## 3. Reflection (~10–15 min)
Prompts:
- Which array pattern felt new (hash map vs write index)?
- One misconception cleared today?
- Target focus for Day 9 (e.g., strings or more hash map drills)

Commit message: `Day 8: Arrays`.

---
## Cheat sheet
```
Index access              O(1)
Full traversal            O(n)
Two nested full loops     O(n^2)
Hash lookup (avg)         O(1)
Append (amortized)        O(1)
Remove dups (sorted)      O(n) time / O(1) space
Two Sum (hash)            O(n) time / O(n) space
```

### Tips & pitfalls
- Avoid unnecessary copies (slicing) in large loops
- Prefer enumerate() for index+value cleanly
- Use descriptive names: write index k, complement need
- For in‑place modifications, test with smallest inputs first ([], [x])

End of Day 8 guide.