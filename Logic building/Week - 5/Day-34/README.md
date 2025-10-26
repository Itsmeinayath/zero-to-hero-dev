# Day 34: Linked Lists - Add Two Numbers & Reverse in Groups

## What you'll learn
- Add two numbers represented as linked lists (with carry handling)
- Reverse a linked list in groups of k nodes
- Master the dummy node pattern for building new lists
- Handle edge cases: different list lengths, final carry, partial groups

---

## Problem 1: Add Two Numbers (LeetCode 2)

### What problem are we solving?
Given two non-empty linked lists representing two non-negative integers, where digits are stored in **reverse order**, add the two numbers and return the sum as a linked list.

Example:
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
       Represents: 342 + 465
Output: [7, 0, 8]
        Represents: 807
```

Visual:
```
  2 → 4 → 3  (represents 342)
+ 5 → 6 → 4  (represents 465)
-----------
  7 → 0 → 8  (represents 807)
```

### Intuition: Elementary school addition
- Add digit by digit from right to left (but our lists are already reversed!)
- Track carry (0 or 1) from each addition
- Handle different list lengths
- Don't forget final carry if it exists

### Algorithm
```
1. Create dummy node to build result list
2. Initialize carry = 0, current = dummy
3. While l1 or l2 or carry exists:
   - Get val1 from l1 (or 0 if l1 is None)
   - Get val2 from l2 (or 0 if l2 is None)
   - Calculate: total = val1 + val2 + carry
   - New digit = total % 10
   - New carry = total // 10
   - Create new node with digit, append to result
   - Move l1, l2, current forward
4. Return dummy.next
```

### Step-by-step example: [2,4,3] + [5,6,4]
```
Step 1: 2 + 5 + 0(carry) = 7, digit=7, carry=0
        Result: [7]

Step 2: 4 + 6 + 0(carry) = 10, digit=0, carry=1
        Result: [7, 0]

Step 3: 3 + 4 + 1(carry) = 8, digit=8, carry=0
        Result: [7, 0, 8]

Both lists exhausted, no carry → done
```

### Python code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10
        
        current.next = ListNode(digit)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next
```

### Complexity
- Time: O(max(n, m)) - traverse both lists once
- Space: O(max(n, m)) - new list for result

### Key insight: Loop condition
The critical part is `while l1 or l2 or carry:` which handles:
- Lists of different lengths
- Final carry that creates an extra digit

---

## Problem 2: Reverse Linked List in Groups (GFG / LeetCode 25)

### What problem are we solving?
Given a linked list, reverse the nodes in groups of k. If the number of nodes is not a multiple of k, the remaining nodes stay as-is (or reverse them depending on variation).

Example:
```
Input: [1, 2, 3, 4, 5, 6, 7, 8], k = 3
Output: [3, 2, 1, 6, 5, 4, 7, 8]
        └─────┘ └─────┘ └───┘
        reverse reverse keep as-is (only 2 nodes)
```

Visual:
```
Original: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

Group 1 (k=3): 1 → 2 → 3  becomes  3 → 2 → 1
Group 2 (k=3): 4 → 5 → 6  becomes  6 → 5 → 4
Group 3 (k=3): 7 → 8      (only 2, keep as-is or reverse based on problem)

Result: 3 → 2 → 1 → 6 → 5 → 4 → 7 → 8
```

### Intuition: Process in chunks
- Break list into groups of k nodes
- Reverse each complete group
- Connect reversed groups together
- Handle remaining nodes (< k)

### Algorithm (iterative approach)
```
1. Count total nodes to know how many complete groups
2. Use dummy node for easier head handling
3. For each complete group of k:
   a. Save the node before group (prev)
   b. Reverse k nodes
   c. Connect prev to new head of reversed group
   d. Connect tail of reversed group to next part
4. Return dummy.next
```

### Helper function: Reverse k nodes
```python
def reverseKNodes(head, k):
    """Reverse first k nodes, return new head and tail"""
    prev = None
    current = head
    tail = head  # Will become tail after reversal
    
    for _ in range(k):
        if not current:
            return None, None  # Not enough nodes
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev, tail  # New head, old head (now tail)
```

### Python code (simplified version)
```python
def reverseKGroup(head, k):
    # Count nodes
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    current = head
    
    # Process complete groups
    while count >= k:
        # Reverse k nodes
        group_head = current
        prev = None
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Connect reversed group
        prev_group.next = prev  # New head of reversed group
        group_head.next = current  # Old head (now tail) points to next
        prev_group = group_head
        
        count -= k
    
    return dummy.next
```

### Complexity
- Time: O(n) - visit each node twice (count + reverse)
- Space: O(1) - only pointers (iterative solution)

---

## Common pitfalls

Add Two Numbers:
- Forgetting to check carry after both lists are exhausted
- Not handling None values when lists have different lengths
- Creating nodes with wrong syntax (Python uses `ListNode()`, not `new ListNode()`)

Reverse in Groups:
- Off-by-one errors in group counting
- Losing connection between groups
- Not handling remainder nodes correctly
- Forgetting to update prev_group pointer

---

## Quick checklist when coding

Add Two Numbers:
- Use dummy node to build result
- Loop condition: `while l1 or l2 or carry`
- Handle None: `val = node.val if node else 0`
- Calculate digit and carry correctly: `digit = total % 10`, `carry = total // 10`
- Return `dummy.next`, not `dummy`

Reverse in Groups:
- Count total nodes first
- Use dummy node for easier head handling
- Reverse exactly k nodes per group
- Connect prev_group → reversed_head → next_part
- Update prev_group after each group
- Handle remainder nodes based on problem variant

---

## Study Plan (Your Notes, Organized)

Problems:
- LeetCode 2 - Add Two Numbers ✓ Completed
- GFG - Reverse Linked List in Groups (Homework)
- LeetCode 25 - Reverse Nodes in k-Group (Similar)

Key learnings:
- **Dummy head pattern**: Simplifies building new lists from scratch
- **Loop condition mastery**: `while l1 or l2 or carry` handles all edge cases
- **Python syntax**: `ListNode()` not `new ListNode()`
- **Time complexity**: O(max(n,m)) for traversing both lists
- **Space complexity**: O(max(n,m)) when building new result list
- **Debugging skills**: Watch for typos in variable names

Next steps:
- Analyze recursive solution for reverse in groups
- Practice more group reversal variations
- Master connecting reversed segments



