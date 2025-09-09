# 📚 Day 23: Strings & Sliding Window - Complete Guide

## 🎯 Learning Objectives
By the end of this session, you will:
- **Master** string manipulation techniques and character operations
- **Understand** the Sliding Window pattern and its applications
- **Implement** optimal solutions for palindrome and character frequency problems
- **Recognize** when to apply sliding window vs other string approaches

---

## 📖 Strings & Sliding Window Fundamentals

### 🔍 **String Manipulation Mastery**:
Strings are sequences of characters that require specialized techniques for efficient processing. Today we focus on **character-by-character analysis** and **window-based solutions**.

**Key Concepts:**
- **Character frequency counting**: HashMap/dictionary approaches
- **Palindrome detection**: Expand around center technique
- **Sliding window**: Dynamic substring analysis
- **Two-pointer on strings**: Efficient comparison and validation

### 🎯 **Sliding Window Technique Patterns**:

| Pattern | Description | Time | Use Cases |
|---------|-------------|------|-----------|
| **Fixed Window** | Window size remains constant | O(n) | Substring of exact length |
| **Variable Window** | Window expands/contracts | O(n) | Longest/shortest substring |
| **Character Frequency** | Track char counts in window | O(n) | Anagram, permutation problems |

---

## 🎬 Visual Understanding: Palindrome Expansion

Understanding the **expand around center** technique:

```
String: "babad"
Goal: Find longest palindromic substring

Center at index 1 (character 'a'):
b[a]bad  →  Check: b ≠ d  →  Length = 1 ("a")
 ↑ ↑

Center at index 2 (character 'b'):  
ba[b]ad  →  Check: a ≠ a  →  Length = 3 ("aba")
  ↑   ↑

Center between index 1,2:
b[ab]ad  →  Check: b ≠ a  →  Length = 0
 ↑  ↑

Continue for all centers...
Result: "aba" or "bab" (length 3) ✅
```

---

## 📚 Learning Resources

### 🎥 Video Resources (Theory - 30 minutes):
1. **NeetCode's "Sliding Window Recap"** (15 min) - [YouTube](https://www.youtube.com/watch?v=MK-NZ4hN7rs&t=300s)
   - Essential sliding window patterns and problem-solving approach
2. **Abdul Bari's "String Algorithms"** (10 min) - Fundamental string operations
3. **mycodeschool String Processing** (5 min) - Character manipulation techniques

### 📄 Article Resources:
1. **GeeksforGeeks String Recap** (15 min) - [Link](https://www.geeksforgeeks.org/python-string/)
   - Comprehensive string operations reference
2. **Sliding Window Technique Guide** - Pattern recognition and applications
3. **Character Frequency Analysis** - HashMap optimization strategies

---

## 🛠️ Problem 1: Longest Palindromic Substring (LeetCode 5)

**Problem**: Find the longest palindromic substring in a given string.
**Link**: [LeetCode Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

### 🔨 Approach 1: Brute Force (Check All Substrings)

**Algorithm Logic**:
- Generate all possible substrings
- Check each substring if it's a palindrome
- Track the longest palindrome found

**Pseudocode**:
```
ALGORITHM LongestPalindromeBrute(s):
    n = length of s
    max_len = 0
    result = ""
    
    FOR i = 0 to n-1:
        FOR j = i to n-1:
            substring = s[i:j+1]
            IF isPalindrome(substring):
                IF length(substring) > max_len:
                    max_len = length(substring)
                    result = substring
    
    RETURN result

FUNCTION isPalindrome(str):
    left = 0, right = length(str) - 1
    WHILE left < right:
        IF str[left] != str[right]:
            RETURN false
        INCREMENT left, DECREMENT right
    RETURN true
```

**Python Implementation**:
```python
def longest_palindrome_brute_force(s):
    """
    Brute force: Check all possible substrings
    Time: O(n³), Space: O(1)
    """
    if not s:
        return ""
    
    def is_palindrome(string):
        """Helper function to check if string is palindrome"""
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
    
    max_len = 0
    result = ""
    n = len(s)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            
            if is_palindrome(substring):
                if len(substring) > max_len:
                    max_len = len(substring)
                    result = substring
                    print(f"Found palindrome: '{substring}' at [{i}:{j+1}], length: {len(substring)}")
    
    return result

# Test with step-by-step visualization
test_string = "babad"
print("String:", test_string)
print("Finding longest palindromic substring...")
result = longest_palindrome_brute_force(test_string)
print(f"Longest palindrome: '{result}'")
```

**Complexity Analysis**:
- **Time**: O(n³) - O(n²) substrings, each taking O(n) to check
- **Space**: O(1) - Only using constant extra space
- **Problem**: Very inefficient for large strings

### 🚀 Approach 2: Better (Expand Around Center)

**Algorithm Logic**:
- For each character (and between characters), treat as potential palindrome center
- Expand outward while characters match
- Track the longest palindrome found

**Pseudocode**:
```
ALGORITHM LongestPalindromeExpand(s):
    n = length of s
    max_len = 0
    start = 0
    
    FOR i = 0 to n-1:
        # Check for odd length palindromes (center at i)
        len1 = expandAroundCenter(s, i, i)
        
        # Check for even length palindromes (center between i and i+1)
        len2 = expandAroundCenter(s, i, i+1)
        
        current_max = MAX(len1, len2)
        
        IF current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    RETURN s[start:start + max_len]

FUNCTION expandAroundCenter(s, left, right):
    WHILE left >= 0 AND right < length(s) AND s[left] == s[right]:
        DECREMENT left
        INCREMENT right
    RETURN right - left - 1
```

**Python Implementation**:
```python
def longest_palindrome_expand(s):
    """
    Expand around center approach for optimal solution
    Time: O(n²), Space: O(1)
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        """Expand around center and return palindrome length"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    max_len = 0
    start = 0
    
    for i in range(len(s)):
        # Check for odd length palindromes (center at i)
        len1 = expand_around_center(i, i)
        
        # Check for even length palindromes (center between i and i+1) 
        len2 = expand_around_center(i, i + 1)
        
        # Get maximum length from both cases
        current_max = max(len1, len2)
        
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
            print(f"New longest palindrome found at center {i}: length {current_max}")
    
    result = s[start:start + max_len]
    return result

# Test with detailed tracing
test_string = "babad"
print("String:", test_string)
print("Expanding around each center:")
result = longest_palindrome_expand(test_string)
print(f"Longest palindrome: '{result}'")
```

### 🎯 Approach 3: Optimal (Enhanced Expand with Optimizations)

**Features**:
- Early termination when remaining string can't beat current best
- Optimized center selection
- Comprehensive edge case handling

**Python Implementation**:
```python
def longest_palindrome_optimal(s):
    """
    Optimal expand around center with optimizations
    Time: O(n²), Space: O(1)
    """
    if not s or len(s) < 2:
        return s
    
    def expand_around_center(left, right):
        """Expand and return start index and length"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1
    
    max_len = 1
    start = 0
    
    for i in range(len(s)):
        # Early termination: if remaining chars can't beat current best
        if len(s) - i <= max_len // 2:
            break
            
        # Check odd length palindromes
        start1, len1 = expand_around_center(i, i)
        
        # Check even length palindromes  
        start2, len2 = expand_around_center(i, i + 1)
        
        # Update if we found a longer palindrome
        if len1 > max_len:
            max_len = len1
            start = start1
            
        if len2 > max_len:
            max_len = len2
            start = start2
    
    return s[start:start + max_len]

# Comprehensive test suite
def test_palindrome_solutions():
    """Test all approaches with various cases"""
    test_cases = [
        ("babad", "Standard case"),
        ("cbbd", "Even length palindrome"),
        ("a", "Single character"),
        ("ac", "No palindrome > 1"),
        ("racecar", "Full string palindrome"),
        ("abcdcba", "Odd length full palindrome"),
        ("abccba", "Even length full palindrome"),
        ("", "Empty string"),
    ]
    
    print("=== Longest Palindromic Substring - All Approaches ===")
    
    for test_str, description in test_cases:
        print(f"\nTest: {description}")
        print(f"String: '{test_str}'")
        
        if test_str:  # Skip empty string for brute force (too slow)
            brute_result = longest_palindrome_brute_force(test_str)
            expand_result = longest_palindrome_expand(test_str)
            optimal_result = longest_palindrome_optimal(test_str)
            
            print(f"Brute Force: '{brute_result}'")
            print(f"Expand Center: '{expand_result}'")
            print(f"Optimal: '{optimal_result}'")
            
            # Verify all approaches give same length (may differ in actual string)
            lengths = [len(brute_result), len(expand_result), len(optimal_result)]
            if len(set(lengths)) == 1:
                print("✅ All approaches give same length")
            else:
                print("❌ Length mismatch!")

# Run comprehensive tests
test_palindrome_solutions()
```

### 🧠 **Why Expand Around Center Works**:

**Intuitive Explanation**:
```
Key Insight: Every palindrome has a center

For odd length palindromes: "racecar"
- Center is at middle character: race[c]ar
- Expand outward: [r]ace[c]ar[r] matches

For even length palindromes: "abba"  
- Center is between middle characters: ab|ba
- Expand outward: [a]b|b[a] matches

By checking all possible centers (n + n-1 = 2n-1 total):
- We're guaranteed to find the longest palindrome
- Each expansion takes at most O(n) time
- Total: O(n²) which is optimal for this approach
```

---

## 🛠️ Problem 2: First Non-Repeating Character (GFG)

**Problem**: Find the first character that appears exactly once in a string.
**Link**: [GeeksforGeeks First Non-Repeating Character](https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/)

### 🔨 Approach 1: Brute Force (Check Each Character)

**Algorithm Logic**:
- For each character, count its occurrences in the entire string
- Return the first character with count = 1
- Simple but inefficient due to repeated counting

**Pseudocode**:
```
ALGORITHM FirstNonRepeatingBrute(s):
    n = length of s
    
    FOR i = 0 to n-1:
        count = 0
        FOR j = 0 to n-1:
            IF s[j] == s[i]:
                INCREMENT count
        
        IF count == 1:
            RETURN s[i]
    
    RETURN None  // No non-repeating character found
```

**Python Implementation**:
```python
def first_non_repeating_brute_force(s):
    """
    Brute force: Count each character against entire string
    Time: O(n²), Space: O(1)
    """
    if not s:
        return None
    
    for i in range(len(s)):
        count = 0
        current_char = s[i]
        
        # Count occurrences of current character
        for j in range(len(s)):
            if s[j] == current_char:
                count += 1
        
        print(f"Character '{current_char}' appears {count} times")
        
        # Return first character with count = 1
        if count == 1:
            return current_char
    
    return None  # No non-repeating character found

# Test with visualization
test_string = "geeksforgeeks"
print("String:", test_string)
print("Finding first non-repeating character...")
result = first_non_repeating_brute_force(test_string)
print(f"First non-repeating character: '{result}'")
```

### 🚀 Approach 2: Better (HashMap for Counts)

**Algorithm Logic**:
- First pass: Count frequency of each character using HashMap
- Second pass: Find first character with frequency = 1
- More efficient with only two passes through the string

**Pseudocode**:
```
ALGORITHM FirstNonRepeatingHashMap(s):
    char_count = new HashMap()
    
    // First pass: Count frequencies
    FOR char in s:
        IF char in char_count:
            INCREMENT char_count[char]
        ELSE:
            char_count[char] = 1
    
    // Second pass: Find first non-repeating
    FOR char in s:
        IF char_count[char] == 1:
            RETURN char
    
    RETURN None
```

**Python Implementation**:
```python
def first_non_repeating_hashmap(s):
    """
    HashMap approach for optimal solution
    Time: O(n), Space: O(k) where k is number of unique characters
    """
    if not s:
        return None
    
    # First pass: Count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    print("Character frequencies:")
    for char, count in char_count.items():
        print(f"  '{char}': {count}")
    
    # Second pass: Find first character with count = 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None  # No non-repeating character found

# Test with detailed tracing
test_string = "geeksforgeeks"
print("String:", test_string)
result = first_non_repeating_hashmap(test_string)
print(f"First non-repeating character: '{result}'")
```

### 🎯 Approach 3: Optimal (Single Pass with Enhanced Logic)

**Features**:
- Optimized data structure usage
- Handles edge cases efficiently
- Memory-efficient character tracking

**Python Implementation**:
```python
def first_non_repeating_optimal(s):
    """
    Optimal single-pass approach with enhanced logic
    Time: O(n), Space: O(1) for ASCII characters
    """
    if not s:
        return None
    
    # For ASCII characters, we can use array instead of HashMap
    # ASCII has 128 characters, extended ASCII has 256
    char_count = [0] * 256
    
    # Single pass to count frequencies
    for char in s:
        char_count[ord(char)] += 1
    
    # Single pass to find first non-repeating
    for char in s:
        if char_count[ord(char)] == 1:
            return char
    
    return None

def first_non_repeating_with_position(s):
    """
    Enhanced version that also tracks first occurrence position
    Time: O(n), Space: O(k)
    """
    if not s:
        return None, -1
    
    char_info = {}  # Store {char: (count, first_position)}
    
    # Count frequencies and track positions
    for i, char in enumerate(s):
        if char in char_info:
            char_info[char] = (char_info[char][0] + 1, char_info[char][1])
        else:
            char_info[char] = (1, i)
    
    # Find character with count=1 and earliest position
    min_position = len(s)
    result_char = None
    
    for char, (count, position) in char_info.items():
        if count == 1 and position < min_position:
            min_position = position
            result_char = char
    
    return result_char, min_position if result_char else -1

# Comprehensive test suite
def test_non_repeating_solutions():
    """Test all approaches with various cases"""
    test_cases = [
        ("geeksforgeeks", "Standard case"),
        ("abccba", "All characters repeat"),
        ("abcdef", "All unique"),
        ("aab", "Simple case"),
        ("a", "Single character"),
        ("", "Empty string"),
        ("racecar", "Palindrome"),
    ]
    
    print("=== First Non-Repeating Character - All Approaches ===")
    
    for test_str, description in test_cases:
        print(f"\nTest: {description}")
        print(f"String: '{test_str}'")
        
        brute_result = first_non_repeating_brute_force(test_str)
        hashmap_result = first_non_repeating_hashmap(test_str)
        optimal_result = first_non_repeating_optimal(test_str)
        enhanced_char, enhanced_pos = first_non_repeating_with_position(test_str)
        
        print(f"Brute Force: '{brute_result}'")
        print(f"HashMap: '{hashmap_result}'")
        print(f"Optimal: '{optimal_result}'")
        print(f"Enhanced: '{enhanced_char}' at position {enhanced_pos}")
        
        # Verify all approaches give same result
        results = [brute_result, hashmap_result, optimal_result, enhanced_char]
        if len(set(results)) <= 1:
            print("✅ All approaches match")
        else:
            print("❌ Results don't match!")

# Run comprehensive tests
test_non_repeating_solutions()
```

### 🔍 **HashMap vs Array Optimization**:

**Comparison**:
```python
def compare_data_structures():
    """
    Compare HashMap vs Array for character counting
    """
    import time
    
    test_string = "a" * 10000 + "b" * 10000 + "c"  # Large string with 'c' as answer
    
    # HashMap approach
    start_time = time.time()
    result1 = first_non_repeating_hashmap(test_string)
    hashmap_time = time.time() - start_time
    
    # Array approach  
    start_time = time.time()
    result2 = first_non_repeating_optimal(test_string)
    array_time = time.time() - start_time
    
    print(f"HashMap time: {hashmap_time:.6f}s, Result: '{result1}'")
    print(f"Array time: {array_time:.6f}s, Result: '{result2}'")
    print(f"Array is {hashmap_time/array_time:.2f}x faster" if array_time < hashmap_time else "HashMap is faster")

# compare_data_structures()
```

---

## 🔄 Sliding Window Pattern Recognition

### 📊 **Common Sliding Window Patterns**:

| Problem Type | Window Behavior | Key Insight |
|--------------|-----------------|-------------|
| **Fixed Size** | Constant window size | Maintain size while sliding |
| **Variable Size** | Expand/contract based on condition | Optimize window for criteria |
| **Character Frequency** | Track char counts in window | Use HashMap to maintain counts |
| **Substring Search** | Find pattern in text | KMP or rolling hash optimization |

### 🎯 **Sliding Window Implementation Template**:

```python
def sliding_window_template(s, condition_func):
    """
    Generic sliding window template
    """
    left = 0
    result = 0  # or [], "", etc. based on problem
    window_data = {}  # Track window state
    
    for right in range(len(s)):
        # Expand window: Add s[right] to window
        char = s[right]
        window_data[char] = window_data.get(char, 0) + 1
        
        # Contract window while condition is violated
        while not condition_func(window_data):
            left_char = s[left]
            window_data[left_char] -= 1
            if window_data[left_char] == 0:
                del window_data[left_char]
            left += 1
        
        # Update result based on current valid window
        result = max(result, right - left + 1)  # For maximum length problems
    
    return result
```

---

## 🧠 Logic Exercises & Visualization

### Exercise 1: Manual Palindrome Expansion
Practice the expand around center technique:

```
String: "level"
Centers to check: 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4

Center at index 2 (character 'v'):
le[v]el → Check: e == e → lev[v]ell → Check: l == l → [level] ✅
   ↑ ↑                        ↑     ↑              ↑     ↑

Your turn with "racecar":
Centers: __, __, __, __, __, __, __
Best center: __
Longest palindrome: ____________
```

### Exercise 2: Character Frequency Tracking
Trace through HashMap approach:

```
String: "abccba"
After first pass:
HashMap: {'a': __, 'b': __, 'c': __}

Second pass:
Check 'a': count = __ → ________
Check 'b': count = __ → ________  
Check 'c': count = __ → ________
Check 'c': count = __ → ________
Check 'b': count = __ → ________
Check 'a': count = __ → ________

First non-repeating: ______ (or None)
```

### Exercise 3: Sliding Window Design
Design a sliding window for this problem:

```
Problem: "Find longest substring without repeating characters"
String: "abcabcbb"

Window state tracking:
- What data structure to use? __________
- When to expand window? _____________
- When to contract window? ___________
- How to update result? ______________

Trace through first few characters:
Position 0 ('a'): window = {____}, length = __
Position 1 ('b'): window = {____}, length = __
Position 2 ('c'): window = {____}, length = __
Position 3 ('a'): window = {____}, action: ______
```

---

## 🎯 Practice Problems & Extensions

### Beginner Level:
1. **Valid Palindrome**: Check if string is palindrome ignoring case/spaces
2. **Reverse String**: Implement in-place string reversal
3. **First Unique Character**: Find first unique character in string

### Intermediate Level:
1. **Longest Substring Without Repeating Characters**: Sliding window approach
2. **Valid Anagram**: Check if two strings are anagrams
3. **Group Anagrams**: Group strings that are anagrams of each other

### Advanced Level:
1. **Minimum Window Substring**: Find smallest substring containing all characters
2. **Palindrome Pairs**: Find pairs of words that form palindromes
3. **Longest Palindromic Subsequence**: Dynamic programming approach

### 🚀 **Implementation Challenges**:

```python
# Challenge 1: Optimize palindrome detection
def is_palindrome_optimized(s):
    """Check palindrome with preprocessing"""
    # Handle case insensitive, ignore spaces/punctuation
    pass

# Challenge 2: Sliding window for anagrams
def find_all_anagrams(s, p):
    """Find all anagram substrings of p in s"""
    # Use sliding window with character frequency
    pass

# Challenge 3: Advanced string matching
def kmp_search(text, pattern):
    """Implement KMP algorithm for pattern matching"""
    # Build failure function and search
    pass
```

---

## 🚀 Performance Analysis & Optimization

### 📊 **Algorithm Comparison**:

| Problem | Brute Force | Optimized | Space | Notes |
|---------|-------------|-----------|-------|-------|
| **Longest Palindrome** | O(n³) | O(n²) | O(1) | Expand around center |
| **Non-Repeating Char** | O(n²) | O(n) | O(k) | HashMap frequency |
| **Substring Search** | O(nm) | O(n+m) | O(m) | KMP algorithm |
| **Anagram Check** | O(n log n) | O(n) | O(k) | Character frequency |

### ⚡ **String Optimization Techniques**:

1. **Character Arrays**: Use arrays instead of HashMap for ASCII
2. **Single Pass**: Combine multiple operations in one iteration
3. **Early Termination**: Stop when answer is found
4. **Memory Pooling**: Reuse data structures

### 🎯 **When to Use Each Approach**:

✅ **Expand Around Center**:
- Palindrome detection problems
- Need actual palindrome string
- Multiple palindromes to find

✅ **HashMap Frequency**:
- Character counting problems
- Anagram detection
- First/last occurrence problems

✅ **Sliding Window**:
- Substring optimization problems
- Dynamic window size needed
- Continuous character analysis

❌ **Not Suitable**:
- Random access required
- Complex string transformations
- Multi-string comparisons

---

## ✅ Key Takeaways

1. **Expand around center** reduces palindrome detection from O(n³) to O(n²)
2. **HashMap frequency counting** enables O(n) character analysis
3. **Sliding window** provides efficient substring optimization
4. **String indexing** and character operations are fundamental
5. **Space-time tradeoffs** often favor HashMap over repeated iteration
6. **ASCII optimization** can improve performance for limited character sets
7. **Pattern recognition** helps choose between different string approaches

---

## 🔗 Additional Resources

- [String Algorithms Visualization](https://visualgo.net/en/suffixarray)
- [Sliding Window Patterns](https://leetcode.com/discuss/study-guide/657507/Sliding-Window-for-Beginners-Problems-or-Template-or-Sample-Solutions)
- [Palindrome Algorithms](https://www.geeksforgeeks.org/tag/palindrome/)
- [Character Frequency Problems](https://leetcode.com/tag/hash-table/)