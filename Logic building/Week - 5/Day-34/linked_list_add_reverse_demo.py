class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(vals):
    """Create a linked list from array of values"""
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


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
    print(" → ".join(result))


def addTwoNumbers(l1, l2):
    """Add two numbers represented as linked lists"""
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10
        
        current.next = ListNode(digit)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next


def reverseKGroup(head, k):
    """Reverse linked list in groups of k nodes"""
    # Count total nodes
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    current = head
    
    # Process complete groups only
    while count >= k:
        # Reverse k nodes
        group_head = current
        prev = None
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Connect reversed group
        prev_group.next = prev  # New head of reversed group
        group_head.next = current  # Old head (now tail) points to next
        prev_group = group_head
        
        count -= k
    
    return dummy.next


def main():
    print("=" * 60)
    print("Problem 1: Add Two Numbers")
    print("=" * 60)
    
    # Test 1: Basic addition
    print("\nTest 1: 342 + 465 = 807")
    print("Lists: [2,4,3] + [5,6,4]")
    l1 = make_list([2, 4, 3])
    l2 = make_list([5, 6, 4])
    print("L1: ", end="")
    print_list(l1)
    print("L2: ", end="")
    print_list(l2)
    result = addTwoNumbers(l1, l2)
    print("Sum: ", end="")
    print_list(result)
    
    # Test 2: Different lengths
    print("\nTest 2: Different length lists")
    print("Lists: [9,9,9] + [1]")
    l3 = make_list([9, 9, 9])
    l4 = make_list([1])
    print("L1: ", end="")
    print_list(l3)
    print("L2: ", end="")
    print_list(l4)
    result2 = addTwoNumbers(l3, l4)
    print("Sum: ", end="")
    print_list(result2)
    
    # Test 3: Final carry
    print("\nTest 3: Final carry creates extra digit")
    print("Lists: [9,9] + [1]")
    l5 = make_list([9, 9])
    l6 = make_list([1])
    print("L1: ", end="")
    print_list(l5)
    print("L2: ", end="")
    print_list(l6)
    result3 = addTwoNumbers(l5, l6)
    print("Sum: ", end="")
    print_list(result3)
    
    print("\n" + "=" * 60)
    print("Problem 2: Reverse Linked List in Groups")
    print("=" * 60)
    
    # Test 4: Reverse in groups of 2
    print("\nTest 4: Reverse groups of 2")
    print("List: [1,2,3,4,5,6,7,8], k=2")
    list1 = make_list([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original: ", end="")
    print_list(list1)
    reversed1 = reverseKGroup(list1, 2)
    print("Reversed: ", end="")
    print_list(reversed1)
    
    # Test 5: Reverse in groups of 3
    print("\nTest 5: Reverse groups of 3 (with remainder)")
    print("List: [1,2,3,4,5,6,7,8], k=3")
    list2 = make_list([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original: ", end="")
    print_list(list2)
    reversed2 = reverseKGroup(list2, 3)
    print("Reversed: ", end="")
    print_list(reversed2)
    print("Note: Last 2 nodes (7,8) stay as-is (not enough for group of 3)")
    
    # Test 6: Reverse in groups of 4
    print("\nTest 6: Reverse groups of 4")
    print("List: [1,2,3,4,5,6,7,8], k=4")
    list3 = make_list([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original: ", end="")
    print_list(list3)
    reversed3 = reverseKGroup(list3, 4)
    print("Reversed: ", end="")
    print_list(reversed3)
    
    # Test 7: k larger than list
    print("\nTest 7: k larger than list length")
    print("List: [1,2,3], k=5")
    list4 = make_list([1, 2, 3])
    print("Original: ", end="")
    print_list(list4)
    reversed4 = reverseKGroup(list4, 5)
    print("Reversed: ", end="")
    print_list(reversed4)
    print("Note: No complete group, list stays as-is")


if __name__ == "__main__":
    main()
