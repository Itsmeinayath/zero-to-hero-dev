# Day 41 — Stack Recap & Patterns

**Topic**: Stacks & Queues (Recap & Mixed Practice)

---

## 📚 Purpose

Today is a recap day to solidify the advanced stack patterns we've learned. The goal is to prove our understanding by re-applying the Monotonic Stack pattern to a new problem and to practice basic LIFO mechanics.

- **Monotonic Stack Pattern**: Solved LeetCode: Daily Temperatures.
- **Basic LIFO Practice**: Solved GFG: Reverse a String using Stack.

---

## 🎯 TL;DR

**Monotonic Stack**: This is the key pattern for "Next Greater/Warmer Element" problems. The "chutiyapaa" O(N²) nested loop is a trap.

**Key Trick**: For "Daily Temperatures," we store **INDICES** on the stack, not values. This lets us calculate the distance.

**Smart Setup**: Pre-filling the `result = [0] * n` list is much cleaner than trying to append answers later.

**LIFO = Reversing Machine**: A stack naturally reverses any sequence. The 2-loop (Push-all, Pop-all) algorithm is the standard way to use a stack for this.

---

## 🎨 Pattern 1: Monotonic Stack — "Daily Temperatures" (Medium)

This is a classic "Next Greater Element" problem. The logic is nearly identical to "Next Greater Element I" (Day 39).

---

### 💡 Core Idea ("The Line of Waiters")

**Brute-Force (Trap)**: O(N²) nested loops to find the next warmer day. This is too slow.

**Optimal (Aha! Moment)**: Use a **Monotonic Decreasing Stack**.
- The stack will hold the **INDICES** of "waiter" days.
- We keep the stack sorted by temperature (decreasing).
- `result = [0] * n` is our pre-filled answer sheet.

---

### 🧠 The Algorithm (For each day i)

1. **Check Waiters**: Get the `current_temp = temperatures[i]`.
2. **Process**: `while stack and current_temp > temperatures[stack[-1]]:`
   - The new `current_temp` is the answer for the "waiter" on top.
   - `waiter_index = stack.pop()`
   - `distance = i - waiter_index`
   - `result_list[waiter_index] = distance` (Update the answer at the waiter's index)
3. **Add New Waiter**: `stack.append(i)` (The current day i now waits for its warmer day).
4. **Finish**: Any index left on the stack at the end never found a warmer day. Its answer is already 0, so we are done.

---

### 📝 Implementation (LeetCode 739)

```python
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result_list = [0] * n  # Pre-fill with default answer
        stack = []             # Will hold INDICES of "waiters"

        # Loop through every day
        for i in range(n):
            current_temp = temperatures[i]
            
            # 1. Process all "waiters" this temp is warmer than
            while stack and current_temp > temperatures[stack[-1]]:
                waiter_index = stack.pop()
                distance = i - waiter_index
                result_list[waiter_index] = distance # Update the answer

            # 2. Add current day's INDEX as a new "waiter"
            stack.append(i)
        
        return result_list
```

---

### ⏱️ Complexity

- **Time**: O(N) — Amortized. Each index is `append()`ed and `pop()`ed at most once.
- **Space**: O(N) — Worst case (`[70, 60, 50]`), the stack holds all N indices.

---

## 🛠️ Exercise 2: Basic LIFO — "Reverse a String using Stack" (Easy)

### 💡 Core Idea (LIFO = Reversing Machine)

This is an exercise to practice LIFO, not a real-world string reversal problem.

**The "Chutiyapaa" Trap**: Using `s[::-1]`. This is a Python trick, but it doesn't use a stack as the problem requires.

**The LIFO Logic**: A stack is a "natural reversing machine." The last item you put in (`'o'`) is the first one you get out.

---

### 🧠 The 2-Loop Algorithm

1. **"Pushing Loop"**: Loop through the input string `s` from start to end. `push` (append) every character onto the stack.
   - `s = "Hello"` → `stack = ['H', 'e', 'l', 'l', 'o']` (TOP)

2. **"Popping Loop"**: Loop `while stack:`. `pop` each character and add it to a `result_string`.
   - `pop()` → `'o'`, `result_string = "o"`
   - `pop()` → `'l'`, `result_string = "ol"`
   - ...and so on, until the stack is empty.

3. **Return** the `result_string`.

---

### 📝 Implementation (GFG)

```python
class Solution:
    def reverse(self, s: str) -> str:
        
        stack = []
        result_string = ""

        # 1. "Pushing Loop": Add all chars to the stack
        for char in s:
            stack.append(char)

        # 2. "Popping Loop": Build the new string from the stack
        while stack:
            result_string += stack.pop()
        
        return result_string
```

---

### ⏱️ Complexity

- **Time**: O(N) — O(N) to push all chars, O(N) to pop all chars. O(2N) → O(N).
- **Space**: O(N) — The stack must store all N characters.

---
