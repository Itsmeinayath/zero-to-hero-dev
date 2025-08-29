## Day 12 - Binary Search
Timebox: ~3 hours (Theory 45–60m • Core variants 75–90m • Optional JS 20m • Reflection 5–10m)  
Commit: `Day 12: Binary Search`  
Objective: Turn any ordered search / threshold / boundary finding task from O(n) into O(log n) by halving search space.

### Session Overview (Read This First)
What we learn today (Pattern Focus): Binary Search family (exact search, insertion point, boundary (first/last), predicate (answer space), rotated array, numeric sqrt).

End-of-day outputs (you should have):
- Reusable iterative template (closed interval) memorized
- Boundary helpers: `lower_bound`, `upper_bound`, first/last occurrence
- Predicate search helper (`binary_search_predicate`)
- Implementations for: classic search (LC 704), search insert (LC 35), first/last position (LC 34), search rotated (LC 33), sqrt (LC 69), peak element (LC 162) – at least drafted
- Personal note: difference between closed [l,r] vs half-open [l,r)

Key competencies gained:
- Recognize monotonic structure (sorted data OR monotonic predicate)
- Choose correct interval style & loop condition
- Bias midpoint updates for boundary queries
- Avoid infinite loops & off-by-one

Primary learning resources (skim then code):
- LeetCode 704 (Binary Search) – baseline
- LeetCode 35 (Search Insert Position) – insertion pattern
- LeetCode 34 (Find First and Last Position) – boundary biasing
- LeetCode 33 (Search in Rotated Sorted Array) – choosing sorted half
- LeetCode 69 (Sqrt(x)) – predicate/answer space
- LeetCode 162 (Find Peak Element) – directional binary search
- GFG: Binary Search basics
- GFG: First and last occurrences of X
- GFG: Square root of a number
- LeetCode Discuss: Binary Search Template III (predicate style)

Stretch (if time remains):
- Capacity to Ship Packages Within D Days (LC 1011) – predicate
- Koko Eating Bananas (LC 875) – predicate on speed

Tracking Suggestion: In your notes add a small table: Problem | Interval Style | Condition to Move Left | Condition to Move Right | Return Value.

### Learning Outcomes
- Recognize when data or answer space is monotonic / sorted
- Implement base iterative binary search + recursive form
- Derive boundary (first/last occurrence) pattern using biasing
- Apply predicate (answer space) search (min x satisfying condition)
- Handle rotated sorted array and square root approximation
- Avoid common pitfalls (infinite loop, off-by-one, wrong mid update)

---
## 1. Quick Start (Read First – 60s)
Use Binary Search when:
1. Data is sorted (array/string) OR
2. Answer space can be linearly ordered & predicate is monotonic (false → true) OR
3. Rotated but each half still partially ordered enabling direction choice.

Core Loop Template (Iterative):
```python
def binary_search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r) // 2  # Python safe
        if nums[m] == target: return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
```

Boundary (First True / Lower Bound) Template:
```python
def lower_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:  # still too small
            l = m + 1
        else:                 # nums[m] >= target -> candidate
            r = m
    return l  # first index where nums[i] >= target
```

Predicate Search (Min x s.t. f(x) == True): keep narrowing left-most True.

---
## 2. Visual Intuition
Example: Find 7 in [1,3,5,7,9]
```
Indices: 0 1 2 3 4
Values : 1 3 5 7 9
Step1: l=0 r=4 m=2 val=5 <7 -> l=3
Step2: l=3 r=4 m=3 val=7 == target -> return 3
```
Halving each iteration → after k steps array size ≈ n / 2^k; stop when size 1 ⇒ k ≈ log2 n.

---
## 3. Complexity Justification
Each iteration discards ~half remaining elements → O(log n) time.
Space: O(1) iterative; O(log n) recursive (call stack).

---
## 4. Variant Patterns Overview
Goal | Adjustments | Return
-----|-------------|-------
Exact index | Classic | index / -1
Insertion point | Return left after loop | position
First occurrence | Bias right toward mid-1 when match but continue | index
Last occurrence | Bias left toward mid+1 when match but continue | index
Lower bound (>=) | Half-open [l,r) + nums[m] < target | l
Upper bound (>) | Half-open [l,r) + nums[m] <= target | l
Predicate / answer space | Evaluate condition(mid) | boundary
Rotated sorted array | Decide sorted half then discard | index
Search on function | Evaluate monotonic function f(mid) | minimal solution

---
## 5. Pitfalls & Fixes
Pitfall | Cause | Fix
--------|-------|----
Infinite loop | Not shrinking interval | Ensure l or r moves each iteration
Miss first occurrence | Return immediately on match | Instead move r = m - 1 (store ans)
Overflow (other langs) | (l + r) overflow | Use l + (r-l)//2 (Python unaffected)
Wrong loop condition | Using while l < r for exact search | Use while l <= r for closed interval
Off-by-one insertion | Returning r | For insert position return l

---
## 6. Core Implementations (Python)
```python
from typing import List, Callable

def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

def search_insert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r)//2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return l  # insertion position

def first_occurrence(nums: List[int], target: int) -> int:
    ans = -1
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] >= target:
            if nums[m] == target:
                ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

def last_occurrence(nums: List[int], target: int) -> int:
    ans = -1
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] <= target:
            if nums[m] == target:
                ans = m
            l = m + 1
        else:
            r = m - 1
    return ans

def lower_bound(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r)//2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r)//2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m
    return l

def binary_search_predicate(lo: int, hi: int, ok: Callable[[int], bool]) -> int:
    # Return smallest x in [lo, hi] with ok(x) True; assume monotonic
    while lo < hi:
        mid = (lo + hi)//2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def search_rotated(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r)//2
        if nums[m] == target:
            return m
        # Left half sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:  # Right half sorted
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

def int_sqrt(n: int) -> int:
    # floor(sqrt(n)) using predicate search
    if n < 0: raise ValueError("n must be non-negative")
    l, r = 0, n
    ans = 0
    while l <= r:
        m = (l + r)//2
        if m*m <= n:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans

# Basic assertions
assert binary_search([1,3,5,7,9],7) == 3
assert binary_search([1,3,5],2) == -1
assert search_insert([1,3,5,7],4) == 2
arr = [1,2,2,2,3,4]
assert first_occurrence(arr,2) == 1
assert last_occurrence(arr,2) == 3
assert lower_bound(arr,2) == 1
assert upper_bound(arr,2) == 4
assert search_rotated([4,5,6,7,0,1,2],0) == 4
assert int_sqrt(16) == 4 and int_sqrt(17) == 4
```

---
## 7. Representative Problems
Problem | Pattern | Key Twist
--------|---------|----------
Binary Search (LC 704) | Exact | Classic
Search Insert Position | Insertion | Return l
First/Last Position (LC 34) | Bounds | Two biased searches
Search Rotated Array (LC 33) | Rotated | Identify sorted half
Sqrt(x) (LC 69) | Predicate | value^2 <= n
Peak Element (LC 162) | Directional | Move toward greater neighbor

---
## 8. Decision Guide
Question | If Yes | Action
---------|--------|-------
Is array fully sorted? | Yes | Classic binary search
Need first/last position? | Yes | Biased bound search
Array rotated? | Yes | Use sorted-half logic
Searching for threshold (min time/ capacity)? | Yes | Predicate search over answer space
Values huge range but monotonic condition? | Yes | Exponential expand then binary search

When NOT to use: data unsorted and cannot be sorted / no monotonic predicate / heavy per-iteration cost > benefit.

---
## 9. Cheat Sheet
Pattern | Loop Condition | Update on Match
--------|----------------|----------------
Exact closed | while l <= r | return immediately
Lower bound | while l < r | r = m
Upper bound | while l < r | l = m + 1
First occurrence | while l <= r | record ans; r = m-1
Last occurrence | while l <= r | record ans; l = m+1
Predicate min True | while lo < hi | hi = mid or lo = mid+1

Formula safety: mid = l + (r-l)//2 (avoid overflow in 32-bit languages).

---
## 10. Common Debug Checklist
- Does interval shrink every iteration? (print l,r if stuck)
- Are you mixing half-open [l,r) with closed [l,r]? (Choose one.)
- Are termination & return consistent with interval style?
- For boundaries: did you remove early return on match?
- For rotated: verify which half is sorted using <= not < (duplicate edge cases) 

---
## 11. Mini Exercises
1. Implement `upper_bound` from memory.
2. Modify `int_sqrt` to return ceiling sqrt.
3. Write predicate search to find minimum capacity to ship packages within D days (classic capacity planning).
4. Solve Peak Element using binary search reasoning.
5. Convert all core functions to recursive variants.

---
## 12. JavaScript Snippets (Optional)
```js
function binarySearch(nums, target){
  let l=0, r=nums.length-1;
  while(l<=r){
    const m = (l + r) >> 1; // bit shift floor
    if(nums[m] === target) return m;
    if(nums[m] < target) l = m + 1; else r = m - 1;
  }
  return -1;
}

function searchInsert(nums, target){
  let l=0, r=nums.length-1;
  while(l<=r){
    const m = (l+r)>>1;
    if(nums[m]===target) return m;
    if(nums[m] < target) l = m+1; else r = m-1;
  }
  return l;
}

function firstOccurrence(nums, target){
  let l=0, r=nums.length-1, ans=-1;
  while(l<=r){
    const m = (l+r)>>1;
    if(nums[m] >= target){
      if(nums[m]===target) ans=m;
      r = m-1;
    } else l = m+1;
  }
  return ans;
}
```

---
## 13. Resources
- NeetCode Binary Search (video + patterns)
- GeeksforGeeks Binary Search & boundary variants
- LeetCode Discuss: Binary search template III (predicate style)
- CP Handbook (monotonic predicate searching section)

---
## 14. Reflection
Prompts:
1. Which variant (exact / boundary / predicate) felt hardest and why?
2. Did you mix interval conventions anywhere?
3. One trigger tomorrow to recognize predicate search earlier?

Sample log: “Implemented exact + bounds + predicate; clarified half-open vs closed intervals; practiced rotated logic.”

---
## 15. Preview (Day 13)
Upcoming: Two-dimensional binary search & applying predicate to optimization (min capacity / time allocation) OR start on prefix sums.

End of Day 12 guide.