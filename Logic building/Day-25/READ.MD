# 📚 Day 25: Sorting Algorithms & Applications - Complete Guide

## 🎯 Learning Objectives
By the end of this session, you will:
- **Master** fundamental sorting algorithms and their applications
- **Understand** sorting-based problem solving techniques
- **Implement** optimal solutions for interval merging and array partitioning
- **Recognize** when sorting preprocessing leads to efficient solutions

---

## 📖 Sorting Algorithms & Applications Fundamentals

### 🔍 **Sorting Algorithm Mastery**:
Sorting is often the key to transforming complex problems into simpler ones. Today we focus on **sorting as preprocessing** and **partition-based algorithms**.

**Key Concepts:**
- **Comparison-based sorting**: Bubble, Selection, Insertion sorts
- **Efficient sorting**: Merge sort, Quick sort principles
- **Sorting applications**: Interval problems, partitioning
- **In-place algorithms**: Space-optimal implementations

### 🎯 **Sorting Algorithm Patterns**:

| Algorithm | Time Avg | Time Worst | Space | Stable | Adaptive | Use Cases |
|-----------|----------|------------|-------|--------|----------|-----------|
| **Bubble Sort** | O(n²) | O(n²) | O(1) | ✅ | ✅ | Small datasets, educational |
| **Selection Sort** | O(n²) | O(n²) | O(1) | ❌ | ❌ | Minimal swaps needed |
| **Insertion Sort** | O(n²) | O(n²) | O(1) | ✅ | ✅ | Nearly sorted data |
| **Merge Sort** | O(n log n) | O(n log n) | O(n) | ✅ | ❌ | Large datasets, stability |
| **Quick Sort** | O(n log n) | O(n²) | O(log n) | ❌ | ❌ | General purpose |

---

## 🎬 Visual Understanding: Interval Merging

Understanding **merge intervals** technique:

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Goal: Merge overlapping intervals

Step 1: Sort by start time (already sorted)
[1,3] [2,6] [8,10] [15,18]

Step 2: Initialize result with first interval
result = [[1,3]]

Step 3: Process [2,6]
[1,3] overlaps with [2,6] because 3 ≥ 2
Merge: [1, max(3,6)] = [1,6]
result = [[1,6]]

Step 4: Process [8,10]  
[1,6] doesn't overlap with [8,10] because 6 < 8
Add to result: [[1,6], [8,10]]

Step 5: Process [15,18]
[8,10] doesn't overlap with [15,18] because 10 < 15
Add to result: [[1,6], [8,10], [15,18]] ✅
```

---

## 📚 Learning Resources

### 🎥 Video Resources (Theory - 30 minutes):
1. **NeetCode's "Sorting Recap"** (15 min) - [YouTube](https://www.youtube.com/watch?v=JU767SDMDvA&t=300s)
   - Sorting algorithms review and applications
2. **Abdul Bari's "Sorting Techniques"** (10 min) - Comprehensive sorting overview
3. **mycodeschool Sorting** (5 min) - Implementation details and optimization

### 📄 Article Resources:
1. **GeeksforGeeks Sorting Algorithms** (15 min) - [Link](https://www.geeksforgeeks.org/sorting-algorithms/)
   - Complete sorting algorithms reference
2. **Interval Problems Guide** - Sorting-based interval algorithms
3. **Partitioning Techniques** - Two-pointer and Dutch flag algorithms

---

## 🛠️ Problem 1: Merge Intervals (LeetCode 56)

**Problem**: Merge all overlapping intervals in an array.
**Link**: [LeetCode Merge Intervals](https://leetcode.com/problems/merge-intervals/)

### 🔨 Approach 1: Brute Force (Check All Pairs)

**Algorithm Logic**:
- For each interval, check if it overlaps with any other interval
- Merge overlapping intervals and repeat until no more merging
- Continue until no overlaps remain

**Pseudocode**:
```
ALGORITHM MergeIntervalsBrute(intervals):
    result = copy of intervals
    changed = true
    
    WHILE changed:
        changed = false
        new_result = []
        i = 0
        
        WHILE i < length(result):
            current = result[i]
            merged = false
            
            FOR j = i+1 to length(result)-1:
                IF overlaps(current, result[j]):
                    merged_interval = merge(current, result[j])
                    new_result.add(merged_interval)
                    // Skip the merged interval
                    result.remove(j)
                    changed = true
                    merged = true
                    BREAK
            
            IF not merged:
                new_result.add(current)
            i++
        
        result = new_result
    
    RETURN result

FUNCTION overlaps(interval1, interval2):
    RETURN interval1[1] >= interval2[0] AND interval2[1] >= interval1[0]

FUNCTION merge(interval1, interval2):
    start = MIN(interval1[0], interval2[0])
    end = MAX(interval1[1], interval2[1])
    RETURN [start, end]
```

**Python Implementation**:
```python
def merge_intervals_brute_force(intervals):
    """
    Brute force: Check all pairs repeatedly
    Time: O(n³), Space: O(n)
    """
    if not intervals:
        return []
    
    def overlaps(interval1, interval2):
        """Check if two intervals overlap"""
        return interval1[1] >= interval2[0] and interval2[1] >= interval1[0]
    
    def merge_two(interval1, interval2):
        """Merge two overlapping intervals"""
        start = min(interval1[0], interval2[0])
        end = max(interval1[1], interval2[1])
        return [start, end]
    
    result = [interval[:] for interval in intervals]  # Deep copy
    
    changed = True
    iteration = 0
    
    while changed:
        iteration += 1
        print(f"Iteration {iteration}: {result}")
        changed = False
        new_result = []
        i = 0
        
        while i < len(result):
            current = result[i]
            merged = False
            
            # Check if current interval overlaps with any later interval
            for j in range(i + 1, len(result)):
                if overlaps(current, result[j]):
                    merged_interval = merge_two(current, result[j])
                    print(f"Merging {current} and {result[j]} → {merged_interval}")
                    new_result.append(merged_interval)
                    
                    # Add all remaining intervals except the merged one
                    for k in range(i + 1, len(result)):
                        if k != j:
                            new_result.append(result[k])
                    
                    changed = True
                    merged = True
                    break
            
            if not merged:
                new_result.append(current)
                
            if merged:
                break
            i += 1
        
        if not changed:
            new_result = result
        
        result = new_result
    
    return result

# Test with step-by-step visualization
test_intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Input intervals:", test_intervals)
result = merge_intervals_brute_force(test_intervals)
print("Final result:", result)
```

**Complexity Analysis**:
- **Time**: O(n³) - O(n²) pairs to check, repeated O(n) times
- **Space**: O(n) - Storing result intervals
- **Problem**: Very inefficient due to repeated checking

### 🚀 Approach 2: Better (Sort and Merge)

**Algorithm Logic**:
- Sort intervals by start time
- Iterate through sorted intervals and merge overlapping ones
- Much more efficient with single pass after sorting

**Pseudocode**:
```
ALGORITHM MergeIntervalsSorted(intervals):
    IF intervals is empty:
        RETURN []
    
    // Sort intervals by start time
    SORT intervals by interval[0]
    
    result = [intervals[0]]
    
    FOR i = 1 to length(intervals)-1:
        current = intervals[i]
        last_merged = result[length(result)-1]
        
        IF current[0] <= last_merged[1]:  // Overlapping
            // Merge intervals
            last_merged[1] = MAX(last_merged[1], current[1])
        ELSE:
            // No overlap, add to result
            result.add(current)
    
    RETURN result
```

**Python Implementation**:
```python
def merge_intervals_sorted(intervals):
    """
    Sort and merge approach
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    print("Sorted intervals:", intervals)
    
    result = [intervals[0]]
    print(f"Initialize result with first interval: {result}")
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = result[-1]
        
        print(f"\nProcessing interval {current}")
        print(f"Last merged interval: {last_merged}")
        
        # Check if current interval overlaps with last merged interval
        if current[0] <= last_merged[1]:
            # Overlapping - merge them
            old_end = last_merged[1]
            last_merged[1] = max(last_merged[1], current[1])
            print(f"Overlap detected! Merging:")
            print(f"  {last_merged[0]},{old_end}] + [{current[0]},{current[1]}] → [{last_merged[0]},{last_merged[1]}]")
        else:
            # No overlap - add current interval to result
            result.append(current)
            print(f"No overlap. Adding {current} to result")
        
        print(f"Current result: {result}")
    
    return result

# Test with detailed tracing
test_intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Input intervals:", test_intervals)
result = merge_intervals_sorted(test_intervals)
print(f"\nFinal merged intervals: {result}")
```

### 🎯 Approach 3: Optimal (Enhanced Sort and Merge)

**Features**:
- Handles edge cases (empty intervals, single interval)
- Optimized memory usage
- Clear separation of concerns

**Python Implementation**:
```python
def merge_intervals_optimal(intervals):
    """
    Optimal sort and merge with enhanced edge case handling
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []
    
    if len(intervals) == 1:
        return intervals
    
    # Sort by start time, then by end time if start times are equal
    intervals.sort(key=lambda x: (x[0], x[1]))
    
    merged = []
    
    for current in intervals:
        # If merged is empty or no overlap with last interval
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            # Overlap exists - merge with last interval
            merged[-1][1] = max(merged[-1][1], current[1])
    
    return merged

# Comprehensive test suite
def test_merge_intervals_solutions():
    """Test all approaches with various cases"""
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], "Standard overlapping"),
        ([[1,4],[4,5]], "Adjacent intervals"),
        ([[1,4],[2,3]], "Nested intervals"),
        ([[1,4],[0,4]], "Same end, different start"),
        ([[1,4],[0,0]], "Point interval"),
        ([[1,4]], "Single interval"),
        ([], "Empty input"),
        ([[1,3],[2,6],[8,10],[9,12],[15,18]], "Multiple overlaps"),
    ]
    
    print("=== Merge Intervals - All Approaches ===")
    
    for intervals, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Input: {intervals}")
        
        if intervals:  # Skip empty for brute force (too complex)
            optimal_result = merge_intervals_optimal([i[:] for i in intervals])
            print(f"Optimal: {optimal_result}")

# Run comprehensive tests
test_merge_intervals_solutions()
```

### 🧠 **Why Sorting Works for Intervals**:

**Key Insight**:
```
After sorting by start time:
- If intervals A and B overlap, and A comes before B, then A.end ≥ B.start
- We only need to check adjacent intervals after sorting
- No need to check all pairs - O(n) instead of O(n²)

Example:
Unsorted: [8,10], [1,3], [15,18], [2,6]
Sorted:   [1,3], [2,6], [8,10], [15,18]

Linear scan:
[1,3] + [2,6] → [1,6] (overlap: 3 ≥ 2)
[1,6] + [8,10] → separate (no overlap: 6 < 8)
[8,10] + [15,18] → separate (no overlap: 10 < 15)

Result: [[1,6], [8,10], [15,18]]
```

---

## 🛠️ Problem 2: Sort Array by Parity (LeetCode 905)

**Problem**: Sort an array so that even numbers come before odd numbers.
**Link**: [LeetCode Sort Array by Parity](https://leetcode.com/problems/sort-array-by-parity/)

### 🔨 Approach 1: Brute Force (Extra Arrays)

**Algorithm Logic**:
- Create separate arrays for even and odd numbers
- Traverse original array and categorize elements
- Combine even and odd arrays

**Python Implementation**:
```python
def sort_parity_brute_force(nums):
    """
    Brute force: Use extra arrays for even and odd
    Time: O(n), Space: O(n)
    """
    if not nums:
        return []
    
    even_nums = []
    odd_nums = []
    
    for num in nums:
        print(f"Processing {num}: {'even' if num % 2 == 0 else 'odd'}")
        if num % 2 == 0:
            even_nums.append(num)
            print(f"  Added to even array: {even_nums}")
        else:
            odd_nums.append(num)
            print(f"  Added to odd array: {odd_nums}")
    
    result = even_nums + odd_nums
    print(f"Final result: {result}")
    return result

# Test with visualization
test_array = [3, 1, 2, 4]
print("Input array:", test_array)
result = sort_parity_brute_force(test_array)
print("Result:", result)
```

### 🚀 Approach 2: Better (Two Pointers In-Place)

**Algorithm Logic**:
- Use two pointers from opposite ends
- Swap elements when left is odd and right is even
- Continue until pointers meet

**Python Implementation**:
```python
def sort_parity_two_pointers(nums):
    """
    Two pointers approach for in-place sorting
    Time: O(n), Space: O(1)
    """
    if not nums:
        return []
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        print(f"Pointers: left={left}, right={right}")
        print(f"Array state: {nums}")
        print(f"Values: nums[{left}]={nums[left]} ({'even' if nums[left] % 2 == 0 else 'odd'}), "
              f"nums[{right}]={nums[right]} ({'even' if nums[right] % 2 == 0 else 'odd'})")
        
        # Move left pointer to find odd number
        while left < right and nums[left] % 2 == 0:
            print(f"  Left {nums[left]} is even, moving left pointer")
            left += 1
        
        # Move right pointer to find even number
        while left < right and nums[right] % 2 == 1:
            print(f"  Right {nums[right]} is odd, moving right pointer")
            right -= 1
        
        # Swap if we found odd on left and even on right
        if left < right:
            print(f"  Swapping nums[{left}]={nums[left]} with nums[{right}]={nums[right]}")
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        print("---")
    
    print(f"Final result: {nums}")
    return nums

# Test with detailed tracing
test_array = [3, 1, 2, 4]
print("Input array:", test_array)
result = sort_parity_two_pointers(test_array.copy())
```

### 🎯 Approach 3: Optimal (Single Pass Partition)

**Features**:
- Single pass through array
- Stable partitioning option
- Flexible criteria handling

**Python Implementation**:
```python
def sort_parity_optimal(nums):
    """
    Optimal single-pass partitioning
    Time: O(n), Space: O(1)
    """
    if not nums:
        return []
    
    # Use partition approach similar to quicksort
    write_index = 0
    
    # First pass: move all even numbers to the front
    for read_index in range(len(nums)):
        if nums[read_index] % 2 == 0:
            nums[write_index], nums[read_index] = nums[read_index], nums[write_index]
            write_index += 1
    
    return nums

# Comprehensive test suite
def test_sort_parity_solutions():
    """Test all approaches with various cases"""
    test_cases = [
        ([3, 1, 2, 4], "Mixed even/odd"),
        ([4, 2, 5, 7], "Even first"),
        ([1, 3, 5, 7], "All odd"),
        ([2, 4, 6, 8], "All even"),
        ([1], "Single odd"),
        ([2], "Single even"),
        ([], "Empty array"),
        ([1, 2], "Two elements"),
        ([0, 1, 2], "With zero"),
    ]
    
    print("=== Sort Array by Parity - All Approaches ===")
    
    for nums, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Input: {nums}")
        
        if nums:
            brute_result = sort_parity_brute_force(nums.copy())
            two_pointer_result = sort_parity_two_pointers(nums.copy())
            optimal_result = sort_parity_optimal(nums.copy())
            
            print(f"Brute Force: {brute_result}")
            print(f"Two Pointers: {two_pointer_result}")
            print(f"Optimal: {optimal_result}")
            
            # Verify all results have even numbers before odd numbers
            def is_valid_parity_sort(arr):
                if not arr:
                    return True
                
                found_odd = False
                for num in arr:
                    if num % 2 == 1:
                        found_odd = True
                    elif found_odd:  # Even number after odd number
                        return False
                return True
            
            results = [brute_result, two_pointer_result, optimal_result]
            if all(is_valid_parity_sort(result) for result in results):
                print("✅ All approaches produce valid parity sorting")
            else:
                print("❌ Some approaches failed parity requirement!")

# Run comprehensive tests
test_sort_parity_solutions()
```

---

## 🧠 Logic Exercises & Visualization

### Exercise 1: Manual Interval Merging
Practice the merge intervals algorithm:

```
Intervals: [[2,3], [4,5], [6,7], [8,9], [1,10]]
Step 1: Sort by start time
Sorted: ________________________________

Step 2: Initialize result with first interval
Result: ________________________________

Step 3: Process each remaining interval
[4,5]: Overlap with [1,10]? ____________
       Action: _______________________
       Result: _______________________

[6,7]: Overlap with current last? _______
       Action: _______________________
       Result: _______________________

Continue until complete...
Final result: __________________________
```

### Exercise 2: Parity Sorting Trace
Trace through two-pointer approach:

```
Array: [5, 2, 3, 4]
Initial: left=0, right=3

Step 1: Check nums[0]=5 (odd), nums[3]=4 (even)
        Action: _______________________
        Array after: ___________________

Step 2: Update pointers: left=__, right=__
        Check nums[left]=__, nums[right]=__
        Action: _______________________
        Array after: ___________________

Continue until left >= right...
Final array: ________________________
```

---

## 🎯 Practice Problems & Extensions

### Beginner Level:
1. **Sort Colors**: Dutch flag algorithm (0s, 1s, 2s)
2. **Meeting Rooms**: Check if person can attend all meetings
3. **Relative Sort Array**: Custom sorting with reference

### Intermediate Level:
1. **Meeting Rooms II**: Minimum conference rooms needed
2. **Insert Interval**: Insert new interval and merge
3. **Non-overlapping Intervals**: Remove minimum intervals

### Advanced Level:
1. **Employee Free Time**: Find common free time slots
2. **Rectangle Area**: Union of rectangles
3. **Skyline Problem**: Building skyline visualization

---

## ✅ Key Takeaways

1. **Sorting as preprocessing** often transforms O(n²) problems to O(n log n)
2. **Interval problems** benefit greatly from sorting by start/end times
3. **Two-pointer techniques** work efficiently on sorted data
4. **Partitioning algorithms** provide O(n) solutions for segregation problems
5. **In-place algorithms** save memory at the cost of stability
6. **Stability** matters when preserving original order is important
7. **Algorithm selection** depends on data characteristics and constraints

---

## 🔗 Additional Resources

- [Sorting Algorithm Visualizations](https://visualgo.net/en/sorting)
- [Interval Problems Pattern](https://leetcode.com/discuss/study-guide/794725/General-Pattern-for-greedy-approach-for-interval-scheduling-problems)
- [Partitioning Algorithms](https://www.geeksforgeeks.org/quicksort-using-dutch-national-flag-algorithm/)
- [LeetCode Sorting Problems](https://leetcode.com/tag/sorting/)
