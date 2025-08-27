## Day 7 – Rest, Review & Consolidation (Revision of Days 1–6)
Purpose today: No new core topics. Solidify fundamentals (data types, variables, conditionals, loops, functions, Big‑O) and clean up weak spots. Light, high‑leverage work only.

### Outcomes
By end of today you can:
- Recall core Python data types & mutability traits without notes
- Choose the correct loop pattern (counted, for‑in, while) on first attempt
- Trace conditional & nested logic confidently
- Write / refactor functions with clear signature, docstring, return path
- State time complexities of simple operations & common loop + list patterns
- Identify at least 2 personal recurring mistakes & their fixes

---
## 1. High‑Level Recap (Days 1–6)
Day | Focus | Key Hooks
----|-------|----------
1 | Data types & variables | int/float/str/bool/list/dict; naming; reassignment
2 | Loops | for vs while; ranges; break / continue; off‑by‑one vigilance
3 | Conditionals | if / elif / else; nested logic; guard clauses
4 | Functions | def, params vs args, return vs print, scope, purity mindset
5 | Big‑O Basics | O(1)/O(n)/O(n^2); nested loops; early exit; space vs time tradeoffs
6 | Consolidation | Combined tasks; integrating loops + conditionals + functions + complexity thinking

Memory anchor: “Data → Control → Abstraction → Performance → Integration”.

---
## 2. Diagnostic Self‑Quiz (Write Answers Before Checking Notes)
1. List 3 immutable types & 2 mutable types.
2. What’s the difference between `return` and `print`? Provide a quick example.
3. Time complexity of: summing list elements; nested loop pair comparison; membership test in list vs set.
4. Show two ways to loop index + value over a list.
5. Rewrite a while loop counting 0→4 as a for loop (and vice versa).
6. When would you prefer an early `return` in a function?
7. Spot the bug: `for i in range(1, len(arr)): total += arr[i]` (what’s missing?).
8. Why can premature micro‑optimization slow learning right now?

Grade yourself: Any hesitation >5s = review target.

---
## 3. Consolidated Cheat Sheet
Category | Snippet | Notes
---------|---------|------
Variables | `x = 5` | Dynamic typing
Multiple assign | `a, b = 1, 2` | Tuple unpack
Swap | `a, b = b, a` | O(1)
Loop over list | `for x in items:` | Direct iteration
Index + value | `for i, x in enumerate(items):` | Zero‑based index
Range | `range(start, stop, step)` | stop excluded
While | `while cond:` | Ensure progress inside
Guard clause | `if not data: return` | Flatten nesting
Function | `def f(a=0): return a*2` | Default evaluated once
Docstring | `def f(): """Explain purpose."""` | Keep concise
List comprehension | `[x*x for x in arr]` | Readability if simple
List length | `len(arr)` | O(1)
Sum list | `sum(arr)` | O(n)
Add list end | `append()` | Amortized O(1)
Insert front | `insert(0, x)` | O(n)
Membership | `x in arr` | O(n) list, O(1) avg set/dict
Nested loops | double pass | O(n^2)
Early break | inside loop | Cuts average, not worst-case

Big‑O Micro Reference:
```
Single loop over n items           -> O(n)
Nested double loop (full cross)    -> O(n^2)
Loop with early break sometimes    -> Worst O(n), best O(1)
Building new list via comprehension -> O(n)
```

---
## 4. Targeted Micro Drills (Pick 3–5 Only)
Short (<5 min each). Stop when flawless.
1. Reverse a string using a loop (no slicing) – verify with slicing.
2. Count vowels in a sentence (case insensitive) – ensure O(n).
3. Write `max_value(nums)` manually (no built‑in), handle empty input.
4. Refactor function with nested ifs into guard clauses.
5. Predict output before running: nested loop printing i,j counts for small ranges.
6. Given list of numbers, build list of squares only for evens (traditional loop vs comprehension).
7. Add timing mentally: which is faster for large list: `in` membership using list vs set? Why?

---
## 5. Personal Error Pattern Log
Create a 2‑column list: (Error → Correction Strategy).
Examples:
- Off‑by‑one in `range(len(arr))` → Use `enumerate` unless index math needed.
- Returning None accidentally → Ensure every branch returns a value.
- Rebuilding string via `+=` in loop → Accumulate pieces in list, `''.join()`.
- Forgetting to reset accumulators → Initialize inside loop scope.

Write at least 2 real mistakes from earlier days + your fix habit.

---
## 6. Mini Integrated Exercise (15–20 min)
Task: Given a list of integers, produce a summary dict: `{ 'count': n, 'sum': total, 'mean': avg, 'max': max_val, 'min': min_val, 'evens': num_evens, 'odds': num_odds }`

Constraints:
- Single pass (O(n))
- No using built‑ins `sum`, `max`, `min` (implement manually for practice)
- Return result from a function (no prints inside logic)

Stretch: Add `'unique': count_of_unique_values` using a set (note space tradeoff O(n)).

Reflection: Identify operations cost (loop O(n), set adds O(1) avg each).

---
## 7. Complexity Spot‑Check
Mark each snippet with complexity before running:
Snippet A:
```
for i in range(n):
	for j in range(i, n):
		pass
```
Answer: O(n^2/2) -> O(n^2)

Snippet B:
```
for x in arr: break
```
Worst: O(1) (always executes one iteration then break)

Snippet C:
```
result = [x for x in arr if x % 2 == 0]
```
O(n)

If any answer >10s → revisit Big‑O notes.

---
## 8. Reflection & Journal Prompts
Answer succinctly:
1. Strongest area now?
2. Most fragile concept (needs reinforcement tomorrow)?
3. One pattern that saved lines of code this week?
4. Habit to adopt next week (e.g., always add doctest / assert for edge case)?
5. Describe Big‑O in one sentence you’d give a non‑technical person.

Commit message suggestion: `Day 7: Revision & consolidation (Days 1–6)`.

---
## 9. Light Optional Stretch (If Energy Left)
Pick just ONE:
- Rewrite two earlier small scripts adding type hints and docstrings.
- Convert a nested loop pattern into a function with early return.
- Benchmark naive string concatenation vs join for 50k small fragments (just to ‘feel’ performance difference).

Stop if fatigue appears; purpose is reinforcement, not burnout.

---
## 10. Preview (Day 8+)
Upcoming topics already started: Lists/arrays operations (Day 8), Strings (Day 9), Two‑Pointers (Day 10). Soon: Hash maps / frequency patterns, sliding window, and basic recursion.

Focus tomorrow: Continue building pattern recognition (strings & arrays synergy) without losing clarity on fundamentals.

---
End of Day 7 revision guide.
