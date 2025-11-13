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

## 🧠 Memory Management Deep Dive

### How Memory Works During Function Calls

When a program runs, memory is divided into different sections:

```
┌──────────────────────────────────────┐
│         PROGRAM MEMORY               │
├──────────────────────────────────────┤
│  Code Segment (Instructions)         │  ← Your actual code
├──────────────────────────────────────┤
│  Data Segment (Global Variables)     │  ← Static/global data
├──────────────────────────────────────┤
│  Heap (Dynamic Memory)               │  ← malloc, new, objects
│         ↓ grows down                 │
│                                       │
│         ↑ grows up                   │
│  Stack (Function Calls)              │  ← **THIS IS WHERE RECURSION LIVES!**
└──────────────────────────────────────┘
```

**The Call Stack (Stack Segment)** is where:
- Function calls are stored
- Local variables live
- Return addresses are saved
- Parameters are passed

---

## 🎨 Visual: Real Memory Management

### Example: Chain of Function Calls

```python
def print1(n):
    print(n)
    print2(n=2)

def print2(n):
    print(n)
    print3(n=3)

def print3(n):
    print(n)
    print4(n=4)

def print4(n):
    print(n)

print1(n=1)  # Start here!
```

### Memory Stack Evolution (Step-by-Step)

#### **Step 1: `print1(1)` is called**

```
STACK MEMORY (grows upward ↑)
┌────────────────────────────────┐
│  Frame: print1()               │ ← Stack Pointer (SP)
│  ├─ Parameter: n = 1           │
│  ├─ Local vars: None           │
│  ├─ Return address: main()     │
│  └─ Instruction: call print2() │
└────────────────────────────────┘
│ (empty space)                  │
└────────────────────────────────┘

Output so far: 1
```

#### **Step 2: `print2(2)` is called (push new frame)**

```
STACK MEMORY
┌────────────────────────────────┐
│  Frame: print2()               │ ← Stack Pointer (SP) moved up
│  ├─ Parameter: n = 2           │
│  ├─ Local vars: None           │
│  ├─ Return address: print1()   │
│  └─ Instruction: call print3() │
├────────────────────────────────┤
│  Frame: print1()               │ ← Still in memory, waiting
│  ├─ Parameter: n = 1           │
│  ├─ Return address: main()     │
│  └─ Status: PAUSED             │
└────────────────────────────────┘

Output so far: 1, 2
```

#### **Step 3: `print3(3)` is called (push another frame)**

```
STACK MEMORY
┌────────────────────────────────┐
│  Frame: print3()               │ ← Stack Pointer (SP)
│  ├─ Parameter: n = 3           │
│  ├─ Local vars: None           │
│  ├─ Return address: print2()   │
│  └─ Instruction: call print4() │
├────────────────────────────────┤
│  Frame: print2()               │ ← Waiting
│  ├─ Parameter: n = 2           │
│  ├─ Status: PAUSED             │
├────────────────────────────────┤
│  Frame: print1()               │ ← Waiting
│  ├─ Parameter: n = 1           │
│  ├─ Status: PAUSED             │
└────────────────────────────────┘

Output so far: 1, 2, 3
Stack size: 3 frames (24-48 bytes each)
```

#### **Step 4: `print4(4)` is called (maximum depth!)**

```
STACK MEMORY (MAXIMUM DEPTH)
┌────────────────────────────────┐
│  Frame: print4()               │ ← Stack Pointer (SP) at peak
│  ├─ Parameter: n = 4           │
│  ├─ Local vars: None           │
│  ├─ Return address: print3()   │
│  └─ Instruction: return        │ ← NO MORE CALLS!
├────────────────────────────────┤
│  Frame: print3()               │ ← Waiting
│  ├─ Parameter: n = 3           │
│  ├─ Status: PAUSED             │
├────────────────────────────────┤
│  Frame: print2()               │ ← Waiting
│  ├─ Parameter: n = 2           │
│  ├─ Status: PAUSED             │
├────────────────────────────────┤
│  Frame: print1()               │ ← Waiting
│  ├─ Parameter: n = 1           │
│  ├─ Status: PAUSED             │
└────────────────────────────────┘

Output so far: 1, 2, 3, 4
Stack size: 4 frames (~96-192 bytes)
```

### The Unwinding Phase (LIFO Pop)

#### **Step 5: `print4()` finishes and returns (pop frame)**

```
STACK MEMORY
┌────────────────────────────────┐
│  Frame: print3()               │ ← SP moved down (popped print4)
│  ├─ Parameter: n = 3           │
│  ├─ Status: RESUMED            │
│  └─ Next: return               │
├────────────────────────────────┤
│  Frame: print2()               │ ← Waiting
│  ├─ Parameter: n = 2           │
├────────────────────────────────┤
│  Frame: print1()               │ ← Waiting
│  ├─ Parameter: n = 1           │
└────────────────────────────────┘

print4 frame is DESTROYED (memory freed)
```

#### **Step 6: `print3()` returns (pop frame)**

```
STACK MEMORY
┌────────────────────────────────┐
│  Frame: print2()               │ ← SP moved down
│  ├─ Parameter: n = 2           │
│  ├─ Status: RESUMED            │
│  └─ Next: return               │
├────────────────────────────────┤
│  Frame: print1()               │ ← Waiting
│  ├─ Parameter: n = 1           │
└────────────────────────────────┘

print3 frame DESTROYED
```

#### **Step 7: `print2()` returns (pop frame)**

```
STACK MEMORY
┌────────────────────────────────┐
│  Frame: print1()               │ ← SP moved down
│  ├─ Parameter: n = 1           │
│  ├─ Status: RESUMED            │
│  └─ Next: return               │
└────────────────────────────────┘

print2 frame DESTROYED
```

#### **Step 8: `print1()` returns (pop frame)**

```
STACK MEMORY
┌────────────────────────────────┐
│  (empty - back to main)        │ ← SP at bottom
└────────────────────────────────┘

print1 frame DESTROYED
All functions completed!
```

---

## 📊 Memory Analysis

### Stack Frame Contents (What's stored for each function call)

```
┌───────────────────────────────────┐
│  STACK FRAME (typical 32-64 bytes)│
├───────────────────────────────────┤
│  Return Address (8 bytes)         │ ← Where to jump back
│  Previous Frame Pointer (8 bytes) │ ← Link to caller's frame
│  Parameters (varies)              │ ← Function arguments
│  Local Variables (varies)         │ ← Function's local data
│  Saved Registers (varies)         │ ← CPU state preservation
└───────────────────────────────────┘
```

### Space Complexity in Action

For `factorial(5)`:
- **5 stack frames** created
- Each frame ≈ 32-64 bytes
- **Total stack space**: ~160-320 bytes
- This is why we say **O(N) space complexity**!

### Stack Overflow Example

```python
def infinite_recursion(n):
    print(n)
    infinite_recursion(n + 1)  # ⚠️ NO BASE CASE!

infinite_recursion(0)
```

**What happens**:
```
Stack grows: frame₁ → frame₂ → frame₃ → ... → frame₁₀₀₀₀
Eventually: 💥 STACK OVERFLOW ERROR
"RecursionError: maximum recursion depth exceeded"
```

Python's default stack limit: ~1000 frames (can check with `sys.getrecursionlimit()`)

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

## 🎨 Want Even More Visual Details?

Check out **[MEMORY_VISUALIZATION.md](./MEMORY_VISUALIZATION.md)** for:
- 📍 **Step-by-step execution** with console output
- 🔄 **Complete push/pop phases** shown one function at a time
- 📊 **Memory graphs** showing stack growth and shrinkage
- 🎯 **Practice exercises** to test your understanding
- ⚠️ **Stack overflow examples** and prevention

---

**Made with ❤️ for interview prep**