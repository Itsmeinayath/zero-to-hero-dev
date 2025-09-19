# 📚 Day 24: Searching Algorithms - Complete Guide

## 🎯 Learning Objectives
By the end of this session, you will:
- **Master** linear and binary search algorithms with their variations
- **Understand** search optimization in rotated and modified arrays
- **Implement** optimal solutions for complex search scenarios
- **Recognize** when to apply different search strategies

---

## 📖 Searching Algorithms Fundamentals

### 🔍 **Search Algorithm Mastery**:
Searching is one of the most fundamental operations in computer science. Today we focus on **logarithmic optimization** and **handling complex array structures**.

**Key Concepts:**
- **Linear Search**: Sequential scanning through elements
- **Binary Search**: Divide and conquer approach for sorted arrays
- **Modified Binary Search**: Adaptations for rotated/modified arrays
- **Search Space Analysis**: Understanding when and how to eliminate half the search space

### 🎯 **Search Algorithm Patterns**:

| Algorithm | Time Complexity | Space | Prerequisites | Use Cases |
|-----------|----------------|--------|---------------|-----------|
| **Linear Search** | O(n) | O(1) | None | Unsorted data, small arrays |
| **Binary Search** | O(log n) | O(1) | Sorted array | Large sorted datasets |
| **Modified Binary** | O(log n) | O(1) | Partially sorted | Rotated, peak finding |
| **Exponential Search** | O(log n) | O(1) | Unbounded sorted | Infinite arrays |

---

## 🎬 Visual Understanding: Binary Search in Rotated Array

Understanding **search in rotated sorted array**:

```
Original Sorted Array: [1, 2, 3, 4, 5, 6, 7]
Rotated at index 4:    [4, 5, 6, 7, 1, 2, 3]
Target: 2

Step 1: Find mid = 3, nums[3] = 7
[4, 5, 6, 7, 1, 2, 3]
 ↑        ↑           ↑
left     mid        right

Step 2: Check which half is sorted
Left half [4,5,6,7] is sorted (4 ≤ 7)
Target 2 not in range [4,7], so search right half

Step 3: Update left = mid + 1 = 4
[4, 5, 6, 7, 1, 2, 3]
             ↑  ↑  ↑
            left mid right

Step 4: Find new mid = 5, nums[5] = 2 = target ✅
Found at index 5!
```

---

## 📚 Learning Resources

### 🎥 Video Resources (Theory - 30 minutes):
1. **Tushar Roy's "Binary Search Recap"** (15 min) - [YouTube](https://www.youtube.com/watch?v=pYT9F8_LFTM&t=600s)
   - Binary search fundamentals and variations
2. **Abdul Bari's "Divide and Conquer"** (10 min) - Search algorithm principles
3. **mycodeschool Binary Search** (5 min) - Implementation details and edge cases

### 📄 Article Resources:
1. **GeeksforGeeks Binary Search Recap** (15 min) - [Link](https://www.geeksforgeeks.org/binary-search/)
   - Comprehensive search algorithms reference
2. **Binary Search Variations** - Modified binary search patterns
3. **Search Optimization Techniques** - Performance analysis and improvements

---

## 🛠️ Problem 1: Search in Rotated Sorted Array (LeetCode 33)

**Problem**: Search for a target value in a rotated sorted array.
**Link**: [LeetCode Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

### 🔨 Approach 1: Brute Force (Linear Search)

**Algorithm Logic**:
- Scan through the array linearly from left to right
- Return index when target is found
- Simple but doesn't utilize the sorted property

**Pseudocode**:
```
ALGORITHM SearchRotatedLinear(nums, target):
    n = length of nums
    
    FOR i = 0 to n-1:
        IF nums[i] == target:
            RETURN i
    
    RETURN -1  // Target not found
```

**Python Implementation**:
```python
def search_rotated_linear(nums, target):
    """
    Brute force linear search approach
    Time: O(n), Space: O(1)
    """
    if not nums:
        return -1
    
    for i in range(len(nums)):
        print(f"Checking index {i}: nums[{i}] = {nums[i]}")
        if nums[i] == target:
            print(f"Target {target} found at index {i}")
            return i
    
    print(f"Target {target} not found in array")
    return -1

# Test with step-by-step visualization
test_array = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Array:", test_array)
print(f"Searching for target: {target}")
result = search_rotated_linear(test_array, target)
print(f"Result: {result}")
```

**Complexity Analysis**:
- **Time**: O(n) - Must check every element in worst case
- **Space**: O(1) - Only using constant extra space
- **Problem**: Doesn't leverage the sorted property of the array

### 🚀 Approach 2: Better (Modified Binary Search)

**Algorithm Logic**:
- Use binary search but handle the rotation
- At each step, determine which half is sorted
- Check if target lies in the sorted half, otherwise search the other half

**Pseudocode**:
```
ALGORITHM SearchRotatedBinary(nums, target):
    left = 0
    right = length(nums) - 1
    
    WHILE left <= right:
        mid = (left + right) // 2
        
        IF nums[mid] == target:
            RETURN mid
        
        // Determine which side is sorted
        IF nums[left] <= nums[mid]:  // Left side is sorted
            IF nums[left] <= target < nums[mid]:
                right = mid - 1  // Target in left sorted half
            ELSE:
                left = mid + 1   // Target in right half
        ELSE:  // Right side is sorted
            IF nums[mid] < target <= nums[right]:
                left = mid + 1   // Target in right sorted half
            ELSE:
                right = mid - 1  // Target in left half
    
    RETURN -1
```

**Python Implementation**:
```python
def search_rotated_binary(nums, target):
    """
    Modified binary search for rotated array
    Time: O(log n), Space: O(1)
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        print(f"Search range: [{left}, {right}], mid = {mid}")
        print(f"Values: left={nums[left]}, mid={nums[mid]}, right={nums[right]}")
        
        # Found target
        if nums[mid] == target:
            print(f"Target {target} found at index {mid}")
            return mid
        
        # Determine which side is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            print(f"Left side [{left}, {mid}] is sorted")
            if nums[left] <= target < nums[mid]:
                print(f"Target {target} is in left sorted half")
                right = mid - 1
            else:
                print(f"Target {target} is in right half")
                left = mid + 1
        else:  # Right side is sorted
            print(f"Right side [{mid}, {right}] is sorted")
            if nums[mid] < target <= nums[right]:
                print(f"Target {target} is in right sorted half")
                left = mid + 1
            else:
                print(f"Target {target} is in left half")
                right = mid - 1
        
        print("---")
    
    print(f"Target {target} not found")
    return -1

# Test with detailed tracing
test_array = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Array:", test_array)
print(f"Searching for target: {target}")
result = search_rotated_binary(test_array, target)
print(f"Result: {result}")
```

### 🎯 Approach 3: Optimal (Enhanced Binary Search)

**Features**:
- Handles edge cases (duplicates, single elements)
- Optimized condition checking
- Clear rotation point identification

**Python Implementation**:
```python
def search_rotated_optimal(nums, target):
    """
    Optimal binary search with enhanced edge case handling
    Time: O(log n), Space: O(1)
    """
    if not nums:
        return -1
    
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Target is in the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            # Target is in the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def find_rotation_point(nums):
    """
    Helper function to find the rotation point (minimum element)
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    # Array is not rotated
    if nums[left] <= nums[right]:
        return left
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Found the rotation point
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Comprehensive test suite
def test_search_rotated_solutions():
    """Test all approaches with various cases"""
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, "Standard rotation"),
        ([4, 5, 6, 7, 0, 1, 2], 3, "Target not present"),
        ([1], 0, "Single element - not found"),
        ([1], 1, "Single element - found"),
        ([1, 3], 3, "Two elements"),
        ([3, 1], 1, "Two elements rotated"),
        ([5, 1, 2, 3, 4], 1, "Rotation at start"),
        ([2, 3, 4, 5, 1], 1, "Rotation at end"),
        ([1, 2, 3, 4, 5], 3, "No rotation"),
    ]
    
    print("=== Search in Rotated Sorted Array - All Approaches ===")
    
    for nums, target, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Array: {nums}, Target: {target}")
        
        linear_result = search_rotated_linear(nums.copy(), target)
        binary_result = search_rotated_binary(nums.copy(), target)
        optimal_result = search_rotated_optimal(nums.copy(), target)
        
        print(f"Linear Search: {linear_result}")
        print(f"Binary Search: {binary_result}")
        print(f"Optimal: {optimal_result}")
        
        # Verify all approaches give same result
        if linear_result == binary_result == optimal_result:
            print("✅ All approaches match")
        else:
            print("❌ Results don't match!")
        
        # Show rotation point
        rotation_point = find_rotation_point(nums)
        print(f"Rotation point: {rotation_point}")

# Run comprehensive tests
test_search_rotated_solutions()
```

### 🧠 **Why Modified Binary Search Works**:

**Key Insight**:
```
In a rotated sorted array, at least one half is always sorted:

Case 1: Left half is sorted
[1, 2, 3, 4, 5, 6, 7] rotated → [4, 5, 6, 7, 1, 2, 3]
                                  ↑_______↑  ↑_______↑
                                   sorted   unsorted

Case 2: Right half is sorted  
[1, 2, 3, 4, 5, 6, 7] rotated → [6, 7, 1, 2, 3, 4, 5]
                                  ↑___↑  ↑___________↑
                                unsorted    sorted

Strategy:
1. Identify which half is sorted
2. Check if target lies in the sorted half
3. If yes, search in sorted half
4. If no, search in the unsorted half
```

---

## 🛠️ Problem 2: Find Minimum in Rotated Sorted Array (LeetCode 153)

**Problem**: Find the minimum element in a rotated sorted array.
**Link**: [LeetCode Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

### 🔨 Approach 1: Brute Force (Linear Scan)

**Algorithm Logic**:
- Scan through array to find the minimum element
- Track the smallest value encountered
- Simple but doesn't use sorted property

**Pseudocode**:
```
ALGORITHM FindMinLinear(nums):
    min_val = nums[0]
    
    FOR i = 1 to length(nums)-1:
        IF nums[i] < min_val:
            min_val = nums[i]
    
    RETURN min_val
```

**Python Implementation**:
```python
def find_min_linear(nums):
    """
    Linear scan to find minimum
    Time: O(n), Space: O(1)
    """
    if not nums:
        return None
    
    min_val = nums[0]
    min_index = 0
    
    for i in range(1, len(nums)):
        print(f"Checking nums[{i}] = {nums[i]}, current min = {min_val}")
        if nums[i] < min_val:
            min_val = nums[i]
            min_index = i
            print(f"New minimum: {min_val} at index {i}")
    
    return min_val

# Test with visualization
test_array = [4, 5, 6, 7, 0, 1, 2]
print("Array:", test_array)
result = find_min_linear(test_array)
print(f"Minimum element: {result}")
```

### 🚀 Approach 2: Better (Binary Search)

**Algorithm Logic**:
- Use binary search to find the rotation point (minimum element)
- If array is not rotated, first element is minimum
- Otherwise, find the point where order breaks

**Pseudocode**:
```
ALGORITHM FindMinBinary(nums):
    left = 0
    right = length(nums) - 1
    
    // Array is not rotated
    IF nums[left] <= nums[right]:
        RETURN nums[left]
    
    WHILE left <= right:
        mid = (left + right) // 2
        
        // Found minimum (rotation point)
        IF mid > 0 AND nums[mid] < nums[mid-1]:
            RETURN nums[mid]
        
        IF nums[mid] >= nums[left]:
            left = mid + 1  // Minimum is in right half
        ELSE:
            right = mid - 1  // Minimum is in left half
    
    RETURN nums[left]
```

**Python Implementation**:
```python
def find_min_binary(nums):
    """
    Binary search to find minimum in rotated array
    Time: O(log n), Space: O(1)
    """
    if not nums:
        return None
    
    left, right = 0, len(nums) - 1
    
    # Array is not rotated - first element is minimum
    if nums[left] <= nums[right]:
        print("Array is not rotated")
        return nums[left]
    
    while left <= right:
        mid = left + (right - left) // 2
        
        print(f"Search range: [{left}, {right}], mid = {mid}")
        print(f"Values: left={nums[left]}, mid={nums[mid]}, right={nums[right]}")
        
        # Check if mid is the minimum
        if mid > 0 and nums[mid] < nums[mid - 1]:
            print(f"Found rotation point at index {mid}")
            return nums[mid]
        
        # Check if mid+1 is the minimum
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            print(f"Found rotation point at index {mid + 1}")
            return nums[mid + 1]
        
        # Decide which half to search
        if nums[mid] >= nums[left]:
            print("Minimum is in right half")
            left = mid + 1
        else:
            print("Minimum is in left half")
            right = mid - 1
        
        print("---")
    
    return nums[left]

# Test with detailed tracing
test_array = [4, 5, 6, 7, 0, 1, 2]
print("Array:", test_array)
result = find_min_binary(test_array)
print(f"Minimum element: {result}")
```

### 🎯 Approach 3: Optimal (Clean Binary Search)

**Features**:
- Simplified logic with clear conditions
- Handles all edge cases efficiently
- Most readable implementation

**Python Implementation**:
```python
def find_min_optimal(nums):
    """
    Optimal binary search with clean logic
    Time: O(log n), Space: O(1)
    """
    if not nums:
        return None
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid element is greater than right element,
        # minimum must be in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return nums[left]

def find_min_with_index(nums):
    """
    Enhanced version that returns both minimum value and its index
    """
    if not nums:
        return None, -1
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left], left

# Comprehensive test suite
def test_find_min_solutions():
    """Test all approaches with various cases"""
    test_cases = [
        ([3, 4, 5, 1, 2], "Standard rotation"),
        ([4, 5, 6, 7, 0, 1, 2], "Rotation in middle"),
        ([11, 13, 15, 17], "No rotation"),
        ([2, 1], "Two elements"),
        ([1], "Single element"),
        ([5, 1, 2, 3, 4], "Rotation at start"),
        ([2, 3, 4, 5, 1], "Rotation at end"),
    ]
    
    print("=== Find Minimum in Rotated Sorted Array - All Approaches ===")
    
    for nums, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Array: {nums}")
        
        linear_result = find_min_linear(nums.copy())
        binary_result = find_min_binary(nums.copy())
        optimal_result = find_min_optimal(nums.copy())
        min_val, min_idx = find_min_with_index(nums.copy())
        
        print(f"Linear: {linear_result}")
        print(f"Binary: {binary_result}")
        print(f"Optimal: {optimal_result}")
        print(f"With Index: value={min_val}, index={min_idx}")
        
        # Verify all approaches give same result
        if linear_result == binary_result == optimal_result == min_val:
            print("✅ All approaches match")
        else:
            print("❌ Results don't match!")

# Run comprehensive tests
test_find_min_solutions()
```

### 🔍 **Binary Search Optimization Logic**:

**Decision Tree**:
```python
def explain_binary_search_logic():
    """
    Explain the decision making in binary search for rotated arrays
    """
    print("""
    Binary Search Decision Logic:
    
    At each step, we have nums[left], nums[mid], nums[right]
    
    For finding minimum:
    if nums[mid] > nums[right]:
        # Minimum is in right half
        # Example: [4,5,6,7,0,1,2], mid=7, right=2
        left = mid + 1
    else:
        # Minimum is in left half (including mid)
        # Example: [6,7,0,1,2,4,5], mid=1, right=5
        right = mid
    
    Key insight: We always have at least one sorted half
    The minimum is always at the rotation point
    """)

# explain_binary_search_logic()
```

---

## 🔄 Advanced Search Patterns

### 📊 **Search Pattern Classification**:

| Pattern | When to Use | Key Characteristics | Examples |
|---------|-------------|-------------------|----------|
| **Standard Binary** | Sorted array | Eliminate half each time | Basic search, insert position |
| **Modified Binary** | Rotated/modified sorted | Identify sorted half first | Rotated array, peak element |
| **Template Binary** | Complex conditions | Use while(left < right) | First/last occurrence |
| **Exponential Search** | Unbounded array | Find range then binary | Infinite arrays |

### 🎯 **Binary Search Template**:

```python
def binary_search_template(arr, target, condition_func):
    """
    Generic binary search template for various problems
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if condition_func(arr, mid, target) == 0:
            return mid  # Found
        elif condition_func(arr, mid, target) < 0:
            left = mid + 1  # Search right
        else:
            right = mid - 1  # Search left
    
    return -1  # Not found

def first_occurrence_template(arr, target):
    """
    Template for finding first occurrence
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

---

## 🧠 Logic Exercises & Visualization

### Exercise 1: Manual Binary Search Trace
Practice binary search in rotated array:

```
Array: [6, 7, 1, 2, 3, 4, 5], Target: 3
Initial: left=0, right=6

Step 1: mid = __, nums[mid] = __
Which half is sorted? ____________
Is target in sorted half? ________
New range: left=__, right=__

Step 2: mid = __, nums[mid] = __
Which half is sorted? ____________
Is target in sorted half? ________
New range: left=__, right=__

Continue until found...
Final answer: index = __
```

### Exercise 2: Rotation Point Finding
Identify the minimum element:

```
Array: [4, 5, 6, 7, 0, 1, 2]

Visual representation:
Index: 0  1  2  3  4  5  6
Value: 4  5  6  7  0  1  2
       ↑  ↑  ↑  ↑  ↓  ↑  ↑
                    min

Where does the "break" occur? ________
What is the pattern? _______________
Minimum value: ____, Index: ____
```

### Exercise 3: Search Strategy Selection
Choose the optimal approach:

```
Problem scenarios:
1. Sorted array, find exact target: ____________
2. Rotated array, find target: _______________
3. Find first occurrence of target: __________
4. Find insertion position: ________________
5. Unsorted array, find target: _____________

Your reasoning for each choice:
1. ___________________________________
2. ___________________________________
3. ___________________________________
4. ___________________________________
5. ___________________________________
```

---

## 🎯 Practice Problems & Extensions

### Beginner Level:
1. **Binary Search**: Implement standard binary search
2. **Search Insert Position**: Find position to insert target
3. **First Bad Version**: Binary search variation

### Intermediate Level:
1. **Find Peak Element**: Binary search in unsorted array
2. **Search in 2D Matrix**: Extended binary search
3. **Find First and Last Position**: Range finding

### Advanced Level:
1. **Median of Two Sorted Arrays**: Binary search optimization
2. **Kth Smallest Element**: Binary search on answer
3. **Search in Rotated Array II**: Handle duplicates

### 🚀 **Implementation Challenges**:

```python
# Challenge 1: Search in 2D matrix
def search_matrix(matrix, target):
    """Search in row-wise and column-wise sorted matrix"""
    # Use binary search properties in 2D
    pass

# Challenge 2: Find peak element
def find_peak_element(nums):
    """Find any peak element in O(log n) time"""
    # Binary search without full sorting
    pass

# Challenge 3: Kth smallest in range
def kth_smallest_in_range(matrix, k):
    """Find kth smallest element using binary search on answer"""
    # Binary search on the value range
    pass
```

---

## 🚀 Performance Analysis & Optimization

### 📊 **Algorithm Comparison**:

| Problem | Linear Search | Binary Search | Space | Notes |
|---------|---------------|---------------|-------|-------|
| **Sorted Array Search** | O(n) | O(log n) | O(1) | Binary is optimal |
| **Rotated Array Search** | O(n) | O(log n) | O(1) | Modified binary |
| **Find Minimum** | O(n) | O(log n) | O(1) | Binary finds rotation point |
| **Range Queries** | O(n) | O(log n) | O(1) | Multiple binary searches |

### ⚡ **Search Optimization Techniques**:

1. **Overflow Prevention**: Use `left + (right - left) // 2` instead of `(left + right) // 2`
2. **Early Termination**: Check for exact match first
3. **Template Usage**: Standardize binary search patterns
4. **Boundary Handling**: Careful with `<=` vs `<` conditions

### 🎯 **When to Use Each Search**:

✅ **Linear Search**:
- Small arrays (n < 50)
- Unsorted data
- Simple implementation needed

✅ **Binary Search**:
- Large sorted arrays
- Logarithmic time required
- Memory is limited

✅ **Modified Binary Search**:
- Rotated/partially sorted arrays
- Peak finding problems
- Condition-based searching

❌ **Not Suitable**:
- Frequently changing data
- Very small datasets
- Complex non-monotonic conditions

---

## ✅ Key Takeaways

1. **Binary search** reduces time complexity from O(n) to O(log n) for sorted data
2. **Modified binary search** handles rotated arrays by identifying sorted halves
3. **Template patterns** provide consistent implementation across various problems
4. **Condition analysis** is crucial for determining search direction
5. **Edge case handling** prevents infinite loops and incorrect results
6. **Rotation point detection** is key for rotated array problems
7. **Search space elimination** is the core principle of efficient searching

---

## 🔗 Additional Resources

- [Binary Search Visualization](https://visualgo.net/en/bst)
- [LeetCode Binary Search Problems](https://leetcode.com/tag/binary-search/)
- [Binary Search Patterns](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template)
- [Search Algorithm Analysis](https://www.geeksforgeeks.org/searching-algorithms/)