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
Workflow per problem: Understand → Pseudocode → Code → Tests → Complexity → Edge cases.

### Problem 1: Find Maximum Element in an Array
Goal: Return the maximum value in a non‑empty list of integers.

Brute force idea: Keep track of current best while scanning once (already optimal) → O(n) time, O(1) space.

Pseudocode:
```
if array empty: (decide) raise error or return None
max_val = first element
for each remaining element x:
    if x > max_val: max_val = x
return max_val
```

Python:
```python
from typing import Iterable, Optional

def find_max(nums: list[int]) -> int:
    if not nums:
        raise ValueError("find_max() arg is an empty list")
    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m

assert find_max([1]) == 1
assert find_max([1, 5, 3, 2]) == 5
assert find_max([-4, -2, -9]) == -2
```
Complexity: Time O(n) (single pass), Space O(1) extra.  
Edge cases: single element, all negatives, already sorted ascending/descending, very large list (streaming still fine).  
Variants: Track both max and second max in same pass; streaming scenario where data arrives chunked (update current max per batch).

### Problem 2: Sum of All Elements (GFG)
Reference: Classic practice (e.g., GFG "Program to find sum of elements in an array").

Goal: Compute total sum of a list of integers.

Approach: Accumulate running total while scanning once.

Pseudocode:
```
total = 0
for x in nums:
    total += x
return total
```

Python:
```python
def sum_array(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    return total

assert sum_array([]) == 0
assert sum_array([5]) == 5
assert sum_array([1,2,3,4]) == 10
assert sum_array([-2, 3, -1]) == 0
```
Complexity: Time O(n), Space O(1).  
Why not use built‑in sum immediately? For learning the loop pattern & manual accumulation; in production prefer built‑in `sum(nums)` (CPython optimized in C).  
Edge cases: empty list (return 0), large magnitude values (watch for overflow in other languages—Python ints auto‑expand).

Mini variant: Average = sum / n (handle n = 0 separately).

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

---
## Appendix A — Python Lists vs array vs NumPy
### 1. Python Lists
- Heterogeneous: can mix ints, strings, floats, even other lists
- Dynamic size, contiguous array of references (CPython)
- Most common general‑purpose sequence

Example:
```python
my_list = [1, "hello", 3.14, [5, 6]]
print(my_list)  # [1, 'hello', 3.14, [5, 6]]
```

### 2. array module
- Homogeneous: all elements same type code (e.g. 'i' for signed int)
- Slightly more compact than list for large numeric collections
- Less feature‑rich; rarely needed unless memory micro‑optimization

Example:
```python
from array import array
ints = array('i', [1, 2, 3, 4])
print(ints)  # array('i', [1, 2, 3, 4])
```

### 3. NumPy ndarray
- Multidimensional, vectorized operations, broadcasting
- Highly efficient for numerical / scientific computing

Example:
```python
import numpy as np
np_array = np.array([1, 2, 3, 4])
print(np_array)  # [1 2 3 4]
```

### 4. Comparison
| Feature                | list (built‑in)            | array.array           | NumPy ndarray              |
|------------------------|----------------------------|-----------------------|----------------------------|
| Mixed types            | Yes                        | No                    | No (dtype per array)       |
| Dynamic resize         | Yes                        | Yes (costly sometimes)| Fixed size (can copy)      |
| Numeric performance    | Moderate (Python loop)     | Slightly better       | High (C vectorized)        |
| Methods richness       | High                       | Low                   | High (math ops)            |
| External dependency    | No                         | No                    | Yes (install numpy)        |
| Best use               | General purpose            | Niche memory saving   | Numeric / scientific       |

Selection guide:
- Everyday scripting → list
- Large homogeneous numeric data + heavy compute → NumPy
- Tiny memory tweak w/out extra dependency → array.array

---
## Appendix B — List Methods Reference
Selected list methods (with typical complexities):

| Method | Purpose | Typical Time* |
|--------|---------|---------------|
| append(x) | Add to end | O(1) amortized |
| extend(iter) | Add many | O(k) (k = len(iter)) |
| insert(i, x) | Insert at index | O(n) (shift) |
| remove(x) | Remove first occurrence | O(n) (search + shift) |
| pop() | Remove last | O(1) |
| pop(i) | Remove at i | O(n) (shift) |
| clear() | Remove all | O(n) |
| index(x, [start],[end]) | Find position | O(n) |
| count(x) | Count occurrences | O(n) |
| sort() | In‑place sort (Timsort) | O(n log n) |
| reverse() | Reverse in place | O(n) |
| copy() | Shallow copy | O(n) |

`join()` note: It's a string method used as separator: `' '.join(words)` (efficient vs manual concatenation).

Examples:
```python
nums = [1, 2, 3]
nums.append(4)        # [1,2,3,4]
nums.extend([5, 6])   # [1,2,3,4,5,6]
nums.insert(1, 9)     # [1,9,2,3,4,5,6]
nums.pop()            # removes 6
nums.remove(9)        # first occurrence of 9
nums.reverse()        # in place reverse
copy_nums = nums.copy()
```

Pitfalls:
- `list.sort()` returns None (in place); use `sorted(list)` for a new list
- Using `+=` with list mutates in place; for copying prefer slice or list()
- Frequent `insert(0, x)` causes O(n) shifts; consider collections.deque

*Complexities refer to CPython typical behavior.

---
End of Day 8 guide.