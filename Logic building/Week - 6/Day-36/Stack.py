"""Simple Stack implementation in Python.

This Stack is a thin wrapper around a Python list and provides the
common stack operations: push, pop, peek, is_empty, size, and clear.

Usage:
	s = Stack()
	s.push(1)
	s.push(2)
	print(s.pop())  # 2
"""

stack = []

print(f"New stack created: {stack}")
print("Pushing 1 onto stack.")
stack.append(1)
print("Pushing 2 onto stack.")
stack.append(2)
print("Pushing 3 onto stack.")
stack.append(3)
print(f"Current stack: {stack}")
print("------------------------------")
# Peek at the top element
top_element = stack[-1] 
print(f"Top element (peek): {top_element}")
print("------------------------------")
# Pop elements from the stack
print("Popping from stack.")
element_removed = stack.pop()
print(f"Popped element: {element_removed}")
print(f"Current stack after pop: {stack}")
element_removed = stack.pop()
print(f"Popped element: {element_removed}")
print(f"Current stack after pop: {stack}")
print("Is stack empty?", len(stack) == 0)
print("Popping last element from stack.")
element_removed = stack.pop()
print(f"Popped element: {element_removed}")
print(f"Current stack after pop: {stack}")
print("------------------------------")


# Implementing stack using array

class MyStack:
    def __init__(self):
        self.data = [] # Initialize an empty list to store stack elements
    
    def push(self,item):
        self.data.append(item) # Add item to the top of the stack
        print(f"Pushed {item} onto stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        item = self.data.pop()  # Remove and return the top item
        print(f"Popped {item} from stack.")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        item = self.data[-1]   # Return the top item without removing it
        print(f"Top element (peek): {item}")
        return item
    
    def is_empty(self):
        return len(self.data) == 0 # Check if stack is empty
    
    def size(self):
        return len(self.data)    # Return the number of items in the stack
    
    def clear(self):
        self.data.clear()       # Remove all items from the stack
        print("Stack cleared.")

# Example usage of MyStack
if __name__ == "__main__":
    stack = MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    print(f"Stack size: {stack.size()}")
    stack.pop()
    stack.peek()
    print(f"Is stack empty? {stack.is_empty()}")
    stack.pop()
    stack.pop()
    print(f"Is stack empty? {stack.is_empty()}")
    stack.pop()  # Attempt to pop from empty stack
    stack.clear()
    