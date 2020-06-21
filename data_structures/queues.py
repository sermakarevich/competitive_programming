"""
For a queue, you use a First-In/First-Out (FIFO) approach.
That means that the first element inserted in the list is the first one to be retrieved.
FIFO is an abbreviation for first in, first out.
It is a method for handling data structures where the first element is processed first
and the newest element is processed last.

he main difference between a queue and a stack is the way you retrieve elements from each.

With queues, you want to add values to a list (enqueue), and when the timing is right,
you want to remove the element that has been on the list the longest (dequeue).
For example, imagine a queue at a trendy and fully booked restaurant.
If you were trying to implement a fair system for seating guests,
then you’d start by creating a queue and adding people as they arrive:
"""

from collections import deque
queue = deque()
print(queue)

queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)

print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
