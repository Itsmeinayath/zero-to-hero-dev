## Day 11 – Sliding Window
Timebox: ~3 hours (Theory 1h • Core problems 75–90m • Optional JS 20–30m • Reflection 5–10m)  
Commit: `Day 11: Sliding Window`  
Objective: Replace brute force subarray/substring scans (O(n^2)) with O(n) window passes (fixed & variable size).

### Learning Outcomes
- Explain difference between fixed vs variable window
- Derive O(n) complexity proof (each boundary advances ≤ n)
- Implement: max sum size k, max average, longest substring w/out repeat, minimum size subarray ≥ target (variant)
- Maintain frequency map or counters incrementally
- Avoid common pitfalls (forgot to shrink, double counting, resetting wrongly)

---
## 1. Quick Start (Read First – 60s)
Use Sliding Window when:
1. Problem involves contiguous range (subarray / substring).
2. Condition depends only on elements currently inside (or their aggregate) and can be updated in O(1) when you add/remove one element.

Two Families:
- Fixed-size: window length = k (e.g., max sum of k, average of k)
- Variable-size: expand end; shrink start until constraint valid (e.g., unique chars, sum >= target, at most K distinct)

Templates:
```python
# Fixed size k
window_sum = sum(a[:k]); best = window_sum
for i in range(k, len(a)):
    window_sum += a[i] - a[i-k]
    best = max(best, window_sum)

# Variable size
start = 0
for end, val in enumerate(a):
    # add val to state
    while condition_violated():
        # remove a[start] from state
        start += 1
    # update answer using (start, end)
```

Heuristic: If you would otherwise re-sum/re-count overlapping ranges repeatedly → window.

---
## 2. Core Concepts & Visuals

### 2.1 Complexity Intuition
Both pointers (`start`, `end`) only move forward → at most 2n moves. Each update O(1) → O(n) total.

### 2.2 Fixed vs Variable
Aspect | Fixed | Variable
-------|-------|---------
Window length | Constant k | Grows/Shrinks
When to slide | After k filled | While constraint violated
State example | Running sum | Sum + (maybe) frequency map
Examples | Max sum size k | Longest substring w/out repeat

### 2.3 Fixed Window Visual
Array: [2, 1, 5, 1, 3, 2], k=3
```
Indices: 0  1  2  3  4  5
Values : 2  1  5  1  3  2
Window : [2  1  5] sum=8 -> slide → remove 2 add 1 -> sum=7 -> slide -> remove1 add3 -> sum=9 (best)
```

### 2.4 Variable Window Visual (Longest Unique Substring: "abcabcbb")
```
start=0
end moves adding chars; maintain last seen index map
"a" -> ok (len=1)
"ab" -> ok (2)
"abc" -> ok (3)
Add 'a' again at end=3: last_seen['a']=0 >= start(0) → start = 0+1 =1
Window now "bca" length 3; continue similarly
Max length recorded =3
```

### 2.5 Common Variable Patterns
Goal | State Maintained | Shrink Condition
-----|------------------|-----------------
No repeat chars | char → last index / count | Duplicate present
At most K distinct | char frequency map | distinct_count > K
Sum <= target (or >=) | current sum | sum constraint broken
Min window covering set | counts of needed chars | all required satisfied → attempt shrink

### 2.6 Pitfalls & Fixes
Pitfall | Cause | Fix
--------|-------|----
Infinite loop | Not shrinking when invalid | Ensure shrink inside while
Wrong length | Updating answer before shrinking | For min problems measure AFTER shrinking to valid minimal
Negative counts | Removing more than added | Only decrement when char leaving window
Missing duplicates | Failing to update start using max(start, last_seen[c]+1) | Use max to avoid going backwards

---
## 3. Problem 1 – Max Sum Subarray of Size K (Fixed)
Goal: Highest sum of any contiguous subarray of length k.

Python:
```python
from typing import List

def max_sum_subarray_k(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        if window_sum > best:
            best = window_sum
    return best

assert max_sum_subarray_k([2,1,5,1,3,2], 3) == 9
assert max_sum_subarray_k([1,2,3], 2) == 5
```
Complexity: O(n) time / O(1) space.
Edge cases: k=1 (return max element); all negatives → still correct.

---
## 4. Problem 2 – Maximum Average Subarray I (Fixed)
Same as problem 1 but return average.
```python
def max_average_subarray_k(nums: List[int], k: int) -> float:
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        if window_sum > best:
            best = window_sum
    return best / k

assert abs(max_average_subarray_k([1,12,-5,-6,50,3],4) - 12.75) < 1e-9
```
Complexity: O(n) / O(1).
Edge cases: k = len(nums) → average entire array.

---
## 5. Problem 3 – Longest Substring Without Repeating Characters (Variable)
Goal: Length of longest substring with all unique chars.

Approach: Map each char to last index; when duplicate inside window, move start to one past previous index.
```python
def length_of_longest_unique(s: str) -> int:
    last = {}
    start = 0
    best = 0
    for end, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1  # shrink past duplicate
        last[ch] = end
        curr_len = end - start + 1
        if curr_len > best:
            best = curr_len
    return best

assert length_of_longest_unique("abcabcbb") == 3
assert length_of_longest_unique("bbbbb") == 1
assert length_of_longest_unique("") == 0
```
Complexity: O(n) time / O(m) space (m distinct chars).
Edge cases: empty string; all unique; all same.

---
## 6. Problem 4 – Minimum Size Subarray Sum ≥ Target (Variable)
Goal: Smallest length of subarray with sum ≥ target (return 0 if none).
```python
def min_subarray_len(target: int, nums: List[int]) -> int:
    start = 0
    curr_sum = 0
    best = float('inf')
    for end, v in enumerate(nums):
        curr_sum += v
        while curr_sum >= target:
            best = min(best, end - start + 1)
            curr_sum -= nums[start]
            start += 1
    return 0 if best == float('inf') else best

assert min_subarray_len(7, [2,3,1,2,4,3]) == 2  # [4,3]
assert min_subarray_len(15, [1,2,3,4,5]) == 5
assert min_subarray_len(100, [1,2,3]) == 0
```
Complexity: O(n) / O(1).
Edge cases: no valid subarray → 0; single element satisfies.

---
## 7. Decision Guide
Problem asks for... | Window Type | State Needed
--------------------|-------------|-------------
Fixed length aggregate | Fixed | Running sum
Max/Min length with constraint | Variable | Counts / sum
At most K distinct | Variable | Map char→count + distinct counter
No duplicates | Variable | Map char→last index
Min covering all required chars | Variable | Need counts of required + satisfied counter

---
## 8. Cheat Sheet
Pattern | Key Lines | Complexity
--------|-----------|-----------
Fixed sum k | `sum += a[i]-a[i-k]` | O(n)/O(1)
Longest unique | `if last[ch]>=start: start=last[ch]+1` | O(n)/O(m)
Min sum ≥ target | shrink while sum≥target | O(n)/O(1)
At most K distinct | while distinct>K: shrink | O(n)/O(K)

Proof gist: start & end only advance forward.

---
## 9. Pitfalls Recap
- Forgetting to shrink → O(n^2) disguised
- Moving start past needed point (use max for duplicate handling)
- Recomputing sum from scratch each slide (kills O(n))
- Off-by-one lengths (always end - start + 1)

---
## 10. Mini Exercises (Pick 2)
1. At most K distinct chars (return length) – adapt unique solution with a freq map.
2. Longest substring with at most 2 distinct (classic: "eceba" → 3)
3. Replace max average problem by tracking start index of best window.
4. Convert `min_subarray_len` to also return the actual subarray slice.
5. Add JS version for `length_of_longest_unique`.

---
## 11. JavaScript Snippets (Optional)
```js
// Fixed max sum size k
function maxSumSubarray(nums, k){
  let win = nums.slice(0,k).reduce((a,b)=>a+b,0);
  let best = win;
  for (let i=k;i<nums.length;i++){
    win += nums[i] - nums[i-k];
    if (win > best) best = win;
  }
  return best;
}

// Longest substring without repeating
function lengthOfLongestUnique(s){
  const last = new Map();
  let start=0, best=0;
  for (let end=0; end<s.length; end++){
    const ch = s[end];
    if (last.has(ch) && last.get(ch) >= start){
      start = last.get(ch) + 1;
    }
    last.set(ch, end);
    const len = end - start + 1;
    if (len > best) best = len;
  }
  return best;
}
```

---
## 12. Reflection
Prompts:
1. Which window problem felt clearest? Why?
2. Did you ever forget to shrink? How will you catch that earlier?
3. One mental trigger tomorrow to identify window suitability faster?

Log example: “Practiced fixed + variable windows; reinforced duplicate handling; comfortable with O(n) justification.”

---
## 13. Preview (Day 12)
Upcoming: Frequency maps + anagram windows OR At most K distinct expansions. Builds directly on today’s variable window.

End of Day 11 guide.
\n+---
## 14. Resources & Reinforcement

### 14.1 Core Videos (pick 1–2 first)
- NeetCode – Sliding Window intro + key variants (succinct pattern framing)
- Tushar Roy – Minimum Window / Unique substring (deeper reasoning walkthrough)
- Abdul Bari – Pointer intuition (helps mental model of advancing boundaries)
- Kevin Naughton Jr – Fast LeetCode pattern drills

### 14.2 Articles / Text
- GeeksforGeeks: Sliding Window Technique (foundational examples)
- NeetCode.io: Text mirrors of video explanations (quick skim)
- LeetCode Discuss tag: sliding-window (edge-case optimizations)
- Educative (Grokking) – Structured progression of window patterns

### 14.3 Practice Progression (Suggested Order)
1. Fixed size: Max sum size k, Max average
2. Unique constraints: Longest substring without repeat
3. Threshold shrinking: Min size subarray sum ≥ target
4. Distinct count: Fruits into baskets / At most K distinct
5. Replacement logic: Longest repeating character replacement
6. Coverage: Minimum window substring (introduces required counts deficit)
7. Structure upgrade: Sliding window maximum (deque variant – beyond basic) 

### 14.4 Advanced / Extensions
- Monotonic Deque: Sliding Window Maximum (maintain decreasing queue)
- Frequency Deficit Map: Minimum Window Substring / Anagram search
- Streaming Windows: Moving average from data stream (rolling, infinite input)
- Compare vs Alternatives: When prefix sums (range sum queries) or Kadane (max subarray any length) is simpler

### 14.5 5‑Day Reinforcement Micro Plan
Day 1: Read GFG + watch NeetCode intro; solve 2 fixed-size
Day 2: Longest unique + At most K distinct
Day 3: Min size subarray sum + Longest repeating character replacement
Day 4: Minimum window substring + Fruits into baskets timed
Day 5: Sliding window maximum + recap blank template + flashcards

### 14.6 Retention Drills
- Write both templates from memory (fixed / variable) at session start
- State invariant aloud (e.g., window always has no duplicates)
- Justify O(n) (each pointer advances forward only)
- Identify shrink condition explicitly before coding

### 14.7 Quick Self QA Checklist
| Question | Yes? |
|----------|------|
| Is problem contiguous? | |
| Can state update in O(1) on add/remove? | |
| Do I have explicit shrink condition? | |
| Am I updating answer at correct phase (after shrink for minimum)? | |
| Do I avoid re-scanning interior of window? | |

### 14.8 Optional Tools
- PyTutor / PythonTutor: Visualize pointer movement
- LeetCode Debugger: Step through shrinking loops
- Simple print tracing first submission (remove after AC)

### 14.9 Flashcard Seeds
- Template (fixed / variable) blanks
- Distinguish: Longest unique vs At most K distinct (state difference?)
- When is while vs if for shrinking? (Always while for full validity restoration)
- Why O(n)? (2 boundary pointers monotonic)

Use this section for spaced repetition; update with insights from mistakes.