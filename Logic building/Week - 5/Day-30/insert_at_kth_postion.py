# Here we are going to learn how to insert a node at the k-th position of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_kth_position(head, data, k):
    # Edge Case 1: k is invalid (less than 1)
    if k < 1:
        print("Position must be 1 or greater.")
        return head

    # Edge Case 2: Inserting at the beginning
    if k == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    # Start traversal to find the (k-1)th node
    previous_node = head
    count = 1
    while count < k - 1 and previous_node is not None:
        previous_node = previous_node.next
        count += 1

    # Edge Case 3: k is out of bounds (greater than list length + 1)
    if previous_node is None:
        print(f"Position {k} is out of bounds.")
        return head

    # --- Perform the Pointer Shuffle ---
    # 1. Create the new node
    new_node = Node(data)
    # 2. Link the new node to the rest of the list
    new_node.next = previous_node.next
    # 3. Link the previous node to the new node
    previous_node.next = new_node

    return head

def print_list(head):
    """Helper function to print the list"""
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")

# --- Setup and Test ---
node1 = Node(10)
node2 = Node(20)
node3 = Node(40)
node1.next = node2
node2.next = node3
head = node1

print("Original List:")
print_list(head)

# Insert 30 at position 3
head = insert_at_kth_position(head, 30, 3)

print("\nList after inserting at position 3:")
print_list(head)