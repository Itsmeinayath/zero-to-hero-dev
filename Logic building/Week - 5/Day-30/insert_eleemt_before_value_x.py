# Here we are going to learn how to insert a node before a node with a specific value in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_before_value(head, value_to_insert, target_value):
    # Edge Case 1: List is empty or target is the head
    if head is None or head.data == target_value:
        new_node = Node(value_to_insert)
        new_node.next = head
        return new_node
    
    # Start searching for the node BEFORE the target
    previous_node = head
    while previous_node.next is not None and previous_node.next.data != target_value:
        previous_node = previous_node.next

    # Edge Case 2: Target value was not found in the list
    if previous_node.next is None:
        print(f"Value {target_value} not found. List is unchanged.")
        return head
    
    # --- Perform the Pointer Shuffle ---
    # 1. Create the new node
    new_node = Node(value_to_insert)
    # 2. Link the new node to the rest of the list (safe step)
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

# Insert 30 before the node with value 40
head = insert_before_value(head, 30, 40)

print("\nList after inserting 30 before 40:")
print_list(head)