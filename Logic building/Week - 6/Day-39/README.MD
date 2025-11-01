# Day 39 - Stack Applications

## 📚 Purpose

A concise, interview-ready guide covering:
- **Deque fundamentals** and quick operations
- **Monotonic Deque pattern** for sliding-window problems
- **Custom implementation** using doubly-linked lists
- **Edge cases** and best practices

---

## 🎯 TL;DR

- **Deque** = Double-ended queue with O(1) operations at both ends
- Use Python's `collections.deque` in production
- Implement custom DLL-backed deque only when explicitly required
- Perfect for sliding-window problems and monotonic queue patterns

---

## ⚡ Quick Operations

```python
from collections import deque

dq = deque()

# Add operations
dq.append(x)       # Add to back - O(1)
dq.appendleft(x)   # Add to front - O(1)

# Remove operations
dq.pop()           # Remove from back - O(1)
dq.popleft()       # Remove from front - O(1)

# Access operations
dq[0]              # Peek front (check if not empty first)
dq[-1]             # Peek back
```

**Complexity**: All operations are **O(1)**

### 🔧 Common Use Cases

- Sliding-window maximum/minimum problems
- Monotonic queue patterns
- BFS level-order traversal
- Fixed-size ring buffers
- Palindrome checking

---

## 🎨 Pattern: Monotonic Deque - Sliding Window Maximum

### 💡 Core Idea

Maintain indices in the deque such that their corresponding values are **non-increasing**. The front index always points to the current window's maximum.

### 🧠 Why It Works

- Store **indices** (not values) to efficiently track and remove expired elements
- When a larger value arrives, remove all smaller values from the back
- When an index expires (falls outside window), remove it from the front

### 📝 Implementation

```python
from collections import deque
from typing import List

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    """
    Find the maximum in each sliding window of size k.
    
    Args:
        nums: List of integers
        k: Window size
        
    Returns:
        List of maximums for each window position
    """
    if not nums or k <= 0:
        return []
    
    q: deque[int] = deque()  # Stores indices (values are non-increasing)
    result: List[int] = []

    for i, val in enumerate(nums):
        # Remove indices outside the current window
        while q and q[0] <= i - k:
            q.popleft()

        # Remove indices with smaller values from the back
        while q and nums[q[-1]] <= val:
            q.pop()

        # Add current index
        q.append(i)

        # Once we've processed at least k elements, record the max
        if i >= k - 1:
            result.append(nums[q[0]])

    return result


# Test
if __name__ == '__main__':
    print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # Output: [3, 3, 5, 5, 6, 7]
```

### ⏱️ Complexity

- **Time**: O(n) — each index enters and exits the deque at most once
- **Space**: O(k) — deque size ≤ window size

### 💡 Pro Tip

Use `<=` in the while-removal condition to control tie behavior:
- `nums[q[-1]] < val` → keeps older duplicates
- `nums[q[-1]] <= val` → keeps newer duplicates

---

## 🛠️ Custom Implementation: `MyDeque` (Doubly-Linked List)

Use this when you need manual node control or when an interviewer explicitly asks for a from-scratch implementation.

### 📦 Complete Implementation

```python
class Node:
    """Node for doubly-linked list."""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyDeque:
    """Deque implementation using doubly-linked list."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        """Check if deque is empty."""
        return self.size == 0

    def add_front(self, val) -> None:
        """Add element to the front - O(1)."""
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def add_back(self, val) -> None:
        """Add element to the back - O(1)."""
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove_front(self):
        """Remove and return element from front - O(1)."""
        if self.is_empty():
            return None
        
        val = self.head.val
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return val

    def remove_back(self):
        """Remove and return element from back - O(1)."""
        if self.is_empty():
            return None
        
        val = self.tail.val
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return val

    def peek_front(self):
        """Get front element without removing - O(1)."""
        return self.head.val if self.head else None

    def peek_back(self):
        """Get back element without removing - O(1)."""
        return self.tail.val if self.tail else None

    def __len__(self):
        """Return size of deque."""
        return self.size

    def __repr__(self):
        """String representation of deque."""
        if self.is_empty():
            return "MyDeque([])"
        
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return f"MyDeque([{', '.join(values)}])"
```

### ⚠️ Edge Cases to Handle

| Scenario | Expected Behavior |
|----------|------------------|
| Remove from empty deque | Return `None` (or raise exception) |
| Remove from single-element deque | Clear both `head` and `tail` |
| Add to empty deque | Set both `head` and `tail` to new node |
| Peek on empty deque | Return `None` (or raise exception) |

---

## 🧪 Try It Out

### Quick Demo

```python
def demo():
    """Quick demo of collections.deque."""
    from collections import deque
    
    dq = deque()
    
    # Add elements
    dq.append(1)
    dq.appendleft(0)
    dq.append(2)
    
    print(f"Deque: {list(dq)}")  # [0, 1, 2]
    
    # Remove elements
    print(f"Pop left: {dq.popleft()}")   # 0
    print(f"Pop right: {dq.pop()}")      # 2
    print(f"Remaining: {list(dq)}")      # [1]


def test_custom_deque():
    """Test custom MyDeque implementation."""
    dq = MyDeque()
    
    dq.add_back(1)
    dq.add_front(0)
    dq.add_back(2)
    
    print(dq)  # MyDeque([0, 1, 2])
    
    print(f"Front: {dq.peek_front()}")   # 0
    print(f"Back: {dq.peek_back()}")     # 2
    
    dq.remove_front()
    dq.remove_back()
    
    print(dq)  # MyDeque([1])


if __name__ == '__main__':
    print("=== Collections Deque Demo ===")
    demo()
    print("\n=== Custom MyDeque Demo ===")
    test_custom_deque()
```

---

## 📊 Comparison: List vs Deque

| Operation | list | deque |
|-----------|------|-------|
| append (right) | O(1)* | O(1) |
| append (left) | O(n) | O(1) |
| pop (right) | O(1) | O(1) |
| pop (left) | O(n) | O(1) |
| Access by index | O(1) | O(n) |
| Memory | Contiguous | Non-contiguous |

*Amortized O(1)

---

## 🎓 Interview Tips

1. **Always use `collections.deque`** in production code — it's optimized and battle-tested
2. **Store indices in monotonic deque problems** — enables efficient expiration checks
3. **Handle edge cases first** in custom implementations:
   - Empty deque operations
   - Single-element transitions
   - Proper pointer updates
4. **Clarify return behavior** — should operations on empty deque return `None` or raise?

---

## 📝 Practice Problems

| Problem | Difficulty | Pattern |
|---------|-----------|---------|
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Monotonic Deque |
| [Implement Deque](https://practice.geeksforgeeks.org/problems/deque-implementations/) | Medium | DLL Implementation |
| [Max of Min for Every Window Size](https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size/) | Hard | Monotonic Deque |


---

**Made with ❤️ for interview prep**
