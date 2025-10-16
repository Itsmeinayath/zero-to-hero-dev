# The Node class (as you defined)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A helper function to print the list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")

# Your delete_kth_node function (perfectly written)
def delete_kth_node(head, k):
    if head is None:
      return None

    if k == 1:
        return head.next
        
    previous_node = head
    count = 1

    while count < k - 1 and previous_node is not None:
        previous_node = previous_node.next
        count += 1

    if previous_node is None or previous_node.next is None:
        return head

    previous_node.next = previous_node.next.next

    return head

# --- Setup ---
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

print("Original List:")
print_list(head)

# --- Test Case ---
k = 3
print(f"\nDeleting node at position {k}...")
head = delete_kth_node(head, k)

print("List after deletion:")
print_list(head)