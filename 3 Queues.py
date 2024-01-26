"""Queue using Python Deque
Aueue is a FIFO data structure: first-In First-Out 
Deque is a double-ended queue, but we can use it for our queue.
We use append() to enqueue an item, and popleft() to dequeue an item.
"""
from collections import deque

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())

"""Fun exercise:
Write a wrapper class for the Queue class, similar to what ze did for Stacks
Try adding enqueue, dequeue, and get_size methods.
"""
# Python MaxHeap