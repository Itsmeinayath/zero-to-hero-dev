# --- This is the blueprint for our Node ---
class DLLNode:
    """
    A node in a Doubly-Linked List.
    """
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# --- This is our main Deque class ---
class MyDeque:
    """
    A Deque (Double-Ended Queue) implemented from scratch
    using a Doubly-Linked List.
    """
    def __init__(self):
        # We keep track of both ends
        self.head = None
        self.tail = None
        self.size = 0  # Keep track of the size
        print("New MyDeque created.")

    def is_empty(self):
        """Returns True if the deque is empty, False otherwise."""
        return self.size == 0

    def add_to_front(self, item):
        """Adds an item to the front (head) of the deque."""
        print(f"Adding {item} to front...")
        new_node = DLLNode(item)

        # We must check if it's empty *before* we change the size
        if self.is_empty():
            # Scenario 1: The deque is EMPTY
            # The new node is both the head and the tail
            self.head = new_node
            self.tail = new_node
        else:
            # Scenario 2: The deque is NOT empty
            # 1. Link new node to the old head
            new_node.next = self.head
            # 2. Link old head back to the new node
            self.head.prev = new_node
            # 3. Re-assign self.head to be the new node
            self.head = new_node
        
        # Now we can safely increment the size
        self.size += 1

    def add_to_back(self, item):
        """Adds an item to the back (tail) of the deque."""
        print(f"Adding {item} to back...")
        
        # 1. Create the new node first (DRY principle)
        new_node = DLLNode(item)

        # 2. Check for the empty case
        if self.is_empty():
            # The new node is both the head and the tail
            self.head = new_node
            self.tail = new_node
        else:
            # 3. Wire up the new node to the end
            # Link old tail forward to new node
            self.tail.next = new_node
            # Link new node back to old tail
            new_node.prev = self.tail
            # Re-assign self.tail to be the new node
            self.tail = new_node
        
        # 4. Increment the size (always happens)
        self.size += 1

    def remove_from_front(self):
        """Removes and returns the item from the front (head)."""
        print("Removing from front...")
        if self.is_empty():
            print("Deque is empty, cannot remove from front.")
            return None
        
        # Get the value to return
        removed_value = self.head.value
        
        # Decrement size
        self.size -= 1

        # Check the "1-item list" edge case
        if self.size == 0:
            # The list is now empty
            self.head = None
            self.tail = None
        else:
            # The "normal" case
            self.head = self.head.next
            self.head.prev = None
            
        return removed_value

    def remove_from_back(self):
        """Removes and returns the item from the back (tail)."""
        print("Removing from back...")
        if self.is_empty():
            print("Deque is empty, cannot remove from back.")
            return None
        
        # Get the value to return
        removed_value = self.tail.value

        # Decrement size
        self.size -= 1
        
        # Check the "1-item list" edge case
        if self.size == 0:
            # The list is now empty
            self.head = None
            self.tail = None
        else:
            # The "normal" case
            # FIX: self.taile -> self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        
        # FIX: Added the missing return statement
        return removed_value

    def get_front(self):
        if self.is_empty():
            print("Deque is empty, cannot get front.")
            return None
        return self.head.value
    
    def get_back(self):
        if self.is_empty():
            print("Deque is empty, cannot get back.")
            return None
        return self.tail.value

    def get_size(self):
        """Returns the current size of the deque."""
        return self.size



def main():
    deque = MyDeque()
    print("Is deque empty?", deque.is_empty())
    deque.add_to_front(10)
    deque.add_to_back(20)
    deque.add_to_front(5)
    deque.add_to_back(25)
    print("the deque now is:    ", end="")
    current = deque.head
    while current:
        print(current.value, end=" <-> ")
        current = current.next
    print("None")
    print("------------------------------")

    print("Front item:", deque.get_front())  # Should be 5
    print("Back item:", deque.get_back())    # Should be 25
    print("Current size:", deque.get_size()) # Should be 4
    print("Removed from front:", deque.remove_from_front()) # Should be 5
    print("Removed from back:", deque.remove_from_back())   # Should be 25
    print("Current size after removals:", deque.get_size()) # Should be 2
    print("Is deque empty?", deque.is_empty())
    print("Removed from front:", deque.remove_from_front()) # Should be 10
    print("Removed from back:", deque.remove_from_back())   # Should be 20
    print("Is deque empty now?", deque.is_empty())
    print("Current size after all removals:", deque.get_size()) # Should be 0
if __name__ == "__main__":
    main()