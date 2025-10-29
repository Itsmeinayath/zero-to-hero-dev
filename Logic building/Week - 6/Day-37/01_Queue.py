from collections import deque

# This example demonstrates basic queue operations using Python's deque from collections module.
# We are using ticketing system analogy where people join a line (enqueue) and are served in order (dequeue). (FIFO - First In First Out) .import no one is getting in middle of the line.
# Creating a new queue
queue = deque()

# Enqueue people (Enqueue means adding to the end of the queue)
print(f"New queue created: {queue} ")
print("Person 'A' gets in line.")
queue.append('A')
print("Person 'B' gets in line.")
queue.append('B')
print("Person 'C' gets in line.")
queue.append('C')

print(f"Current queue: {queue}")
print("------------------------------")

# Peek at the front person
front_person = queue[0]
print(f"Front person (peek): {front_person}")
print(f"Queue after peek (unchanged): {queue}")
print("------------------------------")

# Dequeue people (Dequeue means removing from the front of the queue)
removed_item = queue.popleft()
print(f"Served person : {removed_item}")
print(f"Current queue after serving: {queue}")
removed_item = queue.popleft()
print(f"Served person : {removed_item}")
print(f"Current queue after serving: {queue}")
print("Is queue empty?", len(queue) == 0)
removed_item = queue.popleft()
print(f"Served person : {removed_item}")
print(f"Current queue after serving: {queue}")
print("------------------------------")

