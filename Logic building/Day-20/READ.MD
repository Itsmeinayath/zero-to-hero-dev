# 📚 Day 20: Searching & Sorting Recap - Mixed Practice Guide

## 🎯 Learning Objectives
By the end of this recap session, you will:
- **Consolidate** all searching and sorting concepts from Week 3
- **Master** advanced binary search techniques (Find Peak Element)
- **Compare** and **choose** optimal sorting algorithms for different scenarios
- **Integrate** searching and sorting knowledge for complex problem-solving

---

## 🔄 Week 3 Recap: What We've Learned

### 📊 **Complete Algorithm Arsenal**:

| Day | Algorithm | Best Case | Average | Worst Case | Space | Stable | Adaptive |
|-----|-----------|-----------|---------|------------|-------|--------|----------|
| **17** | Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| **18** | Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ❌ |
| **19** | Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| **Today** | Binary Search | O(1) | O(log n) | O(log n) | O(1) | - | - |

### 🏆 **Algorithm Selection Guide**:
- **Small arrays (n < 50)**: Insertion Sort
- **Nearly sorted data**: Insertion Sort or Bubble Sort
- **Memory constrained**: Selection Sort (minimum swaps)
- **Stability required**: Insertion Sort or Bubble Sort
- **Educational purposes**: Bubble Sort
- **Searching sorted data**: Binary Search

---

## 📖 Binary Search: Advanced Applications

**Binary Search** isn't just for finding elements! It's a powerful technique for finding optimal solutions in sorted or "monotonic" spaces.

### 🔍 Key Pattern Recognition:
- **Sorted Array**: Classic binary search
- **Rotated Sorted Array**: Modified binary search
- **Peak Finding**: Binary search on derivatives
- **Search Space**: Binary search on answer ranges

### 🌟 Advanced Binary Search Template:
```python
def binary_search_template(left, right, condition):
    """
    Universal binary search template
    Find the boundary where condition changes from False to True
    """
    while left < right:
        mid = left + (right - left) // 2
        
        if condition(mid):
            right = mid  # Condition is true, search left half
        else:
            left = mid + 1  # Condition is false, search right half
    
    return left  # The boundary point
```

---

## 🎬 Visual Example: Peak Finding Concept

Understanding peaks in arrays:

```
Array: [1, 2, 1, 3, 5, 6, 4]
Index:  0  1  2  3  4  5  6

Peak Analysis:
- Index 1: arr[1] = 2 > arr[0] = 1 AND arr[1] = 2 > arr[2] = 1 ✅ PEAK
- Index 5: arr[5] = 6 > arr[4] = 5 AND arr[5] = 6 > arr[6] = 4 ✅ PEAK

Binary Search Approach:
Compare mid with mid+1 to determine which half has a peak
If arr[mid] < arr[mid+1]: Peak is in right half
If arr[mid] > arr[mid+1]: Peak is in left half (mid could be peak)
```

---

## 📚 Learning Resources

### 🎥 Video Resources (Theory - 1 hour):
1. **Tushar Roy's "Search & Sort Recap"** (20 min) - [YouTube](https://www.youtube.com/watch?v=pYT9F8_LFTM&t=300s)
   - Comprehensive review of all algorithms
2. **Abdul Bari's "Binary Search Applications"** (25 min) - Advanced binary search patterns
3. **NeetCode's "Sorting Algorithm Comparison"** (15 min) - When to use which algorithm

### 📄 Article Resources:
1. **GeeksforGeeks Searching Algorithms** (20 min) - [Link](https://www.geeksforgeeks.org/searching-algorithms/)
   - Complete reference for all search techniques
2. **Sorting Algorithm Analysis** (15 min) - Performance comparison guide
3. **Binary Search Problem Patterns** - Common application categories

---

## 🛠️ Problem 1: Find Peak Element (LeetCode 162)

**Problem**: Find any peak element in an array where a peak is greater than its neighbors.
**Link**: [LeetCode Find Peak Element](https://leetcode.com/problems/find-peak-element/)

### 🔨 Approach 1: Brute Force (Linear Scan)

**Algorithm Logic**:
- Check each element to see if it's greater than its neighbors
- Handle edge cases for first and last elements
- Return first peak found

**Pseudocode**:
```
ALGORITHM FindPeakLinear(array):
    n = length of array
    
    // Handle edge cases
    IF n == 1: RETURN 0
    
    // Check first element
    IF array[0] > array[1]: RETURN 0
    
    // Check middle elements
    FOR i = 1 to n-2:
        IF array[i] > array[i-1] AND array[i] > array[i+1]:
            RETURN i
    
    // Check last element
    IF array[n-1] > array[n-2]: RETURN n-1
    
    RETURN -1  // No peak found (shouldn't happen)
```

**Python Implementation**:
```python
def find_peak_linear(nums):
    """
    Linear scan to find peak element
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    
    # Edge case: single element
    if n == 1:
        return 0
    
    # Check first element
    if nums[0] > nums[1]:
        return 0
    
    # Check middle elements
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    
    # Check last element
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    
    return -1  # Should never reach here for valid input

# Test the implementation
test_cases = [
    [1, 2, 3, 1],           # Peak at index 2
    [1, 2, 1, 3, 5, 6, 4],  # Multiple peaks
    [1],                     # Single element
    [1, 2],                 # Two elements
    [2, 1]                  # Two elements, peak at start
]

for i, nums in enumerate(test_cases):
    peak_idx = find_peak_linear(nums)
    print(f"Test {i+1}: {nums}")
    print(f"Peak at index {peak_idx}, value = {nums[peak_idx]}")
    print()
```

**Complexity Analysis**:
- **Time**: O(n) - Check each element once
- **Space**: O(1) - Constant extra space
- **Worst Case**: Need to check all elements

### 🚀 Approach 2: Better (Binary Search)

**Algorithm Logic**:
- Use binary search to find peak efficiently
- Compare mid with mid+1 to decide search direction
- Guaranteed to find a peak due to array properties

**Key Insight**: If `nums[mid] < nums[mid+1]`, then there must be a peak in the right half because:
- Either we find an element greater than its right neighbor (peak)
- Or we reach the end (last element is a peak)

**Pseudocode**:
```
ALGORITHM FindPeakBinary(array):
    left = 0
    right = length(array) - 1
    
    WHILE left < right:
        mid = (left + right) // 2
        
        IF array[mid] < array[mid + 1]:
            left = mid + 1    // Peak is in right half
        ELSE:
            right = mid       // Peak is in left half (including mid)
    
    RETURN left  // left == right, pointing to peak
```

**Python Implementation**:
```python
def find_peak_binary(nums):
    """
    Binary search to find peak element
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid element is smaller than next element,
        # peak must be in right half
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # Peak is in left half (including mid)
            right = mid
    
    return left  # left == right at this point

# Test with detailed trace
def find_peak_with_trace(nums):
    """Binary search with detailed step tracing"""
    print(f"Finding peak in: {nums}")
    
    left, right = 0, len(nums) - 1
    step = 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        print(f"Step {step}: left={left}, right={right}, mid={mid}")
        print(f"  nums[{mid}] = {nums[mid]}, nums[{mid+1}] = {nums[mid+1]}")
        
        if nums[mid] < nums[mid + 1]:
            print(f"  {nums[mid]} < {nums[mid+1]}, search right half")
            left = mid + 1
        else:
            print(f"  {nums[mid]} >= {nums[mid+1]}, search left half")
            right = mid
        
        step += 1
    
    print(f"Peak found at index {left}, value = {nums[left]}")
    return left

# Test with trace
test_array = [1, 2, 1, 3, 5, 6, 4]
find_peak_with_trace(test_array)
```

### 🎯 Approach 3: Optimal (Handle All Edge Cases)

**Features**:
- Robust handling of all edge cases
- Clear separation of concerns
- Comprehensive input validation

**Python Implementation**:
```python
def find_peak_optimal(nums):
    """
    Optimal peak finding with comprehensive edge case handling
    Time: O(log n), Space: O(1)
    """
    if not nums:
        raise ValueError("Array cannot be empty")
    
    n = len(nums)
    
    # Handle single element
    if n == 1:
        return 0
    
    # Handle two elements
    if n == 2:
        return 0 if nums[0] > nums[1] else 1
    
    # Binary search for peak
    left, right = 0, n - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Compare with next element
        if mid < n - 1 and nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Comprehensive test suite
def run_peak_tests():
    """Run comprehensive tests for all approaches"""
    test_cases = [
        ([1, 2, 3, 1], "Standard case"),
        ([1, 2, 1, 3, 5, 6, 4], "Multiple peaks"),
        ([1], "Single element"),
        ([1, 2], "Two elements - ascending"),
        ([2, 1], "Two elements - descending"),
        ([1, 3, 2, 1], "Peak in middle"),
        ([1, 2, 3, 4, 5], "Monotonically increasing"),
        ([5, 4, 3, 2, 1], "Monotonically decreasing"),
    ]
    
    print("=== Peak Finding Comprehensive Tests ===")
    
    for i, (nums, description) in enumerate(test_cases):
        print(f"\nTest {i+1}: {description}")
        print(f"Array: {nums}")
        
        # Test all approaches
        linear_result = find_peak_linear(nums.copy())
        binary_result = find_peak_binary(nums.copy())
        optimal_result = find_peak_optimal(nums.copy())
        
        print(f"Linear scan:   Peak at index {linear_result} (value: {nums[linear_result]})")
        print(f"Binary search: Peak at index {binary_result} (value: {nums[binary_result]})")
        print(f"Optimal:       Peak at index {optimal_result} (value: {nums[optimal_result]})")
        
        # Verify all results are valid peaks
        def is_peak(arr, idx):
            n = len(arr)
            left_ok = idx == 0 or arr[idx] > arr[idx - 1]
            right_ok = idx == n - 1 or arr[idx] > arr[idx + 1]
            return left_ok and right_ok
        
        all_valid = (is_peak(nums, linear_result) and 
                    is_peak(nums, binary_result) and 
                    is_peak(nums, optimal_result))
        
        print(f"All results valid: {'✅' if all_valid else '❌'}")

run_peak_tests()
```

---

## 🛠️ Problem 2: Sort Array (Complete Sorting Analysis)

**Problem**: Sort an array in ascending order, but choose the optimal algorithm based on input characteristics.
**Link**: [GeeksforGeeks Sort Array](https://www.geeksforgeeks.org/sort-an-array-in-ascending-order/)

### 🔨 Approach 1: Brute Force (Any O(n²) Sort)

**Algorithm Logic**:
- Use any quadratic sorting algorithm
- For demonstration, we'll use Bubble Sort
- Good for educational purposes but inefficient

**Python Implementation**:
```python
def sort_array_brute(nums):
    """
    Brute force sorting using bubble sort
    Time: O(n²), Space: O(1)
    """
    n = len(nums)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            comparisons += 1
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaps += 1
                swapped = True
        
        # Early termination if no swaps occurred
        if not swapped:
            break
    
    print(f"Bubble Sort: {comparisons} comparisons, {swaps} swaps")
    return nums

# Test brute force approach
test_array = [64, 34, 25, 12, 22, 11, 90]
print("Original:", test_array)
result = sort_array_brute(test_array.copy())
print("Sorted:", result)
```

### 🚀 Approach 2: Better/Optimal (Insertion Sort)

**Algorithm Logic**:
- Use insertion sort for its adaptive properties
- Excellent for small or nearly sorted arrays
- Stable and in-place

**Python Implementation**:
```python
def sort_array_insertion(nums):
    """
    Better sorting using insertion sort
    Time: O(n²) worst, O(n) best, Space: O(1)
    """
    n = len(nums)
    comparisons = 0
    shifts = 0
    
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        
        # Shift elements and count operations
        while j >= 0:
            comparisons += 1
            if nums[j] <= key:
                break
            nums[j + 1] = nums[j]
            j -= 1
            shifts += 1
        
        nums[j + 1] = key
    
    print(f"Insertion Sort: {comparisons} comparisons, {shifts} shifts")
    return nums

# Test insertion sort
test_array = [64, 34, 25, 12, 22, 11, 90]
print("\nOriginal:", test_array)
result = sort_array_insertion(test_array.copy())
print("Sorted:", result)
```

### 🎯 Approach 3: Smart Algorithm Selection

**Features**:
- Automatically choose best algorithm based on input
- Hybrid approach for optimal performance
- Detailed performance analysis

**Python Implementation**:
```python
def analyze_array_characteristics(nums):
    """
    Analyze array to determine optimal sorting strategy
    """
    n = len(nums)
    
    if n <= 1:
        return "trivial"
    
    # Check if already sorted
    sorted_count = 0
    for i in range(n - 1):
        if nums[i] <= nums[i + 1]:
            sorted_count += 1
    
    sorted_percentage = sorted_count / (n - 1)
    
    # Analyze characteristics
    characteristics = {
        "size": n,
        "sorted_percentage": sorted_percentage,
        "is_nearly_sorted": sorted_percentage > 0.8,
        "is_reverse_sorted": sorted_percentage < 0.2,
        "has_duplicates": len(set(nums)) < n,
        "range": max(nums) - min(nums) if n > 0 else 0
    }
    
    return characteristics

def smart_sort(nums):
    """
    Intelligently choose sorting algorithm based on array characteristics
    """
    if not nums:
        return nums
    
    characteristics = analyze_array_characteristics(nums)
    
    if characteristics == "trivial":
        return nums
    
    n = characteristics["size"]
    
    print(f"Array Analysis:")
    print(f"  Size: {n}")
    print(f"  Sorted percentage: {characteristics['sorted_percentage']:.2%}")
    print(f"  Nearly sorted: {characteristics['is_nearly_sorted']}")
    print(f"  Has duplicates: {characteristics['has_duplicates']}")
    
    # Algorithm selection logic
    if n <= 10:
        print("Chosen: Insertion Sort (small array)")
        return sort_array_insertion(nums)
    elif characteristics["is_nearly_sorted"]:
        print("Chosen: Insertion Sort (nearly sorted)")
        return sort_array_insertion(nums)
    elif characteristics["is_reverse_sorted"]:
        print("Chosen: Selection Sort (reverse sorted - minimal swaps)")
        return sort_array_selection(nums)
    else:
        print("Chosen: Insertion Sort (general case)")
        return sort_array_insertion(nums)

def sort_array_selection(nums):
    """Selection sort implementation for comparison"""
    n = len(nums)
    comparisons = 0
    swaps = 0
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            comparisons += 1
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            swaps += 1
    
    print(f"Selection Sort: {comparisons} comparisons, {swaps} swaps")
    return nums

# Comprehensive testing
test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], "Random array"),
    ([1, 2, 3, 5, 4, 6, 7, 8], "Nearly sorted"),
    ([8, 7, 6, 5, 4, 3, 2, 1], "Reverse sorted"),
    ([3, 1, 4, 1, 5, 9, 2, 6], "With duplicates"),
    ([5, 2, 8, 1], "Small array"),
    ([], "Empty array"),
    ([42], "Single element")
]

print("=== Smart Sorting Algorithm Selection ===")
for i, (nums, description) in enumerate(test_cases):
    print(f"\nTest {i+1}: {description}")
    print(f"Original: {nums}")
    if nums:
        result = smart_sort(nums.copy())
        print(f"Sorted: {result}")
    else:
        print("Sorted: []")
```

---

## 🔄 Algorithm Comparison & Selection Guide

### 📊 **Performance Comparison on Different Inputs**:

```python
def comprehensive_sorting_comparison():
    """Compare all three sorting algorithms on various inputs"""
    import time
    import random
    
    test_scenarios = [
        ("Random small", lambda: random.sample(range(100), 20)),
        ("Random large", lambda: random.sample(range(1000), 100)),
        ("Nearly sorted", lambda: list(range(50)) + [random.randint(0, 49) for _ in range(10)]),
        ("Reverse sorted", lambda: list(range(50, 0, -1))),
        ("All same", lambda: [42] * 30),
        ("Many duplicates", lambda: [i//5 for i in range(50)]),
    ]
    
    algorithms = [
        ("Bubble Sort", sort_array_brute),
        ("Insertion Sort", sort_array_insertion),
        ("Selection Sort", sort_array_selection),
    ]
    
    print("=== Comprehensive Sorting Performance Comparison ===")
    
    for scenario_name, generator in test_scenarios:
        print(f"\n📊 Scenario: {scenario_name}")
        data = generator()
        print(f"Array size: {len(data)}")
        
        results = []
        for algo_name, algo_func in algorithms:
            test_data = data.copy()
            
            start_time = time.perf_counter()
            sorted_data = algo_func(test_data)
            end_time = time.perf_counter()
            
            execution_time = (end_time - start_time) * 1000  # Convert to ms
            results.append((algo_name, execution_time))
            
            # Verify correctness
            is_correct = sorted_data == sorted(data)
            print(f"  {algo_name}: {execution_time:.3f}ms {'✅' if is_correct else '❌'}")
        
        # Find best performing algorithm
        best_algo = min(results, key=lambda x: x[1])
        print(f"  🏆 Best: {best_algo[0]} ({best_algo[1]:.3f}ms)")

# Run comprehensive comparison (commented out for performance)
# comprehensive_sorting_comparison()
```

### 🎯 **When to Use Each Algorithm**:

| Scenario | Best Choice | Reason |
|----------|-------------|---------|
| **Small arrays (n < 20)** | Insertion Sort | Simple, fast for small inputs |
| **Nearly sorted** | Insertion Sort | O(n) best case performance |
| **Reverse sorted** | Selection Sort | Minimal swaps needed |
| **Memory critical** | Selection Sort | Fewer swaps, predictable memory access |
| **Stability required** | Insertion/Bubble | Maintains relative order |
| **Educational** | Bubble Sort | Easy to understand and visualize |
| **General purpose** | Insertion Sort | Good balance of simplicity and performance |

---

## 🧠 Logic Exercises & Week 3 Review

### Exercise 1: Algorithm Selection Challenge
For each scenario, choose the optimal algorithm and explain why:

```python
scenarios = [
    "Sort 1000 employee records by salary (stability required)",
    "Sort 15 test scores for a small class",
    "Sort a mostly sorted array of 500 elements",
    "Sort an array known to be in reverse order",
    "Sort data arriving one element at a time (online)",
    "Find if a sorted array has any duplicate elements"
]

# Your answers:
optimal_choices = [
    # Scenario 1: _____ because _____
    # Scenario 2: _____ because _____
    # Scenario 3: _____ because _____
    # Scenario 4: _____ because _____
    # Scenario 5: _____ because _____
    # Scenario 6: _____ because _____
]
```

### Exercise 2: Binary Search Applications
Identify which problems can be solved using binary search:

```python
problems = [
    "Find square root of a number",
    "Find first occurrence of element in sorted array",
    "Find minimum in rotated sorted array",
    "Search in 2D sorted matrix",
    "Find peak element in mountain array",
    "Allocate minimum pages to students"
]

# Mark True/False for binary search applicability
binary_search_applicable = [
    # Problem 1: True/False - Explanation
    # Problem 2: True/False - Explanation
    # ... continue for all problems
]
```

### Exercise 3: Complexity Analysis Review
Fill in the complexity table:

| Algorithm | Best Time | Average Time | Worst Time | Space | When to Use |
|-----------|-----------|--------------|------------|-------|-------------|
| Linear Search | ___ | ___ | ___ | ___ | ___ |
| Binary Search | ___ | ___ | ___ | ___ | ___ |
| Bubble Sort | ___ | ___ | ___ | ___ | ___ |
| Selection Sort | ___ | ___ | ___ | ___ | ___ |
| Insertion Sort | ___ | ___ | ___ | ___ | ___ |

---

## 🎯 Week 3 Mastery Checklist

### ✅ **Searching Algorithms**:
- [ ] Understand linear vs binary search trade-offs
- [ ] Implement binary search without bugs
- [ ] Recognize binary search application patterns
- [ ] Handle edge cases in search algorithms
- [ ] Apply binary search to non-obvious problems

### ✅ **Sorting Algorithms**:
- [ ] Implement all three basic sorts correctly
- [ ] Understand stability and adaptiveness
- [ ] Choose optimal algorithm for given constraints
- [ ] Analyze time/space complexity accurately
- [ ] Optimize implementations with early termination

### ✅ **Problem Solving Skills**:
- [ ] Break down complex problems systematically
- [ ] Choose appropriate data structures and algorithms
- [ ] Handle edge cases and input validation
- [ ] Write clean, readable, and efficient code
- [ ] Test solutions with comprehensive test cases

---

## 🚀 Advanced Challenges

### Challenge 1: Hybrid Sorting Algorithm
```python
def hybrid_sort(nums, threshold=10):
    """
    Implement a hybrid sorting algorithm that:
    1. Uses insertion sort for arrays smaller than threshold
    2. Uses different algorithms based on array characteristics
    3. Measures and reports performance metrics
    """
    # Your implementation here
    pass
```

### Challenge 2: Binary Search Variants
```python
def find_first_occurrence(nums, target):
    """Find first occurrence of target in sorted array with duplicates"""
    # Your implementation here
    pass

def find_last_occurrence(nums, target):
    """Find last occurrence of target in sorted array with duplicates"""
    # Your implementation here
    pass

def find_insertion_position(nums, target):
    """Find position where target should be inserted to maintain sorted order"""
    # Your implementation here
    pass
```

### Challenge 3: Algorithm Visualization
```python
def visualize_sorting_algorithm(nums, algorithm_name):
    """
    Create step-by-step visualization of sorting process
    Show comparisons, swaps, and array state at each step
    """
    # Your implementation here
    pass
```

---

## ✅ Key Takeaways from Week 3

### 🎯 **Fundamental Insights**:
1. **Algorithm choice matters**: No single algorithm is always best
2. **Input characteristics**: Understanding input helps choose optimal approach
3. **Trade-offs everywhere**: Time vs space, stability vs performance
4. **Edge cases critical**: Always handle empty arrays, single elements
5. **Binary search power**: Reduces O(n) problems to O(log n)

### 🚀 **Practical Skills Gained**:
1. **Implementation mastery**: Clean, bug-free algorithm implementations
2. **Complexity analysis**: Accurate time/space complexity assessment
3. **Problem decomposition**: Breaking complex problems into manageable parts
4. **Testing strategies**: Comprehensive test case design
5. **Performance optimization**: Early termination, input analysis

### 🔮 **Looking Ahead**:
- **Week 4**: Advanced data structures (stacks, queues, linked lists)
- **Future topics**: Merge sort, quick sort, heap sort
- **Advanced searching**: Binary search tree, hash tables
- **Real-world applications**: Database indexing, search engines

---

## 🔗 Additional Resources

- [Sorting Algorithm Animations](https://www.sortvisualizer.com/)
- [Binary Search Problem Set](https://leetcode.com/tag/binary-search/)
- [Algorithm Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
- [Interactive Algorithm Visualizations](https://visualgo.net/en)

**Congratulations on completing Week 3! 🎉**
**Next**: Week 4 - Advanced Data Structures & Algorithms!