# This problem is about deleting the last node of a singly linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def delete_last_node(head):
    # First, handle the case when the list is empty
    if head is None:
        print("List is empty, nothing to delete.")
        return None
    
    # If there's only one node, delete it and return None
    if head.next is None:
        print(f"Deleted: {head.data}")
        return None

    second_last = head

    while second_last.next.next is not None:
        second_last = second_last.next
    
    last_node = second_last.next
    print(f"Deleted: {last_node.data}")

    second_last.next = None
    return head

# Setup and Test

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3

def print_list(head):
    if head is None:
        print("Empty list")
        return
    
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print(" -> NULL")

print("Original list:")
print_list(node1)  # Actually call the function to print original list

print("Deleting last node...")
head = delete_last_node(node1)

print("List after deletion:")
print_list(head)