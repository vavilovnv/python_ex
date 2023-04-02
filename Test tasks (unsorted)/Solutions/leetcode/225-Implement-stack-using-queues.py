"""
https://leetcode.com/problems/implement-stack-using-queues/description/

Category - Easy

Implement a last-in-first-out (LIFO) stack using only two queues. The
implemented stack should support all the functions of a normal stack (push,
top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        if self.queue:
            return self.queue.popleft()
        

    def top(self) -> int:
        if self.queue:
            return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
hint
we can use deque
"""
