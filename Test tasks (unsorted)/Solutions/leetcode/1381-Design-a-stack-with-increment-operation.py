"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/

Category - Medium

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:
- CustomStack(int maxSize) Initializes the object with maxSize which is the
maximum number of elements in the stack.
- void push(int x) Adds x to the top of the stack if the stack has not reached
the maxSize.
- int pop() Pops and returns the top of the stack or -1 if the stack is empty.
- void inc(int k, int val) Increments the bottom k elements of the stack by
val. If there are less than k elements in the stack, increment all the
elements in the stack.  
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self._max_size = maxSize
        self._stack = []

    def push(self, x: int) -> None:
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop() if self._stack else -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val
