# Delete First Node from Linked List
# Simple and clean implementation

class Node:
    # Each node has data and points to next node
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_first_node(head):
    """
    Delete the first node from linked list
    
    Visual:
    Before: [10] -> [20] -> [30] -> NULL
             ↑
           Head (delete this)
    
    After:  [20] -> [30] -> NULL
            ↑
         New Head
    """
    
    # Step 1: Check if list is empty
    if head is None:
        print("List is empty, nothing to delete")
        return None
    
    # Step 2: Save the new head (second node)
    new_head = head.next
    
    # Step 3: Return new head
    print(f"Deleted: {head.data}")
    return new_head

def print_list(head):
    # Print the entire list
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

# Example usage
if __name__ == "__main__":
    # Create nodes
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    # Link them
    node1.next = node2
    node2.next = node3
    
    head = node1
    
    print("Original list:")
    print_list(head)
    
    # Delete first node
    head = delete_first_node(head)
    
    print("After deleting first node:")
    print_list(head)
    
    # Delete another node
    head = delete_first_node(head)
    
    print("After deleting first node again:")
    print_list(head)
    
    # Delete last node
    head = delete_first_node(head)
    
    print("After deleting last node:")
    print_list(head)
    
    # Try deleting from empty list
    head = delete_first_node(head)
    print_list(head)