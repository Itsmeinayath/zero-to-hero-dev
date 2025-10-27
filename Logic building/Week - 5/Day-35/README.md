# Day 35: Rest and Revise

Purpose
-------
This day is for consolidation: rest your mind, then actively revise everything you covered this week. The goal is not to learn new topics but to strengthen recall, fix weak spots, and convert passive notes into reliable understanding.

How to use this day
-------------------
- Spend the first 30–60 minutes away from the screen (walk, stretch, rest).
- Follow the short revision blocks below — alternate focused 25–40 minute sessions with 5–10 minute breaks (Pomodoro-style).
- Do the active-recall tasks before re-reading notes or code. Try to reproduce pseudocode and solutions from memory first.

Suggested schedule (4–5 hours total, flexible)
--------------------------------------------
1. Rest & reset — 30–60 minutes: step away, hydrate, short walk.
2. Quick topics sweep — 30 minutes: list the topics you learned this week from memory.
3. Active recall (3 × 40m sessions):
	- Session A: Core linked list operations (insert, delete, reverse) — 40m + 10m break
	- Session B: Two-pointer patterns (merge lists, middle/nth-from-end, cycle detection) — 40m + 10m break
	- Session C: Group/reduction patterns (add two numbers, reverse k-group, merge k lists overview) — 40m
4. Practice sprint — 60–90 minutes: re-solve 2–3 problems under time pressure (see list below).
5. Reflection & next steps — 15–20 minutes: note mistakes and add 2–3 follow-ups for tomorrow.

Core topics to revise (quick checklist)
-------------------------------------
- [ ] Linked list fundamentals: node structure, traversal, printing
- [ ] Insert at head/tail/middle; delete first/last/target node
- [ ] Reverse linked list (iterative and recursive)
- [ ] Add Two Numbers (carry handling; while l1 or l2 or carry)
- [ ] Merge two sorted lists (dummy node, two pointers)
- [ ] Merge k lists (pairwise / heap idea) — high-level
- [ ] Middle of list / Nth from end (slow/fast and gap technique)
- [ ] Cycle detection & cycle start (Floyd’s tortoise & hare)
- [ ] Reverse in groups (k-group iterative and idea for recursive)

Active-recall exercises (do these before re-reading):
------------------------------------------------
1. Without looking, write pseudocode for merging two sorted lists (dummy node approach).
2. From memory, write the loop condition and pointer updates for Floyd’s cycle detection.
3. Explain in 3 sentences why resetting slow to head finds the cycle start.
4. On paper, simulate reverse-in-groups for list [1..8] with k=3 and draw intermediate steps.

Practice problems (pick 2–3)
-----------------------------
- LeetCode 2 — Add Two Numbers
- LeetCode 21 — Merge Two Sorted Lists
- LeetCode 23 — Merge k Sorted Lists (review / plan only)
- LeetCode 19 — Remove Nth Node From End of List
- LeetCode 141 / 142 — Linked List Cycle / Cycle II
- LeetCode 25 — Reverse Nodes in k-Group

Mini-sprint rules
-----------------
- Timebox: 30–45 minutes per problem (first attempt without notes).  
- If stuck after 15 minutes, write what you tried, then resume with notes for the remaining time.  
- After solving, write a 1–2 line explanation of the idea and complexity.

Fix-it log (post-sprint)
-----------------------
- For each problem you re-solved, note the top 1–2 mistakes or gaps and how to fix them. Keep these as the first items for tomorrow’s practice.

Reflection prompts (5 minutes)
----------------------------
- Which topic felt weakest?  
- What specific example or edge case caused confusion?  
- What will I practice tomorrow to fix it?

Files & demo to run
-------------------
If you added demo scripts during the week (for Days 29–35), run them now to verify they still work and to re-familiarize with code structure. Example:

```powershell
python .\Day-32\cycle_detection_demo.py
python .\Day-33\linked_list_two_pointers_demo.py
python .\Day-34\linked_list_add_reverse_demo.py
```

Notes
-----
- Keep this day short and practical — aim for consolidation, not cram.  
- If you feel mentally exhausted, prioritize rest and only complete a short active recall (3–4 quick tasks).  

Next steps
----------
- Use the Fix-it log to seed Day 37 focused practice: pick 1–2 weakest topics and drill targeted problems.
- If everything feels solid, move on to the next week's topic but keep 2–3 review problems in your rotation.

Completed (tick when done)
-------------------------
- [ ] Rested 30–60 minutes
- [ ] Completed active-recall tasks
- [ ] Re-solved 2–3 practice problems
- [ ] Created Fix-it log and next-day targets