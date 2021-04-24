"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def queue_to_stack(queue):
    """
    Converts queue to stack.
    """
    temp_queue = ArrayQueue()
    temp_stack = ArrayStack() #elements are in reversed order
    result_stack = ArrayStack()
    while not queue.isEmpty():
        elem = queue.pop()
        temp_queue.add(elem)
        temp_stack.push(elem)
    while not temp_queue.isEmpty():
        queue.add(temp_queue.pop())
    while not temp_stack.isEmpty():
        result_stack.push(temp_stack.pop()) #we reverse elements
    return result_stack

queue = ArrayQueue()
for i in range(10):
    queue.add(i)
stack = queue_to_stack(queue)
print(queue)
print(stack)