# This file demonstrates the fundamental concepts of linked lists with
# proper terminology, clear explanations, and corrected implementations.

# Delete the first node of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_List(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("NULL")

node1 = Node(10)
node2 = Node(20)    
node3 = Node(30)
node1.next = node2
node2.next = node3

print("Original List:")
print_List(node1)

# Deleting the first node

head  = node1  # Head points to the first node

def delete_first_node(head):
    if head is None:
        return None  # List is empty, nothing to delete
    new_head = head.next

    return new_head

print("\nDeleting the first node...")
head = delete_first_node(head)
print("List after deleting the first node:")
print_List(head)