"""
Stack to queue converter.
"""

from arraystack import ArrayStack
from arrayqueue import ArrayQueue

def stack_to_queue(stack):
    """
    Converts stack to queue.
    """
    temp_stack = ArrayStack()
    result_queue = ArrayQueue()
    while not stack.isEmpty():
        elem = stack.pop()
        result_queue.add(elem)
        temp_stack.push(elem)
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
    return result_queue


