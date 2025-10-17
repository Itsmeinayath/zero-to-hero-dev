# 🔗 Merge Sorted Linked Lists - Complete Implementation

class ListNode:
    """Simple node class for linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists into one sorted list
    
    Time: O(n + m) where n, m are list lengths
    Space: O(1) - only pointers used
    
    Args:
        l1: Head of first sorted linked list
        l2: Head of second sorted linked list
    
    Returns:
        Head of merged sorted linked list
    """
    
    # Create dummy node to simplify edge cases
    dummy = ListNode(0)
    current = dummy
    
    # Compare and merge while both lists have nodes
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes from either list
    current.next = l1 if l1 else l2
    
    # Return merged list (skip dummy node)
    return dummy.next

def print_list(head):
    """Print linked list in readable format"""
    if not head:
        print("Empty list")
        return
    
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" → ".join(result) + " → NULL")

def create_list(values):
    """Create linked list from array of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def merge_k_lists_pairwise(lists):
    """
    Merge k sorted lists using pairwise merging
    
    Time: O(nk²) where n is average list length, k is number of lists
    Space: O(1) excluding output
    """
    if not lists:
        return None
    
    # Keep merging until only one list remains
    while len(lists) > 1:
        merged_lists = []
        
        # Merge lists in pairs
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(merge_two_sorted_lists(l1, l2))
        
        lists = merged_lists
    
    return lists[0]

# Example usage and testing
def main():
    print("🔗 Merge Sorted Linked Lists Demo\n")
    
    # Test 1: Basic merge of two lists
    print("=" * 50)
    print("Test 1: Merge Two Lists")
    print("=" * 50)
    
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    
    print("List 1: ", end="")
    print_list(list1)
    
    print("List 2: ", end="")
    print_list(list2)
    
    merged = merge_two_sorted_lists(list1, list2)
    print("Merged: ", end="")
    print_list(merged)
    
    # Test 2: One empty list
    print("\n" + "=" * 50)
    print("Test 2: One Empty List")
    print("=" * 50)
    
    list3 = create_list([1, 3, 5])
    list4 = create_list([])
    
    print("List 3: ", end="")
    print_list(list3)
    
    print("List 4: ", end="")
    print_list(list4)
    
    merged2 = merge_two_sorted_lists(list3, list4)
    print("Merged: ", end="")
    print_list(merged2)
    
    # Test 3: Different lengths
    print("\n" + "=" * 50)
    print("Test 3: Different Lengths")
    print("=" * 50)
    
    list5 = create_list([1])
    list6 = create_list([2, 3, 4, 5])
    
    print("List 5: ", end="")
    print_list(list5)
    
    print("List 6: ", end="")
    print_list(list6)
    
    merged3 = merge_two_sorted_lists(list5, list6)
    print("Merged: ", end="")
    print_list(merged3)
    
    # Test 4: Merge multiple lists
    print("\n" + "=" * 50)
    print("Test 4: Merge K Lists (Pairwise)")
    print("=" * 50)
    
    k_lists = [
        create_list([1, 4, 5]),
        create_list([1, 3, 4]),
        create_list([2, 6])
    ]
    
    for i, lst in enumerate(k_lists):
        print(f"List {i+1}: ", end="")
        print_list(lst)
    
    merged_k = merge_k_lists_pairwise(k_lists)
    print("Final Merged: ", end="")
    print_list(merged_k)

if __name__ == "__main__":
    main()

"""
🎯 Key Learning Points:

1. DUMMY NODE TECHNIQUE:
   - Simplifies edge case handling
   - Makes code cleaner and less error-prone
   - Always return dummy.next, not dummy

2. TWO POINTER APPROACH:
   - Compare current elements of both lists
   - Link smaller element to result
   - Advance pointer of selected list

3. HANDLE REMAINING ELEMENTS:
   - One list might be longer than other
   - Simply attach remaining part to result
   - No need to iterate through remaining

4. TIME COMPLEXITY:
   - Two lists: O(n + m) - visit each node once
   - K lists (pairwise): O(nk²) - can be optimized
   - K lists (heap): O(nk log k) - optimal approach

5. SPACE COMPLEXITY:
   - In-place merging: O(1) - only pointers
   - New list creation: O(n + m) - if creating new nodes

6. COMMON APPLICATIONS:
   - Merge Sort algorithm
   - Database join operations
   - File merging in external sorting
   - Combining sorted streams
"""