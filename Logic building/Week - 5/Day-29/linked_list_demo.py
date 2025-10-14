"""
🔗 LINKED LIST IMPLEMENTATION AND DEMONSTRATION
==============================================

This file contains a complete implementation of a singly linked list
with basic operations: create, insert, traverse, search, and delete.
"""

class Node:
    """Single node in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Complete linked list implementation"""
    def __init__(self):
        self.head = None  # Points to first node
        self.size = 0     # Keep track of list size
    
    def is_empty(self):
        """Check if list is empty"""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Insert new node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head  # Point to current first node
        self.head = new_node       # Update head to new node
        self.size += 1
        print(f"✅ Inserted {data} at beginning")
    
    def insert_at_end(self, data):
        """Insert new node at the end"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            current.next = new_node  # Link last node to new node
        
        self.size += 1
        print(f"✅ Inserted {data} at end")
    
    def display(self):
        """Print the entire linked list"""
        if self.is_empty():
            print("📋 List is empty")
            return
        
        print("📋 Linked List: ", end="")
        current = self.head
        
        while current:
            if current.next:
                print(f"[{current.data}] → ", end="")
            else:
                print(f"[{current.data}] → NULL")
            current = current.next
        
        print(f"📊 Size: {self.size}")
    
    def traverse_and_print(self):
        """Traverse and print each element"""
        if self.is_empty():
            print("📋 List is empty")
            return
        
        print("🔄 Traversing linked list:")
        current = self.head
        position = 0
        
        while current:
            print(f"  Position {position}: {current.data}")
            current = current.next
            position += 1
    
    def search(self, target):
        """Search for a value in the list"""
        if self.is_empty():
            return -1
        
        current = self.head
        position = 0
        
        while current:
            if current.data == target:
                print(f"🔍 Found {target} at position {position}")
                return position
            current = current.next
            position += 1
        
        print(f"❌ {target} not found in the list")
        return -1
    
    def get_length(self):
        """Get the length of the list"""
        return self.size
    
    def delete_by_value(self, target):
        """Delete first occurrence of target value"""
        if self.is_empty():
            print("❌ Cannot delete from empty list")
            return
        
        # If head node contains target
        if self.head.data == target:
            self.head = self.head.next
            self.size -= 1
            print(f"🗑️ Deleted {target} from beginning")
            return
        
        # Search for target in rest of the list
        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next  # Skip the target node
                self.size -= 1
                print(f"🗑️ Deleted {target} from list")
                return
            current = current.next
        
        print(f"❌ {target} not found for deletion")

def main():
    """Main demonstration function"""
    print("🔗 LINKED LIST DEMONSTRATION")
    print("=" * 40)

    # Create a new linked list
    my_list = LinkedList()

    # Check if empty
    print(f"Is list empty? {my_list.is_empty()}")
    my_list.display()

    print("\n📥 INSERTING ELEMENTS:")
    print("-" * 25)

    # Insert elements
    my_list.insert_at_beginning(10)
    my_list.insert_at_beginning(5)
    my_list.insert_at_end(20)
    my_list.insert_at_end(30)
    my_list.insert_at_beginning(1)

    print(f"\nFinal list after insertions:")
    my_list.display()

    print("\n🔄 TRAVERSAL:")
    print("-" * 15)
    my_list.traverse_and_print()

    print("\n🔍 SEARCHING:")
    print("-" * 15)
    my_list.search(20)  # Should find it
    my_list.search(100) # Should not find it

    print(f"\n📊 List length: {my_list.get_length()}")

    print("\n🗑️ DELETION:")
    print("-" * 15)
    my_list.delete_by_value(20)
    my_list.delete_by_value(1)
    my_list.display()

    print("\n🎯 FINAL STATE:")
    print("-" * 15)
    my_list.traverse_and_print()

if __name__ == "__main__":
    main()