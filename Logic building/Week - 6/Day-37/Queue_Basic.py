from collections import deque

class MyQueue:
    def __init__(self):
        self.data = deque()  # Initialize an empty deque to store queue elements
        print(f"New queue created: {self.data} ")

    def enqueue(self,item):
        self.data.append(item)
        print(f"person '{item}' gets in line")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        item = self.data.popleft()
        print(f"Served person :'{item}'")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty, nothing to peek.")
            return None
        item = self.data[0]
        print(f"Front person (peek): '{item}'")
        return item
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    

# Setup and Test

queue = MyQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(f"Current queue: {queue.data}")
print("------------------------------")
# Peek at the front person
front_person = queue.peek()
print(f"Queue after peek (unchanged): {queue.data}")
print("------------------------------")

# Dequeue people
removed_item = queue.dequeue()
print(f"Current queue after serving: {queue.data}")
removed_item = queue.dequeue()
print(f"Current queue after serving: {queue.data}")
print("Is queue empty?", queue.is_empty())
removed_item = queue.dequeue()
print(f"Current queue after serving: {queue.data}")
print("------------------------------")