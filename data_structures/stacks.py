"""
For a stack, you use a Last-In/Fist-Out (LIFO) approach,
meaning that the last element inserted in the list is the first to be retrieved.
LIFO is an abbreviation for Last in, first out is same as fist in, last out (FILO).
It is a method for handling data structures where the last element is processed first
and the first element is processed last.

the main difference between a queue and a stack is the way you retrieve elements from each.
"""

from collections import deque
history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
print(history)

print(history.popleft())
print(history)
print(history.popleft())
print(history)
print(history.popleft())
print(history)
