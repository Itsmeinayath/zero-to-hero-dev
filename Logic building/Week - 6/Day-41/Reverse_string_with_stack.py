class solution:
    def reverse_string(self,s:str) -> str:
        stack = []
        result_string = ""
        for char in s:
            stack.append(char)

        while stack:
                result_string += stack.pop()
        return result_string
    
"""Implementing a stack using an array (list in Python)
A stack follows Last In First Out (LIFO) principle. 
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
