## Day 13 – String Manipulation Recap & Pattern Consolidation
Timebox: ~3 hours (Review 40m • Core problems 60–70m • Extensions 30m • Drill 20m • Reflection 5–10m)  
Commit: `Day 13: String Manipulation Recap`

### Session Overview
Focus: Consolidate earlier string, two-pointer, and sliding window patterns; strengthen frequency map reasoning; ensure you can derive time/space quickly.

End-of-day outputs:
- Implemented: Valid Anagram, Longest Unique Substring, Valid Palindrome, Group Anagrams (optional), Longest Repeating Character Replacement (stretch)
- Comparison table (sort vs count vs hashing)
- Pitfall checklist (Unicode, case, normalization, window shrinking)
- Personalized trigger list: when to pick frequency array vs dict

Primary Links:
- LC 242 (Valid Anagram)
- LC 3 (Longest Substring Without Repeating Characters)
- LC 125 (Valid Palindrome)
- LC 49 (Group Anagrams)
- LC 424 (Longest Repeating Character Replacement)

### Learning Outcomes
- Distinguish fixed-length frequency vs dynamic window problems
- Use counting array for lowercase-only vs dict for general Unicode
- Maintain last-seen index vs frequency counts appropriately
- Derive O(n) sliding window justification succinctly
- Normalize input (case, alnum filter) safely

---
## 1. Quick Start Patterns
Pattern | Template Core | Use When
-------|---------------|---------
Frequency equality | Build count(s) then adjust with other | Anagram / permutation tests
Two-pointer filtering | l/r move inward validating condition | Palindrome, trimming
Sliding window expand/shrink | Expand right; while invalid shrink left | Unique / at most K distinct / replacements
Grouping by signature | Map canonical signature → bucket | Group anagrams

Minimal Slides:
```python
# Anagram count (lowercase)
cnt = [0]*26
for c in s: cnt[ord(c)-97]+=1
for c in t: cnt[ord(c)-97]-=1
return all(x==0 for x in cnt)

# Longest unique substring
last = {}; start=0; best=0
for i,ch in enumerate(s):
    if ch in last and last[ch] >= start:
        start = last[ch]+1
    last[ch]=i
    best = max(best, i-start+1)
```

---
## 2. Core Problem – Valid Anagram (LC 242)
Approaches:
1. Sort both strings: O(n log n) time, O(1)/O(n) space (depending) – simplest
2. HashMap counts: O(n) time, O(k) space (k distinct)
3. Fixed array (26) when guaranteed lowercase: O(n) time, O(1) space

Python:
```python
def is_anagram(s: str, t: str) -> bool:
    if len(s)!=len(t): return False
    count = [0]*26
    for c in s: count[ord(c)-97]+=1
    for c in t: count[ord(c)-97]-=1
    return all(x==0 for x in count)

assert is_anagram("anagram","nagaram") is True
assert is_anagram("rat","car") is False
```
Edge: unicode → fall back to dict.

---
## 3. Core Problem – Longest Substring Without Repeating (LC 3)
Sliding window with last index.
```python
def length_of_longest_unique(s: str) -> int:
    last = {}
    start = 0
    best = 0
    for i,ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        curr = i - start + 1
        if curr > best: best = curr
    return best

assert length_of_longest_unique("abcabcbb") == 3
assert length_of_longest_unique("bbbbb") == 1
```
Invariant: window s[start:i] has all unique chars.

---
## 4. Add-On – Valid Palindrome (LC 125)
Normalize + two-pointer.
```python
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        while l<r and not s[l].isalnum(): l+=1
        while l<r and not s[r].isalnum(): r-=1
        if s[l].lower()!=s[r].lower(): return False
        l+=1; r-=1
    return True

assert is_palindrome("A man, a plan, a canal: Panama")
assert not is_palindrome("race a car")
```
Time O(n), Space O(1) extra.

---
## 5. Add-On – Group Anagrams (LC 49)
Signature = tuple of 26 counts (lowercase assumption) or sorted string.
```python
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for w in strs:
        count = [0]*26
        for c in w: count[ord(c)-97]+=1
        groups[tuple(count)].append(w)
    return list(groups.values())

res = group_anagrams(["eat","tea","tan","ate","nat","bat"])
```
Time O(n * L * alphabet) or O(n * L log L) if using sorting.

---
## 6. Stretch – Longest Repeating Character Replacement (LC 424)
Allow up to k replacements to make substring all same char.
Key Trick: Track max frequency in window; if (window_size - max_freq) > k shrink.
```python
def character_replacement(s: str, k: int) -> int:
    from collections import defaultdict
    freq = defaultdict(int)
    start = 0
    best = 0
    maxf = 0
    for end,ch in enumerate(s):
        freq[ch]+=1
        if freq[ch] > maxf: maxf = freq[ch]
        while (end-start+1) - maxf > k:
            freq[s[start]]-=1
            start+=1
        best = max(best, end-start+1)
    return best
```
Note: maxf may be stale but safe (upper bound) → correctness preserved.

---
## 7. Decision Guide
Goal | Use | State
-----|-----|------
Check permutation equality | Frequency array/dict | counts
Find longest unique region | Sliding window (last index) | last positions
Normalize + compare ends | Two-pointer | indices
Group similar words | Signature mapping | dict sig→list
Window with limited edits | Sliding window + max freq | freq map + maxf

---
## 8. Complexity Cheat Sheet
Operation | Time | Extra Space
----------|------|------------
Frequency compare (lowercase) | O(n) | O(1)
Sort strings | O(n log n) | O(1)/O(n)
Longest unique window | O(n) | O(m distinct)
Palindrome check | O(n) | O(1)
Group anagrams (count sig) | O(n * L + n*alphabet) | O(n * alphabet)
Char replacement window | O(n) | O(m)

---
## 9. Pitfalls & Fixes
Pitfall | Cause | Fix
--------|-------|----
Unicode mismatch | Fixed 26 array on unicode | Use dict
Window shrink missing | Using if instead of while | Always while invalid
Case sensitivity errors | Forgot .lower() | Normalize both sides
Stale maxf confusion | Trying to recompute each shrink | Keep maxf; accept overestimation
Inefficient anagram grouping | Sorting each + large alphabet | Use count signature

---
## 10. Mini Drills (Pick 3–5)
1. Rewrite `is_anagram` using dict for arbitrary chars.
2. Modify palindrome to ignore accents (strip or normalize NFKD – conceptual note).
3. Adapt longest unique to return substring itself.
4. Group anagrams returning results sorted lexicographically inside each group.
5. Write a function to check if s contains a permutation of pattern p (fixed-size 26 count sliding window).

Permutation Inclusion Hint (LC 567): Maintain window count, compare to pattern count, shrink when window bigger than len(p).

---
## 11. JS Snippets (Optional)
```js
// Valid Anagram (assumes lowercase)
function isAnagram(s,t){
  if(s.length!==t.length) return false;
  const cnt = new Array(26).fill(0);
  for(const c of s) cnt[c.charCodeAt(0)-97]++;
  for(const c of t) if(--cnt[c.charCodeAt(0)-97] < 0) return false;
  return true;
}

// Longest Unique Substring
function lengthOfLongestUnique(s){
  const last = new Map();
  let start=0, best=0;
  for(let i=0;i<s.length;i++){
    const c = s[i];
    if(last.has(c) && last.get(c) >= start) start = last.get(c)+1;
    last.set(c,i);
    if(i-start+1 > best) best = i-start+1;
  }
  return best;
}
```

---
## 12. Resources
- NeetCode: Anagram / Longest Substring videos
- GFG: Python String Operations
- LeetCode Discuss patterns: Sliding window summary
- Official Unicode docs (normalization, optional deep dive)

---
## 13. Reflection
Prompts:
1. Which pattern (frequency vs sliding window) feels most automatic now?
2. One common pitfall you resolved today?
3. Write a one-liner rule for when to use a counting array.

Log sample: “Practiced frequency + window; clarified stale maxf concept; comfortable deriving O(n).”

---

End of Day 13 guide.