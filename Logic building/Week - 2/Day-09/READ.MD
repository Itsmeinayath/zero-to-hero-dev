## Day 9 – Strings (Python / DSA)

Timebox: ~3 hours  
Objective: Understand Python string fundamentals (immutability, slicing, traversal) and apply two core two‑pointer patterns.

## Learning outcomes
- Explain why strings are immutable and the impact on operations
- Use slicing (`s[a:b:c]`) for extraction and reversal
- Traverse efficiently with for / while and two pointers
- Normalize strings for comparison (lowercasing, filtering alphanumerics)
- Implement in‑place style algorithms on list-of-char representations
- State time & space complexity for each approach

---
## 1. Theory (~1 hour)
Definition: A Python string is an immutable sequence of Unicode code points. Any apparent “modification” builds a new string.

Key operations (complexity hints):
- `len(s)` O(1)
- Index access `s[i]` O(1)
- Slicing `s[a:b]` O(k) where k = slice length (creates new string)
- Concatenation in loop `res += ch` → O(n^2) anti‑pattern for large n → prefer `list.append()` + `''.join(list)`
- Membership test `x in s` O(n)
- Methods (each returns new string unless no change needed): `lower()`, `upper()`, `strip()`, `replace()`, `split()`, `join(iterable)` (join is O(total length))

Traversal patterns:
```python
for ch in s: ...              # simple value iteration
for i, ch in enumerate(s): ... # need index
i, j = 0, len(s)-1             # two-pointer inward scan
```

Two-pointer use cases today: reverse sequence, palindrome validation with character filtering.

Common pitfalls:
- Trying `s[0] = 'H'` (TypeError)
- Off‑by‑one in slices (remember end index excluded)
- Building strings via repeated concatenation inside loops

Mini mental model: Treat string as read‑only array of chars; create a list if you need in‑place swaps.

---
## 2. Practice (~2 hours)
Format per problem: Goal → Reasoning → Pseudocode → Code → Tests → Complexity → Edge cases / notes.

### Problem 1: Reverse String (LeetCode #344)
Goal: Reverse characters. LeetCode version supplies a list `s: list[str]` and expects in‑place O(1) extra space.

Reasoning:
- Use two indices swapping towards the center (classic two‑pointer). Stops at midpoint.
- Pythonic alternative for a pure string: `s[::-1]` (creates new string O(n) time & space).

Pseudocode:
```
left = 0; right = n-1
while left < right:
    swap s[left], s[right]
    left++, right--
return s
```

Code (list in‑place):
```python
from typing import List

def reverse_list_chars(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Helper for a string input (returns new string)
def reverse_string(s: str) -> str:
    # Using slicing (concise) – still O(n)
    return s[::-1]

chars = list("hello")
reverse_list_chars(chars)
assert ''.join(chars) == 'olleh'
assert reverse_string("a") == "a"
assert reverse_string("") == ""
```
Complexity (two‑pointer): Time O(n), Space O(1) extra.  
Why optimal: Each character touched constant times.

Edge cases: empty list, length 1, already palindromic, very long (confirm linear scaling).

### Problem 2: Valid Palindrome (LeetCode #125)
Goal: Return True if string is a palindrome considering only alphanumeric chars and ignoring case.

Reasoning:
- Two pointers from ends.
- Skip non‑alphanumeric via `str.isalnum()`.
- Lowercase comparison on the fly (avoid building a filtered copy for strict O(1) extra, though building once is also O(n) time & space).

Pseudocode:
```
i=0; j=n-1
while i<j:
    advance i while i<j and not alnum(s[i])
    advance j while i<j and not alnum(s[j])
    if lower(s[i]) != lower(s[j]): return False
    i++; j--
return True
```

Code:
```python
def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False
assert is_palindrome("") is True  # empty treated as palindrome
assert is_palindrome("0P") is False
```
Complexity: Time O(n) single scan; Space O(1) extra.

Alternative (simpler, extra memory):
```python
def is_palindrome_copy(s: str) -> bool:
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]
```
Trade‑off: Cleaner code vs O(n) extra space.

Edge cases: empty string, only punctuation, numeric palindromes ("1221"), mixed case.

### Optional mini exercises
- Count vowels in a string (return dict of counts) – O(n)
- First non‑repeating character (use frequency map) – O(n)
- Check if two strings are anagrams (sort O(n log n) or count O(n))
- Remove all duplicate characters keeping order (use set track) – O(n)

---
## 3. Reflection (~10 min)
Prompts:
- Which pattern felt clearer: two‑pointer reverse or palindrome filtering? Why?
- Did you accidentally try to mutate a string directly? How to avoid next time?
- One improvement for tomorrow (e.g., practice hash map + string combos)?

Commit message suggestion: `Day 9: Strings – reverse & palindrome`.

---
## Cheat sheet
```
len(s)                  O(1)
s[i]                    O(1)
s[a:b]                  O(k) creates new string
join(list_of_parts)     O(total length) (preferred over += in loop)
x in s                  O(n)
reverse (two-pointer)   O(n) / O(1) extra
palindrome check        O(n) / O(1) extra
```

### Tips & pitfalls
- Avoid `result += ch` inside large loops → build list then `''.join(parts)`
- Always think: “Does this create a new string?” before chaining methods repeatedly
- Use `islower()/isupper()/isalpha()/isalnum()` for clean filtering logic
- Validate empties & 1‑length early for clarity

---
## Appendix A – Common String Methods (selected)
| Method | Purpose | Notes |
|--------|---------|-------|
| s.lower() | Case normalize | New string (id changes) |
| s.strip() | Trim ends | `lstrip`, `rstrip` variants |
| s.replace(old, new[, count]) | Substitute | Full scan O(n) |
| s.split(sep) | Split to list | Without sep → splits on whitespace groups |
| sep.join(list) | Join pieces | Most efficient assembly |
| s.count(sub) | Count occurrences | O(n * m) worst if sub length m naive |
| s.find(sub) | First index or -1 | O(n * m) worst (no KMP) |
| s.startswith(prefix) | Prefix test | Optional start/end indices |
| s.isalnum() | Alnum test | Used in palindrome filter |

---
End of Day 9 guide.