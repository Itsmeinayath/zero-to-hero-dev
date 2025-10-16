# Complete code for deleting a node by its value from a singly linked list.

class Node:
    """
    Represents a single node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_by_value(head, value_to_delete):
    """
    Deletes the first occurrence of a node with the given value.
    """
    # Edge Case 1: The list is empty.
    if head is None:
        print("List is empty, nothing to delete.")
        return None
    
    # Edge Case 2: The head node itself holds the value.
    if head.data == value_to_delete:
        print(f"Deleted head node with value: {value_to_delete}")
        return head.next
    
    # --- Search for the node BEFORE the target ---
    previous_node = head
    
    # This loop finds the node before our target, and safely stops
    # if the target isn't found or it reaches the end.
    while previous_node.next is not None and previous_node.next.data != value_to_delete:
        previous_node = previous_node.next

    # --- Perform Deletion (AFTER the loop) ---
    # If previous_node.next is not None, we found the node to delete.
    if previous_node.next is not None:
        print(f"Found and deleted node with value: {value_to_delete}")
        # Skip over the target node
        previous_node.next = previous_node.next.next
    else:
        # If previous_node.next is None, the value was not in the list.
        print(f"Value {value_to_delete} was not found in the list.")

    return head

def print_list(head):
    """
    A helper function to print the linked list nicely.
    """
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")

# --- Setup and Test ---

# 1. Create the linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

# 2. Print the original list
print("Original List:")
print_list(head)

# 3. Call your function to delete the node with value 30
print("\n--- Deleting node with value 30 ---")
head = delete_by_value(head, 30)

# 4. Print the final list
print("\nFinal List:")
print_list(head)