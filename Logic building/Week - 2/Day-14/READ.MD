## Day 14 – Week 2 Rest & Reflection
Light cognitive load; consolidate patterns; set up spaced repetition. Commit: `Day 14: Week 2 Reflection`.

### 1. Purpose & Mindset
Today is for recovery + integration (no new heavy topics). Goal: surface weak links early, lock in strong ones, design next week’s focus.

### 2. Week 2 Coverage Snapshot
Day 8: Arrays (lists vs arrays, method complexity, fixed vs dynamic)  
Day 9: Strings (frequency, reversal, palindrome, anagram, sliding window intro)  
Day 10: Two Pointers (taxonomy, variant decisions, visuals)  
Day 11: Sliding Window (fixed + variable, min/longest variants)  
Day 12: Binary Search (exact, bounds, predicate, rotated)  
Day 13: Array & String Manipulation Recap (in-place + window consolidation)

### 3. Self‑Assessment Matrix (Fill 1–5)
Skill | Score | Notes / Specific Gap
------|-------|--------------------
Two Pointer identification | [ ] | 
Sliding window shrink condition | [ ] | 
Binary search boundary variants | [ ] | 
Predicate (answer space) search | [ ] | 
In-place compaction vs partition | [ ] | 
Frequency vs hashmap choice | [ ] | 
Time/space articulation (concise) | [ ] | 

If any score ≤3 → schedule 2 focused drills next week (see Section 10).

### 4. Lightning Diagnostic (Answer Without IDE)
1. Longest unique substring template: (write from memory).  
2. Condition to shrink in min subarray ≥ target?  
3. lower_bound vs upper_bound return difference?  
4. When do you prefer backfill vs forward merge?  
5. O(n) justification for sliding window in one sentence.  
6. Rotated array search: which inequality picks sorted half?  
7. Character replacement window validity test formula.  

Flag any hesitation >10s; add to flashcards.

### 5. Error Log (Populate From Memory)
| Date | Problem | Original Mistake | Root Cause | Fix Strategy |
|------|---------|------------------|-----------|--------------|
|      |         |                  |           |              |

### 6. Spaced Repetition Setup
Create/Update flashcards:
- Q: “Sliding window – min window shrink timing?” → A: After condition satisfied attempt to shrink while still valid.
- Q: “First vs last occurrence modification?” → A: Move boundary inward, record answer.
- Q: “Predicate search invariant?” → A: hi always points to a True candidate; lo to last False.
- Q: “When use counting array?” → A: Fixed, small contiguous alphabet (e.g., lowercase 26). 

Review schedule: Today (learn), Day 16 (1st review), Day 19, Day 24.

### 7. Flashcard Write (Do On Paper / Notes)
Write from memory then verify: fixed-size window template, variable window template, binary search (closed), lower_bound (half-open), first occurrence variant, in-place merge backwards, frequency signature for anagram grouping.

### 8. Low‑Effort Micro Drills (Optional ~20m Total)
1. Implement longest unique substring in <2 min.  
2. Implement lower_bound & upper_bound from scratch.  
3. Convert removeDuplicates to handle “allow at most 2 occurrences” variant.  
4. Min subarray length ≥ target timed (goal <2 min).  
5. Explain to imaginary interviewer the difference between partition vs compaction.  

### 9. Repo Hygiene
- Ensure each Day folder has README & (if exists) playground script.  
- Add missing docstrings where absent in utility functions.  
- Tag TODO comments for known weak areas (e.g., `# REVIEW: predicate bounds`).

### 10. Targeted Improvement Plan
Weak Area → Drill Pair (schedule early next week):
Binary search bounds → Re-do LC 34 + write table of transitions.  
Sliding window shrink hesitation → Solve LC 76 (min window substring) focusing on shrink loop tracing.  
Predicate search gap → Implement Koko Eating Bananas + Ship Packages capacity back-to-back.  
Two pointer confusion → Contrast problems requiring contiguity vs selection (explain why no window).  

### 11. Performance Tracking Template
| Problem | Last Time (mins) | Target Next | Errors | Next Attempt Date |
|---------|------------------|-------------|--------|-------------------|
| Longest unique substring |              | <2     |        |                 |
| Min subarray ≥ target |              | <2     |        |                 |
| Lower/Upper bound pair |              | <1.5   |        |                 |
| Rotated search |              | <2     |        |                 |

### 12. Reflection Prompts
1. Strongest pattern now? Why?  
2. Most frequent bug class this week?  
3. One meta improvement (process, not code) for next week?  
4. Energy curve: which hour did focus drop? Adjust schedule?  
5. Single sentence summary of Week 2 learning.  

Sample Log: “Consolidated window & binary search variants; need faster boundary recall; plan predicate drills early next week.”

### 13. Wellness / Recovery (Do Not Skip)
Sleep: Aim 7–8h. Light movement (walk/stretch) to offset late sessions. Hydrate. Avoid cramming tonight.

### 14. Week 3 Preview
Planned Themes:
- Prefix sums & difference arrays (range sum / range update)  
- Hash / frequency advanced (permutation inclusion, anagram windows)  
- More predicate binary search (capacities, thresholds)  
- Stack fundamentals (valid parentheses, monotonic stack intro preview)  
- Possibly start prefix product / two-sum style hashing recap consolidation.

Success Criteria Next Week:
- Recite prefix sum formula variant for inclusive/exclusive ranges
- Implement min window substring with clear commentary
- Solve at least one predicate BS capacity problem without reference

### 15. Optional Light Reading
- Blog: “Why sliding window is just controlled expansion + restoration of invariant.”  
- Article: Efficient boundary binary search templates.

### 16. Commit Reminder
After filling sections you want: commit with message `Day 14: Week 2 Reflection`.

End of Day 14 rest & reflection guide.