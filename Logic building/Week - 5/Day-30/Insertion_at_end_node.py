# Here we are going to learn how to insert a node at the end of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    # Step 1: Create the new node.
    new_node = Node(data)
    
    # Step 2 (Edge Case): If the list is empty, the new node is the head.
    if head is None:
        return new_node
    
    # Step 3: Start a pointer at the head to find the end.
    temp_pointer = head
    while temp_pointer.next is not None:
        temp_pointer = temp_pointer.next

    # Step 4: Link the last node to the new node.
    temp_pointer.next = new_node
    
    # Step 5: Return the original, unchanged head.
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
node3 = Node(30)
node1.next = node2
node2.next = node3
head = node1

print("Original List:")
print_list(head)

# Insert 40 at the end and update the head variable (though it doesn't change)
head = insert_at_end(head, 40)

print("\nList after inserting at the end:")
print_list(head)