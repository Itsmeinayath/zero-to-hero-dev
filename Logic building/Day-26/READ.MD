# 📚 Day 26: Mixed Practice - Algorithm Integration Mastery

## 🎯 Learning Objectives
By the end of this session, you will:
- **Master** algorithm integration across different problem domains
- **Understand** Kadane's algorithm for maximum subarray problems
- **Implement** efficient solutions for finding Kth largest elements
- **Recognize** when to combine multiple algorithmic patterns
- **Apply** optimization techniques from previous weeks

---

## 📖 Mixed Practice Fundamentals

### What is Mixed Practice?
Mixed practice involves solving problems that **combine multiple algorithmic concepts** learned in previous weeks. Instead of focusing on a single pattern, you'll need to **identify and apply the most appropriate technique** or **combine multiple approaches** for optimal solutions.

### 🔑 Key Skills for Mixed Practice
1. **Pattern Recognition**: Quickly identify which algorithm(s) to apply
2. **Algorithm Selection**: Choose the most efficient approach for given constraints
3. **Implementation Speed**: Code solutions quickly and correctly
4. **Optimization**: Transform brute force solutions into optimal ones

### 🧠 Why Mixed Practice Matters
- **Real-world problems** rarely fit into single algorithm categories
- **Interview preparation** requires combining multiple concepts
- **Problem-solving skills** improve through pattern integration
- **Algorithm mastery** comes from applying concepts flexibly

---

## 📚 Learning Resources

### 📹 Video Resources
- **NeetCode's "Mixed Recap"** (15 min) - Algorithm integration patterns
  - URL: https://www.youtube.com/watch?v=gD7A1VvSSB8&t=600s
- **Abdul Bari's "Dynamic Programming"** (25 min) - Kadane's algorithm deep dive
- **Tushar Roy's "Heap Operations"** (20 min) - Kth largest element techniques

### 📖 Article Resources
- **GeeksforGeeks "DSA Basics"** - Comprehensive algorithm review
  - URL: https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/
- **LeetCode Discuss** - Mixed practice problem discussions
- **Programiz "Algorithm Complexity"** - Time/space analysis guide

### 🔧 Interactive Tools
- **VisuAlgo** - Algorithm visualization for multiple concepts
- **LeetCode Playground** - Test implementations quickly
- **Algorithm Visualizer** - See how algorithms work together

---

## 🛠️ Problem 1: Maximum Subarray (LeetCode 53)

### 📋 Problem Statement
Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum** and return its sum.

**Example:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
```

### 🎬 Visual Understanding: Kadane's Algorithm
```
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        
Step-by-step process:
Index 0: curr_sum = -2, max_sum = -2
Index 1: curr_sum = max(1, -2+1) = 1, max_sum = 1
Index 2: curr_sum = max(-3, 1-3) = -2, max_sum = 1
Index 3: curr_sum = max(4, -2+4) = 4, max_sum = 4
Index 4: curr_sum = max(-1, 4-1) = 3, max_sum = 4
Index 5: curr_sum = max(2, 3+2) = 5, max_sum = 5
Index 6: curr_sum = max(1, 5+1) = 6, max_sum = 6 ✅
Index 7: curr_sum = max(-5, 6-5) = 1, max_sum = 6
Index 8: curr_sum = max(4, 1+4) = 5, max_sum = 6

Result: Maximum subarray sum = 6
Subarray: [4, -1, 2, 1]
```

### 🥉 Approach 1: Brute Force
**Explanation**: Check all possible subarrays and find the maximum sum.

**Pseudocode:**
```
FUNCTION maxSubarrayBrute(nums):
  SET max_sum = negative infinity
  
  FOR i FROM 0 TO length(nums) - 1:
    FOR j FROM i TO length(nums) - 1:
      SET current_sum = 0
      FOR k FROM i TO j:
        current_sum += nums[k]
      max_sum = max(max_sum, current_sum)
  
  RETURN max_sum
```

**Python Implementation:**
```python
def maxSubarrayBrute(nums):
    max_sum = float('-inf')
    n = len(nums)
    
    # Check all possible subarrays
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(nums[i:j+1])
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Brute Force Result: {maxSubarrayBrute(test_array)}")  # Output: 6
```

**Analysis:**
- ⏱️ **Time Complexity**: O(n³) - Three nested loops
- 💾 **Space Complexity**: O(1) - Constant extra space
- ✅ **Pros**: Simple to understand and implement
- ❌ **Cons**: Extremely inefficient for large arrays

### 🥈 Approach 2: Better (Optimized Brute Force)
**Explanation**: Calculate sum incrementally instead of recalculating from scratch.

**Pseudocode:**
```
FUNCTION maxSubarrayBetter(nums):
  SET max_sum = negative infinity
  
  FOR i FROM 0 TO length(nums) - 1:
    SET current_sum = 0
    FOR j FROM i TO length(nums) - 1:
      current_sum += nums[j]
      max_sum = max(max_sum, current_sum)
  
  RETURN max_sum
```

**Python Implementation:**
```python
def maxSubarrayBetter(nums):
    max_sum = float('-inf')
    n = len(nums)
    
    # Check all subarrays starting from each position
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Better Approach Result: {maxSubarrayBetter(test_array)}")  # Output: 6
```

**Analysis:**
- ⏱️ **Time Complexity**: O(n²) - Two nested loops
- 💾 **Space Complexity**: O(1) - Constant extra space
- ✅ **Pros**: Better than brute force, incremental sum calculation
- ❌ **Cons**: Still quadratic time complexity

### 🥇 Approach 3: Optimal (Kadane's Algorithm)
**Explanation**: Dynamic programming approach that decides at each position whether to extend the existing subarray or start a new one.

**Core Insight**: At each position, we have two choices:
1. **Extend** the previous subarray by including current element
2. **Start fresh** from current element

**Pseudocode:**
```
FUNCTION maxSubarrayOptimal(nums):
  SET max_sum = nums[0]
  SET current_sum = nums[0]
  
  FOR i FROM 1 TO length(nums) - 1:
    // Choose: extend previous subarray or start new
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)
  
  RETURN max_sum
```

**Python Implementation:**
```python
def maxSubarrayOptimal(nums):
    if not nums:
        return 0
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    # Kadane's algorithm
    for i in range(1, len(nums)):
        # Either extend the existing subarray or start new
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Enhanced version with subarray tracking
def maxSubarrayWithSubarray(nums):
    if not nums:
        return 0, []
    
    max_sum = nums[0]
    current_sum = nums[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, nums[start:end+1]

# Test
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = maxSubarrayWithSubarray(test_array)
print(f"Optimal Result: {max_sum}")  # Output: 6
print(f"Subarray: {subarray}")       # Output: [4, -1, 2, 1]
```

**Analysis:**
- ⏱️ **Time Complexity**: O(n) - Single pass through array
- 💾 **Space Complexity**: O(1) - Constant extra space
- ✅ **Pros**: Optimal time complexity, elegant dynamic programming solution
- ✅ **Pros**: Works for all negative arrays too

---

## 🛠️ Problem 2: Kth Largest Element in Array (LeetCode 215)

### 📋 Problem Statement
Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array. Note that it is the kth largest element in sorted order, not the kth distinct element.

**Example:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: [6,5,4,3,2,1] → 2nd largest is 5
```

### 🎬 Visual Understanding: Different Approaches
```
Array: [3, 2, 1, 5, 6, 4], k = 2

Approach 1 - Sorting:
Original: [3, 2, 1, 5, 6, 4]
Sorted:   [6, 5, 4, 3, 2, 1] (descending)
K=2: nums[k-1] = nums[1] = 5

Approach 2 - Min Heap of size K:
Step 1: [3]
Step 2: [2, 3] → heap maintains 2 largest: [2, 3]
Step 3: [2, 3] → 1 < 2, so ignore
Step 4: [3, 5] → 5 > 2, so remove 2, add 5
Step 5: [5, 6] → 6 > 3, so remove 3, add 6
Step 6: [5, 6] → 4 < 5, so ignore
Final heap: [5, 6] → minimum = 5 (2nd largest)

Approach 3 - Quickselect:
Partition around pivot to find kth position directly
```

### 🥉 Approach 1: Brute Force (Sorting)
**Explanation**: Sort the array and return the kth element from the end.

**Pseudocode:**
```
FUNCTION findKthLargestBrute(nums, k):
  SORT nums in descending order
  RETURN nums[k-1]
```

**Python Implementation:**
```python
def findKthLargestBrute(nums, k):
    # Sort in descending order
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k-1]

# Alternative: sort ascending and take from end
def findKthLargestBrute2(nums, k):
    nums_sorted = sorted(nums)
    return nums_sorted[-k]  # kth from end

# Test
test_array = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Brute Force Result: {findKthLargestBrute(test_array, k)}")  # Output: 5
```

**Analysis:**
- ⏱️ **Time Complexity**: O(n log n) - Due to sorting
- 💾 **Space Complexity**: O(1) - If sorting in-place, O(n) if creating new array
- ✅ **Pros**: Simple to implement and understand
- ❌ **Cons**: Overkill for just finding one element

### 🥈 Approach 2: Better (Min-Heap of Size K)
**Explanation**: Maintain a min-heap of size k containing the k largest elements seen so far.

**Pseudocode:**
```
FUNCTION findKthLargestHeap(nums, k):
  CREATE empty min_heap
  
  FOR each num in nums:
    ADD num to min_heap
    IF size of min_heap > k:
      REMOVE minimum from min_heap
  
  RETURN top of min_heap
```

**Python Implementation:**
```python
import heapq

def findKthLargestHeap(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        
        # Keep only k largest elements
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Top of min-heap is kth largest
    return min_heap[0]

# Test with step-by-step visualization
def findKthLargestHeapTrace(nums, k):
    min_heap = []
    
    for i, num in enumerate(nums):
        heapq.heappush(min_heap, num)
        print(f"After adding {num}: heap = {min_heap}")
        
        if len(min_heap) > k:
            removed = heapq.heappop(min_heap)
            print(f"Removed {removed}: heap = {min_heap}")
    
    return min_heap[0]

# Test
test_array = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Heap Result: {findKthLargestHeapTrace(test_array, k)}")  # Output: 5
```

**Analysis:**
- ⏱️ **Time Complexity**: O(n log k) - n insertions, each O(log k)
- 💾 **Space Complexity**: O(k) - Heap stores k elements
- ✅ **Pros**: More efficient than sorting when k << n
- ✅ **Pros**: Good for streaming data

### 🥇 Approach 3: Optimal (Quickselect Algorithm)
**Explanation**: Partitioning-based selection algorithm that finds kth largest in average O(n) time.

**Pseudocode:**
```
FUNCTION findKthLargestQuickselect(nums, k):
  SET target = length(nums) - k  // Convert to 0-indexed
  RETURN quickselect(nums, 0, length(nums)-1, target)

FUNCTION quickselect(nums, left, right, target):
  IF left == right:
    RETURN nums[left]
  
  SET pivot_index = partition(nums, left, right)
  
  IF pivot_index == target:
    RETURN nums[pivot_index]
  ELSE IF pivot_index < target:
    RETURN quickselect(nums, pivot_index+1, right, target)
  ELSE:
    RETURN quickselect(nums, left, pivot_index-1, target)
```

**Python Implementation:**
```python
import random

def findKthLargestQuickselect(nums, k):
    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        # Random pivot for better average performance
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Partition around pivot
        pivot_index = partition(left, right)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)
    
    def partition(left, right):
        pivot = nums[right]
        i = left
        
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    # Convert kth largest to kth smallest (0-indexed)
    return quickselect(0, len(nums) - 1, len(nums) - k)

# Test
test_array = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Quickselect Result: {findKthLargestQuickselect(test_array.copy(), k)}")  # Output: 5
```

**Analysis:**
- ⏱️ **Time Complexity**: O(n) average, O(n²) worst case
- 💾 **Space Complexity**: O(1) average (O(log n) recursion stack)
- ✅ **Pros**: Optimal average time complexity
- ✅ **Pros**: In-place algorithm
- ❌ **Cons**: Complex implementation, worst-case still quadratic

---

## 🧠 Logic Exercises

### Exercise 1: Kadane's Algorithm Deep Dive
**Question**: Why does Kadane's algorithm work? Explain the decision at each step.

**Answer**: At each position, we ask: "Should I extend the previous subarray or start fresh?"
- If `current_sum + nums[i] < nums[i]`, the previous subarray is dragging us down, so start fresh
- Otherwise, extending gives us a better sum
- We track the maximum seen so far as our answer
- **Key insight**: We only keep track of the best option at each step

### Exercise 2: Heap vs Sorting Trade-offs
**Question**: When is using a heap better than sorting for finding kth largest?

**Answer**:
- **Heap is better when**: k << n (k much smaller than n), streaming data, memory constraints
- **Sorting is better when**: k ≈ n, need multiple order statistics, simpler implementation
- **Time comparison**: Heap O(n log k) vs Sort O(n log n)
- **Space comparison**: Heap O(k) vs Sort O(1) in-place

### Exercise 3: Algorithm Selection Framework
**Question**: How do you choose between different approaches for the same problem?

**Answer**:
1. **Analyze constraints**: Array size, k value, memory limits
2. **Consider use case**: One-time vs repeated queries, streaming data
3. **Implementation complexity**: Interview vs production code
4. **Performance requirements**: Worst-case vs average-case guarantees

---

## 🔄 Performance Comparison

### Maximum Subarray Performance Analysis
```python
import time
import random

def performance_test_max_subarray():
    # Generate test data
    sizes = [100, 1000, 10000]
    
    for n in sizes:
        nums = [random.randint(-100, 100) for _ in range(n)]
        
        print(f"\nArray size: {n}")
        
        # Test brute force (only for small arrays)
        if n <= 1000:
            start = time.time()
            result1 = maxSubarrayBrute(nums)
            time1 = time.time() - start
            print(f"Brute Force: {result1}, Time: {time1:.4f}s")
        
        # Test better approach
        start = time.time()
        result2 = maxSubarrayBetter(nums)
        time2 = time.time() - start
        print(f"Better: {result2}, Time: {time2:.4f}s")
        
        # Test optimal approach
        start = time.time()
        result3 = maxSubarrayOptimal(nums)
        time3 = time.time() - start
        print(f"Optimal: {result3}, Time: {time3:.4f}s")

# Run performance test
performance_test_max_subarray()
```

### Kth Largest Performance Analysis
```python
def performance_test_kth_largest():
    sizes = [1000, 10000, 100000]
    k_values = [1, 10, 100]
    
    for n in sizes:
        for k in k_values:
            if k > n:
                continue
                
            nums = [random.randint(1, 1000000) for _ in range(n)]
            
            print(f"\nArray size: {n}, k: {k}")
            
            # Test sorting approach
            start = time.time()
            result1 = findKthLargestBrute(nums.copy(), k)
            time1 = time.time() - start
            print(f"Sorting: {result1}, Time: {time1:.4f}s")
            
            # Test heap approach
            start = time.time()
            result2 = findKthLargestHeap(nums.copy(), k)
            time2 = time.time() - start
            print(f"Heap: {result2}, Time: {time2:.4f}s")
            
            # Test quickselect approach
            start = time.time()
            result3 = findKthLargestQuickselect(nums.copy(), k)
            time3 = time.time() - start
            print(f"Quickselect: {result3}, Time: {time3:.4f}s")

# Run performance test
performance_test_kth_largest()
```

---

## 🎯 Advanced Practice Problems

### 🔥 Beginner Level
1. **Maximum Product Subarray** (LeetCode 152) - Variation of Kadane's algorithm
2. **Top K Frequent Elements** (LeetCode 347) - Heap practice with frequency counting
3. **Find Peak Element** (LeetCode 162) - Binary search in unsorted array

### 🔥 Intermediate Level
1. **Sliding Window Maximum** (LeetCode 239) - Deque + sliding window technique
2. **Merge k Sorted Lists** (LeetCode 23) - Heap + linked list manipulation
3. **Longest Increasing Subsequence** (LeetCode 300) - DP + binary search optimization

### 🔥 Advanced Level
1. **Maximum Sum of 3 Non-Overlapping Subarrays** (LeetCode 689) - Advanced DP
2. **Median of Two Sorted Arrays** (LeetCode 4) - Binary search mastery
3. **Range Sum Query 2D** (LeetCode 304) - Prefix sums + matrix operations

---

## ✅ Key Takeaways

### 🎯 Algorithm Integration Mastery
1. **Pattern Recognition**: Identify when problems combine multiple concepts
2. **Optimization Thinking**: Transform brute force → better → optimal systematically
3. **Trade-off Analysis**: Understand time vs space vs implementation complexity
4. **Template Application**: Use learned patterns as building blocks for complex solutions

### 🚀 Kadane's Algorithm Applications
- **Core Problems**: Maximum subarray, maximum product subarray
- **Variations**: Circular arrays, multiple subarrays, with constraints
- **Key Insight**: Local optimization leads to global optimum
- **Implementation**: Simple but powerful dynamic programming

### 🔥 Selection Algorithm Strategies
- **Sorting**: Simple but O(n log n), good for multiple queries
- **Heap**: Efficient for small k, excellent for streaming data
- **Quickselect**: Optimal average case, complex but powerful
- **Choice depends**: Problem constraints and use case requirements

### 💡 Mixed Practice Problem-Solving Framework
1. **Read carefully**: Understand constraints and edge cases
2. **Identify patterns**: Which algorithms/data structures apply?
3. **Start simple**: Implement brute force for correctness
4. **Optimize step-by-step**: Apply learned optimization techniques
5. **Test thoroughly**: Verify with multiple test cases

---

