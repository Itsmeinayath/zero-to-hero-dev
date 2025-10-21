# Day 32: Linked List Cycle Detection (Floyd’s Algorithm)

## What you’ll learn
- Detect if a linked list has a cycle using two pointers (Tortoise and Hare)
- Find the node where the cycle begins (Cycle II)
- Understand why it’s O(n) time and O(1) space

---

## Intuition: Two runners on a track
- Slow moves 1 step; Fast moves 2 steps
- If there’s no loop, Fast reaches the end → no meet
- If there’s a loop, Fast keeps lapping and will eventually meet Slow inside the loop

Visual:
```
head → a → b → c → d → e ↘
                ↑      f ← g
```
Slow and Fast will meet at some node inside the cycle if one exists.

---

## What problem are we solving?
- A linked list is like a chain of nodes. Normally, the last node points to NULL (end).
- Sometimes, by mistake or by design, a node points back to a previous node → it forms a circle (cycle).
- The questions we answer:
    1) Is there a cycle? (Yes/No)
    2) If yes, where does the cycle start?

Why two pointers work:
- Fast moves twice as quickly as Slow. On a circular track, a faster runner will always catch up with a slower runner.

---

## Problem 1: Detect Cycle (LeetCode 141)

Pseudocode:
```
Input: head
slow = head; fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

Edge cases to remember:
- Empty list or single node → False
- Self-loop (node.next is itself) → True

Python (iterative, O(1) space):
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## Problem 2: Find Cycle Start (LeetCode 142)

Key fact after a meeting happens: if you reset one pointer to head and then move both 1 step each, they will meet at the start of the cycle.

Why this works (short):
- Let: distance head→cycleStart = a, cycleStart→meeting = b, cycle length = c
- At meeting: fast moved 2k, slow moved k steps → 2k - k = k is a multiple of c
- Therefore, moving one pointer to head and both at 1 step leads them to meet at cycle start after a steps

Pseudocode:
```
slow = head; fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
return None
```

Python:
```python
def detect_cycle_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

---

## Complexity
- Time: O(n) — each pointer traverses at most a few passes
- Space: O(1) — constant extra pointers

---

## Step-by-step walkthrough (example)

Consider list: 3 → 2 → 0 → -4 → (back to 2)

Indices:   0   1   2    3
Values:   [3,  2,  0,  -4]
Cycle: tail connects to index 1 (value 2)

1) Detect cycle:
- Start: slow=3, fast=3
- Move1: slow=2, fast=0
- Move2: slow=0, fast=2
- Move3: slow=-4, fast=-4 → met → cycle exists

2) Find cycle start:
- Reset slow=head (3); fast stays at meeting (-4)
- Step together:
    - step1: slow=2, fast=2 → met at 2 → cycle start is node with value 2

This always works because the extra distance Fast covered is a multiple of the cycle length.

---

## Minimal runnable demo
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def attach_cycle(head, pos):
    # pos = index (0-based) of node to connect tail to; -1 for no cycle
    if pos < 0 or not head:
        return head
    tail = head
    idx = 0
    join = None
    while tail.next:
        if idx == pos:
            join = tail
        tail = tail.next
        idx += 1
    # check last node index
    if idx == pos:
        join = tail
    if join:
        tail.next = join
    return head

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def detect_cycle_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

if __name__ == "__main__":
    h = make_list([3, 2, 0, -4])
    attach_cycle(h, 1)  # cycle starts at value 2
    print("Has cycle?", has_cycle(h))  # True
    start = detect_cycle_start(h)
    print("Cycle starts at:", start.val if start else None)  # 2

    h2 = make_list([1, 2])
    print("Has cycle?", has_cycle(h2))  # False
    print("Cycle starts at:", detect_cycle_start(h2))  # None
```

---

## Common pitfalls
- Forgetting the safety check: `while fast and fast.next:`
- Returning the meeting node instead of resetting to head for Cycle II
- Handling empty list or single node incorrectly

---

## Quick practice
- LeetCode 141: Linked List Cycle (detect boolean)
- LeetCode 142: Linked List Cycle II (return cycle start node)

Use the demo above to sanity-check your logic before submitting.

---

## Quick checklist when coding
- [ ] Handle empty list / single node first
- [ ] Use `while fast and fast.next:` for safety
- [ ] Move slow by 1, fast by 2
- [ ] For Cycle II: after meeting, set slow=head and move both by 1
- [ ] Return the node when slow == fast (that’s the cycle start)

---

## Study Plan (Your Notes, Organized)

Theory (≈1 hour):
- Learn Floyd’s cycle detection (tortoise and hare)
- Watch: Tushar Roy — Cycle Detection (20 min)
- Read: GFG — Detect Loop in a Linked List (20 min)

Practice (≈2 hours):
- LeetCode 141 — Linked List Cycle
    - Brute force: hash set (O(n) space)
    - Optimal: Floyd’s algorithm (O(1) space), O(n) time
    - Pseudocode:
        ```
        slow = head; fast = head
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast: return True
        return False
        ```
- LeetCode 142 — Linked List Cycle II
    - Find the node where the cycle begins
    - Pseudocode:
        ```
        slow = head; fast = head
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                        slow = head
                        while slow != fast:
                                slow = slow.next
                                fast = fast.next
                        return slow
        return None
        ```

Suggestion: Draw the pointer moves for a small example to build intuition.

---

## Resources
- Article: GFG — Detect Loop in a Linked List — https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
- Practice:
  - LeetCode 141 — Linked List Cycle
  - LeetCode 142 — Linked List Cycle II

---

## Quick reference (cheat sheet)

Detect cycle (bool):
```
slow=head; fast=head
while fast and fast.next:
    slow=slow.next; fast=fast.next.next
    if slow==fast: return True
return False
```

Find cycle start (node):
```
slow=head; fast=head
while fast and fast.next:
    slow=slow.next; fast=fast.next.next
    if slow==fast:
        slow=head
        while slow!=fast:
            slow=slow.next; fast=fast.next
        return slow
return None
```
t: None
```