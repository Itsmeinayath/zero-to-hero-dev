# 📚 Day 18: Selection Sort - Complete Learning Guide

## 🎯 Learning Objectives
By the end of this session, you will:
- Understand the Selection Sort algorithm and its working principle
- Implement Selection Sort with different optimization levels
- Compare Selection Sort with other sorting algorithms
- Solve minimum element finding problems efficiently

---

## 📖 What is Selection Sort?

**Selection Sort** is a simple comparison-based sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion and placing it at the beginning. It divides the array into two parts: sorted and unsorted.

### 🔍 Key Characteristics:
- **Time Complexity**: O(n²) in all cases
- **Space Complexity**: O(1) - In-place sorting
- **Stability**: Not stable (can change relative order of equal elements)
- **Adaptive**: No (always performs the same number of comparisons)

### 🌟 How It Works:
1. Find the minimum element in the entire array
2. Swap it with the first element
3. Find the minimum in the remaining unsorted portion
4. Swap it with the second element
5. Repeat until the entire array is sorted

---

## 🎬 Visual Example

Let's trace through sorting `[64, 25, 12, 22, 11]`:

```
Initial: [64, 25, 12, 22, 11]
         ↑ unsorted portion

Step 1: Find min(64,25,12,22,11) = 11, swap with first
Result: [11, 25, 12, 22, 64]
             ↑ unsorted portion

Step 2: Find min(25,12,22,64) = 12, swap with second
Result: [11, 12, 25, 22, 64]
                 ↑ unsorted portion

Step 3: Find min(25,22,64) = 22, swap with third
Result: [11, 12, 22, 25, 64]
                     ↑ unsorted portion

Step 4: Find min(25,64) = 25, already in place
Result: [11, 12, 22, 25, 64]
                         ↑ unsorted portion

Final:  [11, 12, 22, 25, 64] ✅ SORTED
```

---

## 📚 Learning Resources

### 🎥 Video Resources (Theory - 1 hour):
1. **Abdul Bari's "Selection Sort"** (15 min) - [YouTube](https://www.youtube.com/watch?v=xWBP4lzkoyE)
   - Clear explanation with step-by-step visualization
2. **CS50's Sorting Algorithms** (20 min) - Visual comparison with other sorts
3. **mycodeschool Selection Sort** (10 min) - Implementation walkthrough

### 📄 Article Resources:
1. **GeeksforGeeks Selection Sort** (20 min) - [Link](https://www.geeksforgeeks.org/selection-sort/)
   - Comprehensive implementation and analysis
2. **Programiz Selection Sort** (15 min) - Interactive examples
3. **Khan Academy Sorting** - Mathematical analysis

---

## 🛠️ Problem 1: Selection Sort Implementation

**Problem**: Implement selection sort to sort an array in ascending order.
**Link**: [GeeksforGeeks Selection Sort](https://www.geeksforgeeks.org/selection-sort/)

### 🔨 Approach 1: Brute Force (Basic Implementation)

**Algorithm Logic**:
- Use nested loops to find minimum element
- Swap minimum with current position
- Continue for all positions

**Pseudocode**:
```
ALGORITHM SelectionSort(array):
    n = length of array
    
    FOR i = 0 to n-2:
        min_index = i
        
        FOR j = i+1 to n-1:
            IF array[j] < array[min_index]:
                min_index = j
        
        SWAP array[i] with array[min_index]
    
    RETURN array
```

**Python Implementation**:
```python
def selection_sort_basic(arr):
    """
    Basic Selection Sort Implementation
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Find minimum element in remaining unsorted array
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Optional: Print step for visualization
        print(f"Step {i+1}: {arr}")
    
    return arr

# Test the implementation
test_array = [64, 25, 12, 22, 11]
print("Original array:", test_array)
result = selection_sort_basic(test_array.copy())
print("Sorted array:", result)
```

**Complexity Analysis**:
- **Time**: O(n²) - Always performs n(n-1)/2 comparisons
- **Space**: O(1) - Only uses constant extra space
- **Comparisons**: n(n-1)/2 in all cases
- **Swaps**: At most n-1 swaps

### 🚀 Approach 2: Better Implementation (Optimized)

**Optimizations**:
- Early termination when no swaps needed
- Better variable naming and code structure
- Input validation

**Python Implementation**:
```python
def selection_sort_optimized(arr):
    """
    Optimized Selection Sort with early termination
    Time: O(n²), Space: O(1)
    Best case: O(n) when array is already sorted
    """
    if not arr or len(arr) <= 1:
        return arr
    
    n = len(arr)
    
    for i in range(n - 1):
        min_idx = i
        
        # Find minimum element index
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Only swap if minimum is not already in correct position
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Optional: Early termination check
        # If remaining elements are already sorted
        is_sorted = True
        for k in range(i + 1, n - 1):
            if arr[k] > arr[k + 1]:
                is_sorted = False
                break
        
        if is_sorted:
            break
    
    return arr

# Test with different cases
test_cases = [
    [64, 25, 12, 22, 11],
    [1, 2, 3, 4, 5],  # Already sorted
    [5, 4, 3, 2, 1],  # Reverse sorted
    [1],               # Single element
    []                 # Empty array
]

for i, test in enumerate(test_cases):
    result = selection_sort_optimized(test.copy())
    print(f"Test {i+1}: {test} → {result}")
```

### 🎯 Approach 3: Optimal Implementation (Production-Ready)

**Features**:
- Generic comparison function
- Support for custom key functions
- Comprehensive error handling
- Detailed documentation

**Python Implementation**:
```python
def selection_sort_optimal(arr, key=None, reverse=False):
    """
    Production-ready Selection Sort implementation
    
    Args:
        arr: List to sort
        key: Function to extract comparison key from each element
        reverse: If True, sort in descending order
    
    Returns:
        Sorted list (modifies original)
    
    Time: O(n²), Space: O(1)
    """
    if not arr or len(arr) <= 1:
        return arr
    
    n = len(arr)
    
    # Define comparison function
    def compare(a, b):
        val_a = key(a) if key else a
        val_b = key(b) if key else b
        
        if reverse:
            return val_a > val_b
        return val_a < val_b
    
    # Selection sort algorithm
    for i in range(n - 1):
        extreme_idx = i  # Index of minimum (or maximum if reverse)
        
        # Find the appropriate extreme element
        for j in range(i + 1, n):
            if compare(arr[j], arr[extreme_idx]):
                extreme_idx = j
        
        # Swap if necessary
        if extreme_idx != i:
            arr[i], arr[extreme_idx] = arr[extreme_idx], arr[i]
    
    return arr

# Advanced test cases
print("=== Advanced Selection Sort Tests ===")

# Sort numbers in descending order
numbers = [64, 25, 12, 22, 11]
print(f"Descending: {selection_sort_optimal(numbers.copy(), reverse=True)}")

# Sort strings by length
words = ["python", "java", "c", "javascript", "go"]
print(f"By length: {selection_sort_optimal(words.copy(), key=len)}")

# Sort tuples by second element
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 95)]
print(f"By grade: {selection_sort_optimal(students.copy(), key=lambda x: x[1])}")
```

---

## 🛠️ Problem 2: Find Minimum Element in Array

**Problem**: Find the smallest element in an array efficiently.
**Link**: [GeeksforGeeks Minimum Element](https://www.geeksforgeeks.org/to-find-smallest-element-in-an-array/)

### 🔨 Approach 1: Brute Force (Linear Scan)

**Pseudocode**:
```
ALGORITHM FindMinimum(array):
    IF array is empty:
        RETURN null or error
    
    min_value = array[0]
    
    FOR i = 1 to length(array)-1:
        IF array[i] < min_value:
            min_value = array[i]
    
    RETURN min_value
```

**Python Implementation**:
```python
def find_minimum_basic(arr):
    """
    Find minimum element using linear scan
    Time: O(n), Space: O(1)
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    min_val = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    
    return min_val

# Test
test_arrays = [
    [64, 25, 12, 22, 11],
    [1, 2, 3, 4, 5],
    [-5, -1, -10, 0, 3],
    [42]
]

for arr in test_arrays:
    min_val = find_minimum_basic(arr)
    print(f"Array: {arr}, Minimum: {min_val}")
```

### 🚀 Approach 2: Optimal with Index Tracking

**Python Implementation**:
```python
def find_minimum_with_index(arr):
    """
    Find minimum element and its index
    Time: O(n), Space: O(1)
    """
    if not arr:
        return None, -1
    
    min_val = arr[0]
    min_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    
    return min_val, min_idx

# Test with index tracking
test_array = [64, 25, 12, 22, 11]
min_val, min_idx = find_minimum_with_index(test_array)
print(f"Array: {test_array}")
print(f"Minimum value: {min_val} at index: {min_idx}")
```

---

## 🔄 Selection Sort vs Bubble Sort Comparison

| Aspect | Selection Sort | Bubble Sort |
|--------|----------------|-------------|
| **Best Case** | O(n²) | O(n) |
| **Average Case** | O(n²) | O(n²) |
| **Worst Case** | O(n²) | O(n²) |
| **Space Complexity** | O(1) | O(1) |
| **Stability** | Not stable | Stable |
| **Swaps** | O(n) | O(n²) |
| **Comparisons** | O(n²) | O(n²) |
| **Adaptive** | No | Yes |

### Key Differences:
1. **Selection Sort** makes fewer swaps (at most n-1)
2. **Bubble Sort** can terminate early if array becomes sorted
3. **Selection Sort** always performs same number of comparisons
4. **Bubble Sort** is stable, Selection Sort is not

---

## 🧠 Logic Exercises

### Exercise 1: Trace Through Algorithm
Given array `[29, 10, 14, 37, 13]`, manually trace selection sort:

**Your Turn**: Fill in the steps
```
Initial: [29, 10, 14, 37, 13]
Step 1:  [__, __, __, __, __]  // Find min: __, swap with position 0
Step 2:  [__, __, __, __, __]  // Find min: __, swap with position 1
Step 3:  [__, __, __, __, __]  // Find min: __, swap with position 2
Step 4:  [__, __, __, __, __]  // Find min: __, swap with position 3
Final:   [__, __, __, __, __]
```

### Exercise 2: Count Operations
For an array of size 5, calculate:
- Number of comparisons: ___
- Maximum number of swaps: ___
- Minimum number of swaps: ___

### Exercise 3: Variant Implementation
Implement selection sort that finds the **maximum** element and places it at the end:

```python
def selection_sort_max_to_end(arr):
    """
    Your implementation here
    Find maximum and place at end, work backwards
    """
    pass
```

---

## 🎯 Practice Problems

### Beginner Level:
1. Sort an array of integers using selection sort
2. Find the second smallest element in an array
3. Sort an array of strings alphabetically

### Intermediate Level:
1. Implement selection sort for 2D array rows
2. Sort array of objects by multiple criteria
3. Count number of swaps made during sorting

### Advanced Level:
1. Implement recursive selection sort
2. Selection sort with custom comparator
3. Hybrid algorithm: Selection sort for small arrays, merge sort for large

---

## 🚀 Time & Space Complexity Summary

```
Selection Sort Analysis:
├── Time Complexity
│   ├── Best Case:    O(n²) - Always same comparisons
│   ├── Average Case: O(n²) - Typical performance
│   └── Worst Case:   O(n²) - Maximum comparisons
├── Space Complexity
│   └── Auxiliary:    O(1)  - In-place sorting
└── Other Properties
    ├── Stability:    Not stable
    ├── Adaptive:     No
    └── Online:       No
```

---

## ✅ Key Takeaways

1. **Selection Sort** is simple but inefficient for large datasets
2. Always performs **O(n²) comparisons** regardless of input
3. Makes **minimum number of swaps** (at most n-1)
4. **Not stable** - can change relative order of equal elements
5. **In-place** sorting algorithm with O(1) space complexity
6. Good for **small arrays** or when **swap cost is high**
7. **Not adaptive** - doesn't benefit from partially sorted arrays

---

## 🔗 Additional Resources

- [Sorting Algorithm Visualizer](https://visualgo.net/en/sorting)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Algorithm Design Manual - Chapter on Sorting](https://www.algorist.com/)
- [Selection Sort Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)