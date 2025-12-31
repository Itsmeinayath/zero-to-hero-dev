# 🧠 Call Stack Memory Visualization

**Complete Step-by-Step Execution Flow**

This document shows exactly how the call stack grows and shrinks during function execution, **one step at a time**.

---

## 📝 The Code We're Analyzing

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

---

## 🎬 Phase 1: Building the Stack (PUSH Phase)

### Step 0: Program Starts

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│                  │                Program starts...
│     (empty)      │                
│                  │                
└──────────────────┘                
```

**Memory**: Stack is empty, ready for function calls.

---

### Step 1: `print1(1)` is Called

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print1(n=1)     │ ← SP           1
│  - n = 1         │                
│  - line: print() │                
└──────────────────┘                

Stack Size: 1 frame
Memory Used: ~48 bytes
```

**What Happens**:
1. ✅ `print1(n=1)` frame is **PUSHED** onto stack
2. ✅ Executes: `print(1)` → Output: **1**
3. ⏸️ About to call `print2(n=2)`, but hasn't called yet
4. 🔄 `print1` is now **WAITING** (paused)

---

### Step 2: `print2(2)` is Called from `print1`

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print2(n=2)     │ ← SP (NEW!)    1
│  - n = 2         │                2
│  - line: print() │                
├──────────────────┤                
│  print1(n=1)     │ ⏸️ PAUSED      
│  - waiting for   │                
│    print2()      │                
└──────────────────┘                

Stack Size: 2 frames
Memory Used: ~96 bytes
```

**What Happens**:
1. ✅ `print2(n=2)` frame is **PUSHED** onto stack
2. ✅ Executes: `print(2)` → Output: **2**
3. ⏸️ `print1` is still on the stack, **PAUSED**, waiting for `print2` to finish
4. 🔄 `print2` is now **WAITING** (about to call `print3`)

---

### Step 3: `print3(3)` is Called from `print2`

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print3(n=3)     │ ← SP (NEW!)    1
│  - n = 3         │                2
│  - line: print() │                3
├──────────────────┤                
│  print2(n=2)     │ ⏸️ PAUSED      
│  - waiting for   │                
│    print3()      │                
├──────────────────┤                
│  print1(n=1)     │ ⏸️ PAUSED      
│  - waiting for   │                
│    print2()      │                
└──────────────────┘                

Stack Size: 3 frames
Memory Used: ~144 bytes
```

**What Happens**:
1. ✅ `print3(n=3)` frame is **PUSHED** onto stack
2. ✅ Executes: `print(3)` → Output: **3**
3. ⏸️ Both `print1` and `print2` are **PAUSED** on the stack
4. 🔄 `print3` is now **WAITING** (about to call `print4`)

---

### Step 4: `print4(4)` is Called from `print3` - MAXIMUM DEPTH!

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print4(n=4)     │ ← SP (TOP!)    1
│  - n = 4         │                2
│  - line: print() │                3
├──────────────────┤                4
│  print3(n=3)     │ ⏸️ PAUSED      
│  - waiting for   │                
│    print4()      │                
├──────────────────┤                
│  print2(n=2)     │ ⏸️ PAUSED      
│  - waiting for   │                
│    print3()      │                
├──────────────────┤                
│  print1(n=1)     │ ⏸️ PAUSED      
│  - waiting for   │                
│    print2()      │                
└──────────────────┘                

Stack Size: 4 frames (PEAK!)
Memory Used: ~192 bytes
```

**What Happens**:
1. ✅ `print4(n=4)` frame is **PUSHED** onto stack
2. ✅ Executes: `print(4)` → Output: **4**
3. 🎯 **MAXIMUM DEPTH REACHED!** Stack is at its tallest
4. ✅ `print4` has **NO MORE FUNCTION CALLS** to make
5. 🔄 `print4` is now ready to **RETURN**

---

## 🔄 Phase 2: Unwinding the Stack (POP Phase)

### Step 5: `print4(4)` Completes and Returns

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print3(n=3)     │ ← SP (moved!)  1
│  - RESUMING!     │                2
│  - next: return  │                3
├──────────────────┤                4
│  print2(n=2)     │ ⏸️ PAUSED      
│  - waiting...    │                
├──────────────────┤                
│  print1(n=1)     │ ⏸️ PAUSED      
│  - waiting...    │                
└──────────────────┘                

Stack Size: 3 frames (↓)
```

**What Happens**:
1. ✅ `print4(n=4)` finishes execution
2. 🗑️ `print4` frame is **POPPED** (removed/destroyed from stack)
3. 💾 Memory freed: ~48 bytes
4. ▶️ Control returns to `print3` (the caller)
5. 🔓 `print3` **RESUMES** execution right after where it called `print4`

---

### Step 6: `print3(3)` Completes and Returns

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print2(n=2)     │ ← SP (moved!)  1
│  - RESUMING!     │                2
│  - next: return  │                3
├──────────────────┤                4
│  print1(n=1)     │ ⏸️ PAUSED      
│  - waiting...    │                
└──────────────────┘                

Stack Size: 2 frames (↓)
```

**What Happens**:
1. ✅ `print3(n=3)` finishes execution (nothing left to do)
2. 🗑️ `print3` frame is **POPPED** (removed/destroyed from stack)
3. 💾 Memory freed: ~48 bytes (total freed so far: ~96 bytes)
4. ▶️ Control returns to `print2` (the caller)
5. 🔓 `print2` **RESUMES** execution right after where it called `print3`

---

### Step 7: `print2(2)` Completes and Returns

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│  print1(n=1)     │ ← SP (moved!)  1
│  - RESUMING!     │                2
│  - next: return  │                3
└──────────────────┘                4

Stack Size: 1 frame (↓)
```

**What Happens**:
1. ✅ `print2(n=2)` finishes execution (nothing left to do)
2. 🗑️ `print2` frame is **POPPED** (removed/destroyed from stack)
3. 💾 Memory freed: ~48 bytes (total freed so far: ~144 bytes)
4. ▶️ Control returns to `print1` (the caller)
5. 🔓 `print1` **RESUMES** execution right after where it called `print2`

---

### Step 8: `print1(1)` Completes and Returns

```
CALL STACK                          CONSOLE OUTPUT
┌──────────────────┐                
│                  │                1
│     (empty)      │ ← SP (bottom!) 2
│                  │                3
└──────────────────┘                4

Stack Size: 0 frames (↓)
```

**What Happens**:
1. ✅ `print1(n=1)` finishes execution (nothing left to do)
2. 🗑️ `print1` frame is **POPPED** (removed/destroyed from stack)
3. 💾 Memory freed: ~48 bytes (total freed: ~192 bytes - all memory reclaimed!)
4. ▶️ Control returns to wherever `print1` was called from (main program)
5. ✅ **STACK IS NOW EMPTY** - Program can exit

---

## 📊 Summary Table

| Step | Action | Function | Stack Size | Memory Used | Output |
|------|--------|----------|------------|-------------|--------|
| 0 | Start | - | 0 | 0 bytes | - |
| 1 | PUSH | `print1(1)` | 1 | ~48 bytes | 1 |
| 2 | PUSH | `print2(2)` | 2 | ~96 bytes | 2 |
| 3 | PUSH | `print3(3)` | 3 | ~144 bytes | 3 |
| 4 | PUSH | `print4(4)` | 4 | ~192 bytes | 4 |
| 5 | **POP** | `print4(4)` ✅ | 3 ↓ | ~144 bytes | - |
| 6 | **POP** | `print3(3)` ✅ | 2 ↓ | ~96 bytes | - |
| 7 | **POP** | `print2(2)` ✅ | 1 ↓ | ~48 bytes | - |
| 8 | **POP** | `print1(1)` ✅ | 0 ↓ | 0 bytes | - |

---

## 🎯 Key Insights

### The LIFO Principle (Last-In, First-Out)

```
PUSH Order:  print1 → print2 → print3 → print4
POP Order:   print4 → print3 → print2 → print1
             (reverse!)
```

### Memory Growth Pattern

```
Stack Memory Over Time:

   ↑
192│        ┌──┐
144│     ┌──┤  │
 96│  ┌──┤  │  │
 48│┌─┤  │  │  │──┐
  0│┘ │  │  │  │  └──┐
   └──┴──┴──┴──┴─────┴→
     1  2  3  4  5  6  7  8  (steps)
     
     PUSH PHASE   POP PHASE
     (growing)    (shrinking)
```

### What Gets Stored in Each Frame?

```
┌─────────────────────────────┐
│ Stack Frame (32-64 bytes)   │
├─────────────────────────────┤
│ • Return Address            │ ← Where to jump back
│ • Previous Frame Pointer    │ ← Link to caller
│ • Parameters (n = ?)        │ ← Function arguments
│ • Local Variables           │ ← Function's data
│ • Instruction Pointer       │ ← What line we're on
└─────────────────────────────┘
```

---

## 🔍 Why This Matters for Recursion

### Recursion Uses the Same Pattern!

```python
def factorial(n):
    if n == 0:              # BASE CASE (stops the PUSH phase)
        return 1
    return n * factorial(n-1)  # RECURSIVE CALL (keeps PUSHing)

factorial(3)
```

**Stack Evolution**:

```
PUSH Phase:
factorial(3) → factorial(2) → factorial(1) → factorial(0)

Stack at Maximum:
┌──────────────┐
│ factorial(0) │ ← Returns 1 (BASE CASE!)
├──────────────┤
│ factorial(1) │ ← Waiting, needs result from factorial(0)
├──────────────┤
│ factorial(2) │ ← Waiting, needs result from factorial(1)
├──────────────┤
│ factorial(3) │ ← Waiting, needs result from factorial(2)
└──────────────┘

POP Phase (with values!):
factorial(0) returns 1
factorial(1) gets 1, computes 1*1=1, returns 1
factorial(2) gets 1, computes 2*1=2, returns 2
factorial(3) gets 2, computes 3*2=6, returns 6 ✅
```

---

## ⚠️ Stack Overflow Example

**What if there's NO base case?**

```python
def infinite(n):
    print(n)
    infinite(n + 1)  # ⚠️ Never stops!

infinite(0)
```

**Stack keeps growing**:

```
CALL STACK (Growing indefinitely...)
┌──────────────────────────────┐
│  infinite(1000)              │ ← Stack Pointer
├──────────────────────────────┤
│  infinite(999)               │
├──────────────────────────────┤
│  infinite(998)               │
├──────────────────────────────┤
│         ...                  │ (997 more frames)
├──────────────────────────────┤
│  infinite(3)                 │
├──────────────────────────────┤
│  infinite(2)                 │
├──────────────────────────────┤
│  infinite(1)                 │
├──────────────────────────────┤
│  infinite(0)                 │ ← Bottom
└──────────────────────────────┘

Memory Used: ~1000 frames × 48 bytes = ~48 KB

💥 Stack Memory Limit Reached!
RecursionError: maximum recursion depth exceeded
```

Python's default limit: ~1000 frames (varies by system)

---

## 🎓 Practice Exercise

Try to predict the stack for this code:

```python
def A():
    print("A")
    B()
    print("A done")

def B():
    print("B")
    C()
    print("B done")

def C():
    print("C")
    print("C done")

A()
```

**Challenge**: Draw the stack at each step and predict the output!

<details>
<summary>Click to see the answer</summary>

**Output**:
```
A
B
C
C done
B done
A done
```

**Stack Evolution**:
```
Step 1: A() → prints "A"
Step 2: A() calls B() → prints "B"
Step 3: B() calls C() → prints "C"
Step 4: C() → prints "C done", returns
Step 5: B() resumes → prints "B done", returns
Step 6: A() resumes → prints "A done", returns
```

</details>

---

**Made with ❤️ for understanding recursion at the memory level**
