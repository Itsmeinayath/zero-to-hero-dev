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


def middleNode(head):
    """Find the middle node using slow/fast pointers"""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def removeNthFromEnd(head, n):
    """Remove nth node from end using two-pointer gap technique"""
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    # Create gap of n nodes
    for _ in range(n):
        fast = fast.next
    
    # Move both until fast reaches last node
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    # Delete node after slow
    slow.next = slow.next.next
    
    return dummy.next


def main():
    print("=" * 60)
    print("Problem 1: Middle of the Linked List")
    print("=" * 60)
    
    # Test 1: Odd length
    print("\nTest 1: Odd length list [1, 2, 3, 4, 5]")
    list1 = make_list([1, 2, 3, 4, 5])
    print("Original: ", end="")
    print_list(list1)
    middle1 = middleNode(list1)
    print(f"Middle node value: {middle1.val}")
    
    # Test 2: Even length
    print("\nTest 2: Even length list [1, 2, 3, 4, 5, 6]")
    list2 = make_list([1, 2, 3, 4, 5, 6])
    print("Original: ", end="")
    print_list(list2)
    middle2 = middleNode(list2)
    print(f"Middle node value: {middle2.val} (second middle)")
    
    print("\n" + "=" * 60)
    print("Problem 2: Remove Nth Node From End")
    print("=" * 60)
    
    # Test 3: Remove 2nd from end
    print("\nTest 3: Remove 2nd from end of [1, 2, 3, 4, 5]")
    list3 = make_list([1, 2, 3, 4, 5])
    print("Original: ", end="")
    print_list(list3)
    list3 = removeNthFromEnd(list3, 2)
    print("After removing 2nd from end: ", end="")
    print_list(list3)
    
    # Test 4: Remove last node
    print("\nTest 4: Remove last node (1st from end) of [1, 2, 3]")
    list4 = make_list([1, 2, 3])
    print("Original: ", end="")
    print_list(list4)
    list4 = removeNthFromEnd(list4, 1)
    print("After removing last: ", end="")
    print_list(list4)
    
    # Test 5: Remove head (edge case)
    print("\nTest 5: Remove head of [1, 2] (2nd from end)")
    list5 = make_list([1, 2])
    print("Original: ", end="")
    print_list(list5)
    list5 = removeNthFromEnd(list5, 2)
    print("After removing head: ", end="")
    print_list(list5)
    
    # Test 6: Single node
    print("\nTest 6: Remove from single node [1]")
    list6 = make_list([1])
    print("Original: ", end="")
    print_list(list6)
    list6 = removeNthFromEnd(list6, 1)
    print("After removal: ", end="")
    print_list(list6)


if __name__ == "__main__":
    main()
