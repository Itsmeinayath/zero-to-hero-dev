## Day 15 - Linear Search & Search Strategy Foundations
Timebox: ~3 hrs (Concept 30m • Core problems 60–75m • Variants 30m • Comparisons 20m • Reflection 5–10m)  
Commit: `Day 15: Linear Search`

### Session Overview
Pattern Focus: Sequential scan (baseline) + recognizing when to upgrade to better patterns (binary search, hashing, prefix sums). Today you build intuition for scan cost & early exits.

End-of-day outputs:
- Implementations: basic linear search, sentinel linear search, search insert (linear + binary), first occurrence, count occurrences
- Decision triggers for switching away from linear
- Complexity comparison table (linear vs binary vs hashing)

### Learning Outcomes
- State linear search algorithm & O(n) proof in one sentence
- Recognize unsorted vs sorted data implications
- Use sentinel & early-exit micro-optimizations (understand their small impact)
- Justify when preprocessing (sorting/hash) amortizes cost
- Contrast brute / better / optimal for each demo problem

---
## 1. Quick Start
Linear search scans left→right until target found or list ends. Worst case touches every element ⇒ O(n). Use when: small n, unsorted data, one-off search where building indexes is wasteful.

Template:
```python
def linear_search(a, target):
    for i, v in enumerate(a):
        if v == target:
            return i
    return -1
```

---
## 2. Problem 1 – Basic Linear Search (Brute / Better / Optimal)
Goal: index of target or -1.

Brute:
- Approach: For-loop check each element.
- Complexity: O(n) time / O(1) space.
Better (micro):
- Early exit is already inherent; minor: iterate with while and manual index (no real gain) OR check last element separately via sentinel to reduce boundary tests inside loop.
Optimal (for unsorted single query):
- Same as brute—no asymptotic improvement without extra structure.

Python:
```python
def linear_search(nums, target):
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1
```
Edge: empty → -1; duplicates → returns first index.

Sentinel Variant (micro optimization demonstration):
```python
def linear_search_sentinel(nums, target):
    if not nums: return -1
    nums.append(target)  # sentinel
    i = 0
    while nums[i] != target:
        i += 1
    nums.pop()  # remove sentinel
    return i if i < len(nums) else -1
```
Note: Avoid if mutation problematic; educational only.

---
## 3. Problem 2 – Search Insert Position (Brute / Better / Optimal)
Goal: index of target or insertion index preserving sort.

Brute (linear): scan until >= target.
Better (guard): if target > last → return len(nums) early.
Optimal: binary search (O(log n)) – already learned; reuse template.

Linear Implementation:
```python
def search_insert_linear(nums, target):
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)
```

Optimal (Binary):
```python
def search_insert_binary(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target: return m
        if nums[m] < target: l = m+1
        else: r = m-1
    return l
```
Trade-off: For single tiny array n<20, linear simpler; for larger or repeated queries, binary wins.

---
## 4. Problem 3 – First Occurrence vs Any Occurrence
Brute: same as basic (returns first).
Better: If unsorted but you only care existence -> early return on first match (same complexity, improved average when target near front).
Optimal: Build hash map index for repeated queries to O(1) expected (preprocess O(n)).
```python
def first_occurrence(nums, target):
    for i,v in enumerate(nums):
        if v == target: return i
    return -1

def build_index(nums):
    from collections import defaultdict
    index = defaultdict(list)
    for i,v in enumerate(nums): index[v].append(i)
    return index  # query cost O(1) to fetch list
```

---
## 5. Problem 4 – Count Occurrences
Brute: traverse and increment counter.
Better: Python `sum(1 for x in nums if x==target)` (concise; same complexity).
Optimal (many queries): frequency dictionary built once.
```python
def count_occurrences(nums, target):
    c = 0
    for v in nums:
        if v == target: c += 1
    return c
```

---
## 6. Problem 5 – Min / Max Element
Brute: track best while scanning.
Better: Python built-ins `min(nums)`, `max(nums)` (implemented in C loops – still O(n)).
Optimal: For streaming updates keep running min/max; for range queries use segment tree / sparse table (future topics).
```python
def find_min(nums):
    if not nums: raise ValueError("empty")
    m = nums[0]
    for v in nums[1:]:
        if v < m: m = v
    return m
```

---
## 7. Decision Guide
Situation | Use Linear? | Upgrade To
----------|-------------|-----------
Single small unsorted list | Yes | —
Many repeated searches | No | Build hash / sort + binary search
Need ordered insertion index | Maybe small n | Binary search large n
Need min/max once | Yes | —
Need frequent range min queries | No | Segment tree (later)

Rule of Thumb: If preprocessing cost amortized over many queries, prefer structure; otherwise simple scan.

---
## 8. Complexity Comparison (Single Query)
Method | Preprocess | Query | Total (1 query) | Sorted Required
-------|-----------|-------|-----------------|----------------
Linear | 0 | O(n) | O(n) | No
Binary | O(n log n) (sort) | O(log n) | O(n log n) | Yes
Hash index | O(n) build | O(1) avg | O(n) | No

Break-even heuristic: If expected queries q > log n then sorting + binary may pay off; if q >> 1 then hashing often best (with memory trade-off).

---
## 9. Pitfalls & Fixes
Pitfall | Cause | Fix
--------|-------|----
Incorrect -1 return | Missing return outside loop | Ensure final return
Off-by-one insertion | Returning len-1 instead len | Return l (binary) or len(nums) for linear
Mutating list for sentinel & forgetting cleanup | Early return before pop | Always pop or avoid sentinel
Premature optimization | Overusing binary on tiny arrays | Measure / reason about n

---
## 10. Mini Exercises
1. Implement negative linear search returning last occurrence (scan reverse).  
2. Add case-insensitive search for list of strings.  
3. Given many queries, refactor with hash index and benchmark (conceptually).  
4. Write a function returning all indices of target (no extra pass).  
5. Implement linear search that stops if remaining length < known minimum position (contrived prune).  

---
## 11. JS Snippets
```js
function linearSearch(nums, target){
  for(let i=0;i<nums.length;i++) if(nums[i]===target) return i;
  return -1;
}

function searchInsertLinear(nums, target){
  for(let i=0;i<nums.length;i++) if(nums[i] >= target) return i;
  return nums.length;
}
```

---
## 12. Resources
- GFG: Linear Search basics
- Abdul Bari: Linear Search video
- LeetCode: 704 (Binary) for contrast, 35 (Insert position)
- Article: Hash tables vs array scans (any reputable CS blog)

---
## 13. Reflection
Prompts:
1. When would you never choose linear search now?  
2. Biggest mental trigger to switch to binary?  
3. Summarize trade-off: preprocessing vs per-query cost.

Sample Log: “Practiced linear + sentinel; clarified when to upgrade to binary/hash; reinforced O(n) boundaries.”

End of Day 15 guide.