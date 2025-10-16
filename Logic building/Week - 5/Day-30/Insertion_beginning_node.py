# Here this file we gonna learn how to insert a node at the beginning of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # New head of the list

def print_list(head):
    if head is None:
        print("Empty list")
        return
    current = head
    while current:
        print(current.data, end= "->")
        current = current.next
    print("NULL")


# Setup and Test
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
head = node1  # Current head of the list

print("Original list:")
print_list(head)  # Print the original list

print("Inserting  at the beginning...")
head = insert_at_beginning(head, 5)  # Insert 5 at the beginning

print_list(head)  # Print the updated list
