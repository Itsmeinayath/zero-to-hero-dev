 # 🫧 Day 17: Bubble Sort Mastery

## 🎯 Today's Goal: Master Comparison-Based Sorting

**Logic Focus**: Understanding the core mechanics of comparing adjacent elements and swapping them to place them in order.

### 📚 Part 1: Theory (Est. 1 hour)
- **Read**: GFG's "Bubble Sort"
- **Video**: Search "Bubble Sort algorithm explanation" on YouTube
- **Focus**: Understanding the step-by-step process

### 💻 Part 2: Practice (Est. 2 hours)
- **First Problem**: GFG - Bubble Sort Implementation
- **Second Problem**: LeetCode - Sort Colors (Dutch National Flag)

---

## 🎯 Today's Mission

Today we begin learning about sorting algorithms. We'll start with one of the simplest, **Bubble Sort**. While it's not efficient enough for real-world use, it's an excellent algorithm for learning the fundamental concepts of sorting, like comparing and swapping.

---

## 📖 Topic Explanation: Bubble Sort 🫧

### What is Bubble Sort?

**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The name comes from the way smaller or larger elements "bubble" to their correct position.

### 🔑 The Core Logic

In each pass through the array, the **largest unsorted element** will "bubble up" to its correct final position at the end of the unsorted portion. 

- After the **first pass** → largest element is at the very end
- After the **second pass** → second-largest element is in second-to-last position  
- And so on...

### 🧠 Simple Analogy

Imagine a line of people of different heights:
1. Compare the first two people and swap them if the shorter person is on the right
2. Then compare the second and third, and so on
3. By the time you reach the end of the line, the tallest person will have been swapped all the way to the end
4. Repeat this process, but ignore the last person because they're already in the correct spot

### 🎬 Visual Example: Sorting [5, 1, 4, 2]

```
🎯 Goal: Sort [5, 1, 4, 2] → [1, 2, 4, 5]

Pass 1: Bubble largest element (5) to the end
├── [5, 1, 4, 2] → Compare 5 and 1 → Swap → [1, 5, 4, 2]
├── [1, 5, 4, 2] → Compare 5 and 4 → Swap → [1, 4, 5, 2]
└── [1, 4, 5, 2] → Compare 5 and 2 → Swap → [1, 4, 2, 5] ✅
    Result: Largest element (5) is now at the end

Pass 2: Bubble second largest (4) to position
├── [1, 4, 2, 5] → Compare 1 and 4 → No swap → [1, 4, 2, 5]
└── [1, 4, 2, 5] → Compare 4 and 2 → Swap → [1, 2, 4, 5] ✅
    Result: Second-largest element (4) is now in place

Pass 3: Final check
└── [1, 2, 4, 5] → Compare 1 and 2 → No swap → [1, 2, 4, 5] ✅
    Result: Array is now sorted!
```

Today's Goal: Master Comparison-Based Sorting
Logic Focus: Understanding the core mechanics of comparing adjacent elements and swapping them to place them in order.

Part 1: Theory (Est. 1 hour)
Read: GFG’s “Bubble Sort”.

Your 90 day plan.txt has a video from NeetCode, which may be unavailable. A good YouTube search for a replacement is "Bubble Sort algorithm explanation".

Part 2: Practice (Est. 2 hours)
First Problem: GFG: Bubble Sort

Second Problem: LeetCode: Sort Colors

## 📝 Problem 1: GFG - Bubble Sort Implementation

**Goal**: Implement the Bubble Sort algorithm to sort a given array in ascending order.

### 🔄 Approach: Standard Bubble Sort with Optimization

**Explanation**: We use nested loops - the outer loop controls passes, inner loop performs comparisons and swaps. **Key optimization**: if a full pass completes with zero swaps, the array is sorted and we can stop early.

#### 📋 Pseudocode:
```
FUNCTION bubbleSort(arr):
  SET n = length of arr

  // Outer loop for the number of passes
  FOR i FROM 0 TO n - 1:
    SET swapped = False

    // Inner loop for comparing adjacent elements
    // Range shrinks each pass (largest elements already sorted)
    FOR j FROM 0 TO n - i - 2:
      IF arr[j] > arr[j+1]:
        SWAP arr[j] and arr[j+1]
        swapped = True

    // Early termination: if no swaps, array is sorted
    IF swapped == False:
      BREAK
```

#### 🐍 Python Implementation:
```python
def bubbleSort(arr: list[int]) -> None:
    n = len(arr)

    # Outer loop for each pass
    for i in range(n):
        swapped = False
        
        # Inner loop for comparisons
        # The last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if current element > next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swaps occurred, array is sorted
        if not swapped:
            break

# Test the implementation
test_array = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {test_array}")
bubbleSort(test_array)
print(f"Sorted: {test_array}")
```

#### 📊 Analysis:

**✅ Pros:**
- Very simple sorting logic to understand
- Works in-place with constant space

**❌ Cons:**
- Extremely inefficient for large lists
- Rarely used in practice

**⏱️ Time Complexity**: O(n²) - Nested loops lead to quadratic comparisons  
**💾 Space Complexity**: O(1) - In-place sorting, no extra memory scaling with input

---

## 📝 Problem 2: LeetCode - Sort Colors

**Goal**: Given an array with objects colored red (0), white (1), or blue (2), sort them in-place so objects of the same color are adjacent, in order red → white → blue.

**Example**: `[2, 0, 2, 1, 1, 0]` → `[0, 0, 1, 1, 2, 2]`

### 🥉 Approach 1: Brute Force (Library Sort)

**Explanation**: Use built-in sorting function.

```python
def sortColors_brute(nums):
    nums.sort()  # Simple but not allowed in interviews
```

**Analysis**: O(n log n) time - Usually forbidden in interviews as it doesn't demonstrate algorithmic knowledge.

### 🥈 Approach 2: Counting Sort (Better)

**Explanation**: Since we only have 3 values (0, 1, 2), count occurrences and reconstruct the array.

#### 📋 Pseudocode:
```
FUNCTION sortColors_counting(nums):
  CREATE counts = [0, 0, 0] // Count 0s, 1s, 2s

  // First pass: count occurrences
  FOR each number 'num' in nums:
    counts[num] = counts[num] + 1

  SET write_index = 0

  // Second pass: reconstruct array
  FOR color FROM 0 TO 2:
    FOR i FROM 0 TO counts[color] - 1:
      nums[write_index] = color
      INCREMENT write_index by 1
```

#### 🐍 Python Implementation:
```python
def sortColors_counting(nums):
    # Count occurrences of each color
    count_0 = count_1 = count_2 = 0
    
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:  # num == 2
            count_2 += 1
    
    # Reconstruct array
    index = 0
    # Place all 0s
    for _ in range(count_0):
        nums[index] = 0
        index += 1
    # Place all 1s
    for _ in range(count_1):
        nums[index] = 1
        index += 1
    # Place all 2s
    for _ in range(count_2):
        nums[index] = 2
        index += 1
```

**📊 Analysis:**
- **⏱️ Time**: O(n) - Two passes through array
- **💾 Space**: O(1) - Fixed size counts array
- **✅ Pro**: Very efficient in time
- **❌ Con**: Requires two passes (optimal solution uses one)

### 🥇 Approach 3: Dutch National Flag Algorithm (Optimal)

**Explanation**: Single-pass, in-place solution using three pointers.

#### 🎯 Three Pointer Strategy:
- **`low`**: Points where next 0 should go (starts at index 0)
- **`mid`**: Current element being processed (starts at index 0)  
- **`high`**: Points where next 2 should go (starts at last index)

#### 🔄 Algorithm Logic:
- If `nums[mid] == 0`: Swap with `nums[low]`, increment both `low` and `mid`
- If `nums[mid] == 1`: Just increment `mid` (already in correct place)
- If `nums[mid] == 2`: Swap with `nums[high]`, decrement `high` only (don't increment `mid` - need to check swapped element)

#### 📋 Pseudocode:
```
FUNCTION sortColors_optimal(nums):
  SET low = 0, mid = 0, high = length of nums - 1

  WHILE mid <= high:
    IF nums[mid] == 0:
      SWAP nums[low] and nums[mid]
      INCREMENT low by 1
      INCREMENT mid by 1
    ELSE IF nums[mid] == 1:
      INCREMENT mid by 1
    ELSE: // nums[mid] == 2
      SWAP nums[mid] and nums[high]
      DECREMENT high by 1
      // Don't increment mid - check swapped element
```

#### 🐍 Python Implementation:
```python
def sortColors_optimal(nums):
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:      # Red
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:    # White
            mid += 1
        else:                   # Blue (nums[mid] == 2)
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid!

# Test all approaches
test_colors = [2, 0, 2, 1, 1, 0]
print(f"Original: {test_colors}")
sortColors_optimal(test_colors)
print(f"Sorted: {test_colors}")
```

**📊 Analysis:**
- **⏱️ Time**: O(n) - Single pass through array
- **💾 Space**: O(1) - True in-place sorting
- **✅ Pros**: Most optimal solution, famous algorithm
- **❌ Con**: Three-pointer logic can be tricky initially

---

## 🎯 Summary

✅ **Bubble Sort**: Simple O(n²) algorithm perfect for learning sorting fundamentals  
✅ **Sort Colors**: Real problem showcasing optimization from O(n²) → O(n) → O(n) single-pass  
✅ **Key Concepts**: Adjacent comparisons, early termination, three-pointer techniques

**Next**: Practice implementing both algorithms and understand when each approach is optimal!