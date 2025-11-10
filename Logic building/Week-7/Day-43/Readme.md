# Day 43 — Recursion Basics

**Topic**: Recursion & Backtracking (Recursion Basics)

---

## 📚 Purpose

Today marks the start of **Week 7**, the most important week for building "coding ability." The topic is **Recursion**.

The goal is to demystify recursion, prove it's not magic, and show that it's just a logical pattern based on **two "Commandments"** and the **Call Stack** (our Day 36 topic!).

---

## 🎯 TL;DR

**Recursion**: A function that calls itself.

**The 2 "Commandments"**:
1. **Base Case**: The "stopping condition" (the simplest possible problem).
2. **Recursive Case**: The "delegation" step, where the function calls itself with a smaller problem.

**The "Magic" Revealed**: Recursion is powered by the **Call Stack**. This is a LIFO (Last-In, First-Out) stack in memory that "pauses" and "resumes" function calls. My handwritten notes visualized this perfectly.

**Real-World Use**: Recursion is not for "toy problems" like factorial. It is the **only way** to solve problems with "nested" or "unknown" depth, such as File Systems, Trees, Graphs (DFS), and all of Backtracking.

---

## ⚡ Core Concept: The Call Stack

A recursive function "pauses" by pushing its state onto the **Call Stack (LIFO)**. It "resumes" when the function above it pops off and returns an answer.

---

## 🎭 The "CEO & Intern" Analogy

Think of recursion as a company hierarchy:

1. **`factorial(5)`** (The CEO) is called. It can't finish. It delegates by calling `factorial(4)`.
2. **`factorial(4)`** (The Manager) is "pushed" onto the stack. It delegates by calling `factorial(3)`.
3. ...This repeats until...
4. **`factorial(0)`** (The Intern) is "pushed" onto the stack.
5. **`factorial(0)`** hits the **Base Case**! It returns `1` and is popped.
6. **`factorial(1)`** un-pauses. It gets the `1`, finishes its job (`1 * 1 = 1`), returns `1`, and is popped.
7. This **"return back"** phase continues until the **`factorial(5)`** (The CEO) gets its answer and is popped.

---

## 🎨 Visual: Call Stack for `factorial(3)`

### The "Push" Phase (Going Down)

```
Call: factorial(3)
┌─────────────────────┐
│   factorial(3)      │ ← Waiting for factorial(2)
│   return 3 * f(2)   │
└─────────────────────┘

Call: factorial(2)
┌─────────────────────┐
│   factorial(2)      │ ← Waiting for factorial(1)
│   return 2 * f(1)   │
├─────────────────────┤
│   factorial(3)      │ ← Paused
│   return 3 * f(2)   │
└─────────────────────┘

Call: factorial(1)
┌─────────────────────┐
│   factorial(1)      │ ← Waiting for factorial(0)
│   return 1 * f(0)   │
├─────────────────────┤
│   factorial(2)      │ ← Paused
│   return 2 * f(1)   │
├─────────────────────┤
│   factorial(3)      │ ← Paused
│   return 3 * f(2)   │
└─────────────────────┘

Call: factorial(0) → BASE CASE!
┌─────────────────────┐
│   factorial(0)      │ ✅ BASE CASE
│   return 1          │ ← Returns immediately!
├─────────────────────┤
│   factorial(1)      │ ← Paused
│   return 1 * f(0)   │
├─────────────────────┤
│   factorial(2)      │ ← Paused
│   return 2 * f(1)   │
├─────────────────────┤
│   factorial(3)      │ ← Paused
│   return 3 * f(2)   │
└─────────────────────┘
```

### The "Pop" Phase (Returning Back)

```
factorial(0) returns 1
┌─────────────────────┐
│   factorial(1)      │ ← Resumes! Gets 1
│   return 1 * 1 = 1  │
├─────────────────────┤
│   factorial(2)      │ ← Paused
│   return 2 * f(1)   │
├─────────────────────┤
│   factorial(3)      │ ← Paused
│   return 3 * f(2)   │
└─────────────────────┘

factorial(1) returns 1
┌─────────────────────┐
│   factorial(2)      │ ← Resumes! Gets 1
│   return 2 * 1 = 2  │
├─────────────────────┤
│   factorial(3)      │ ← Paused
│   return 3 * f(2)   │
└─────────────────────┘

factorial(2) returns 2
┌─────────────────────┐
│   factorial(3)      │ ← Resumes! Gets 2
│   return 3 * 2 = 6  │ ✅ Final answer!
└─────────────────────┘

Stack is empty → factorial(3) = 6
```

---

## 🛠️ Implementation 1: GFG: Factorial

A "toy problem" to practice the two commandments.

**Analyze**: `5! = 5 * 4 * 3 * 2 * 1`

**Plan (The 2 Commandments)**:
- **Base Case**: `0! = 1`
- **Recursive Case**: `n! = n * (n-1)!`

---

### 📝 Final Code

```python
class Solution:
    def factorial(self, n: int) -> int:
        
        # 1. Base Case (The "Intern")
        if n == 0:
            return 1
        
        # 2. Recursive Case (The "Delegation")
        else:
            return n * self.factorial(n - 1)
```

---

### ⏱️ Complexity

- **Time**: O(N) — The function is called N times (e.g., `factorial(5)` calls `f(4)`, `f(3)`, `f(2)`, `f(1)`, `f(0)`).
- **Space**: O(N) — This is the **hidden cost**. Each of the N calls is stored on the Call Stack, so it uses N frames of memory.

---

## 🛠️ Implementation 2: GFG: Sum of Natural Numbers

Another "toy problem" to practice the pattern.

**Analyze**: `S(3) = 3 + 2 + 1`

**Plan (The 2 Commandments)**:
- **Base Case**: `S(0) = 0` (This is safer than `S(1)=1` to prevent stack overflow if `n=0`).
- **Recursive Case**: `S(n) = n + S(n-1)`

---

### 📝 Final Code

```python
class Solution:
    def sumOfNaturalNumbers(self, n: int) -> int:
        
        # 1. Base Case (The "Intern")
        if n == 0:
            return 0
        
        # 2. Recursive Case (The "Delegation")
        else:
            return n + self.sumOfNaturalNumbers(n - 1)
```

---

### ⏱️ Complexity

- **Time**: O(N) — The function is called N times.
- **Space**: O(N) — For the N calls stored on the Call Stack.

---

## 🎨 Visual: Call Stack for `sum(3)`

### The Journey Down (Push Phase)

```
Call: sum(3)
┌─────────────────────┐
│   sum(3)            │
│   return 3 + sum(2) │ ← Waiting...
└─────────────────────┘
        ↓ calls sum(2)

┌─────────────────────┐
│   sum(2)            │
│   return 2 + sum(1) │ ← Waiting...
├─────────────────────┤
│   sum(3)            │ ← Paused
└─────────────────────┘
        ↓ calls sum(1)

┌─────────────────────┐
│   sum(1)            │
│   return 1 + sum(0) │ ← Waiting...
├─────────────────────┤
│   sum(2)            │ ← Paused
├─────────────────────┤
│   sum(3)            │ ← Paused
└─────────────────────┘
        ↓ calls sum(0)

┌─────────────────────┐
│   sum(0)            │ ✅ BASE CASE!
│   return 0          │ ← Returns immediately
├─────────────────────┤
│   sum(1)            │ ← Paused
├─────────────────────┤
│   sum(2)            │ ← Paused
├─────────────────────┤
│   sum(3)            │ ← Paused
└─────────────────────┘
```

### The Journey Back (Pop Phase)

```
sum(0) returns 0
┌─────────────────────┐
│   sum(1)            │ ← Resumes!
│   return 1 + 0 = 1  │
├─────────────────────┤
│   sum(2)            │ ← Paused
├─────────────────────┤
│   sum(3)            │ ← Paused
└─────────────────────┘

sum(1) returns 1
┌─────────────────────┐
│   sum(2)            │ ← Resumes!
│   return 2 + 1 = 3  │
├─────────────────────┤
│   sum(3)            │ ← Paused
└─────────────────────┘

sum(2) returns 3
┌─────────────────────┐
│   sum(3)            │ ← Resumes!
│   return 3 + 3 = 6  │ ✅ Final answer!
└─────────────────────┘

Stack empty → sum(3) = 6
```

---

## 🔑 Key Takeaways

1. **Recursion = Base Case + Recursive Case** — Always write these two!
2. **Call Stack is LIFO** — Last function called is first to return
3. **Space Complexity Matters** — O(N) stack space is the hidden cost
4. **Visualize the Stack** — Draw it out to understand the flow
5. **Recursion shines for Trees/Graphs** — Not just toy problems!

---

**Made with ❤️ for interview prep**