# Day 33: Linked Lists - Middle Node & Nth from End

## What you'll learn
- Find the middle node using slow/fast pointers (Tortoise and Hare)
- Remove the Nth node from the end in one pass using two-pointer gap technique
- Master dummy node usage for edge case handling

---

## Problem 1: Middle of the Linked List

### What problem are we solving?
Given a singly linked list, return the middle node. If there are two middle nodes (even-length list), return the second middle node.

Example:
```
Input: [1, 2, 3, 4, 5]
Output: Node with value 3

Input: [1, 2, 3, 4, 5, 6]
Output: Node with value 4 (second middle)
```

### Intuition: Two-speed race
- Use two pointers: `slow` (1 step) and `fast` (2 steps)
- When `fast` reaches the end, `slow` is at the middle
- Why? Fast travels 2x distance, so when fast finishes, slow is halfway

Visual:
```
[1] → [2] → [3] → [4] → [5] → NULL
 ↑                              ↑
slow                          fast (start)

[1] → [2] → [3] → [4] → [5] → NULL
      ↑              ↑
    slow           fast (after 1 iteration)

[1] → [2] → [3] → [4] → [5] → NULL
           ↑                    ↑
         slow                 fast (end: slow at middle)
```

### Algorithm
```
1. Initialize slow = head, fast = head
2. While fast and fast.next exist:
   - Move slow one step
   - Move fast two steps
3. Return slow (it's at the middle)
```

### Python code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Complexity
- Time: O(n) - traverse list once
- Space: O(1) - only two pointers

---

## Problem 2: Remove Nth Node From End

### What problem are we solving?
Remove the nth node from the end of a linked list in one pass.

Example:
```
Input: [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]  (removed 4, which is 2nd from end)
```

### Intuition: Two-pointer gap
- Create a gap of n nodes between two pointers
- Move both together until the fast pointer reaches the end
- The slow pointer will be right before the node to delete

Visual (n=2):
```
Step 1: Create gap of 2
dummy → [1] → [2] → [3] → [4] → [5] → NULL
 ↑             ↑
slow          fast (moved n=2 steps)

Step 2: Move both until fast reaches end
dummy → [1] → [2] → [3] → [4] → [5] → NULL
                    ↑             ↑
                  slow           fast

Step 3: Delete node after slow
slow.next = slow.next.next
Result: [1] → [2] → [3] → [5]
```

### Why dummy node?
- Handles edge case: removing the head node
- Simplifies pointer logic (no special case needed)

### Algorithm
```
1. Create dummy node pointing to head
2. Set slow = dummy, fast = dummy
3. Move fast n steps ahead (create gap)
4. Move both pointers until fast.next is None
5. Delete: slow.next = slow.next.next
6. Return dummy.next
```

### Python code
```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    # Create gap of n nodes
    for _ in range(n):
        fast = fast.next
    
    # Move both until fast reaches last node
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    # Delete node after slow
    slow.next = slow.next.next
    
    return dummy.next
```

### Complexity
- Time: O(n) - one pass through the list
- Space: O(1) - constant extra space

---

## Step-by-step walkthrough

### Middle node example: [1, 2, 3, 4, 5]
```
Initial: slow=1, fast=1
Move 1:  slow=2, fast=3
Move 2:  slow=3, fast=5
Move 3:  fast.next=NULL, stop → slow=3 (middle)
```

### Remove 2nd from end: [1, 2, 3, 4, 5], n=2
```
Initial:  dummy→1→2→3→4→5, slow=dummy, fast=dummy
Gap:      fast moves 2 steps → fast=2
Together: slow=dummy→1, fast=2→3
Together: slow=1→2, fast=3→4
Together: slow=2→3, fast=4→5
Together: slow=3→4, fast=5→NULL.next, stop
Delete:   slow.next = slow.next.next (3→5, skipping 4)
Result:   1→2→3→5
```

---

## Common pitfalls
- Middle node: forgetting `while fast and fast.next` (causes null pointer error)
- Remove nth: not using dummy node (breaks when removing head)
- Remove nth: wrong gap creation or loop condition

---

## Quick checklist when coding
- [ ] Middle: check `fast and fast.next` in loop condition
- [ ] Remove nth: create dummy node first
- [ ] Remove nth: advance fast exactly n times
- [ ] Remove nth: loop until `fast.next` (not just `fast`)
- [ ] Remove nth: return `dummy.next`, not `head`

---

## Study Plan (Your Notes, Organized)

Problems completed:
- LeetCode 876 - Middle of the Linked List
- LeetCode 19 - Remove Nth Node From End of List

Key insights:
- Tortoise and Hare: fast moves 2x speed of slow
- Two-pointer gap: maintain n-node distance between pointers
- Dummy node: simplifies edge cases (especially removing head)
- One-pass solutions: more elegant than counting length first

Approach comparison:
- Middle node:
  - Brute: count length, traverse to length/2 (two passes)
  - Optimal: slow/fast pointers (one pass, O(1) space)
- Remove nth:
  - Brute: count length, traverse to (length-n)th node (two passes)
  - Optimal: two-pointer gap (one pass, O(1) space)

---

## How to run the demo

Run the standalone script:

```powershell
python .\linked_list_two_pointers_demo.py
```

Expected output shows both middle node and remove nth operations with examples.