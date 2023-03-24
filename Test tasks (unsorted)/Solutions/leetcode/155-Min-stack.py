"""
https://leetcode.com/problems/min-stack/

Category - Medium

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31 - 1
        

    def push(self, val: int) -> None:
        if self.min >= val:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)           
        

    def pop(self) -> None:
        try:
            value = self.stack.pop()
            if value == self.min:
                self.min = self.stack.pop()
        except:
            return None

                
    def top(self) -> int:
        try:
            return self.stack[-1]
        except:
            return None
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
hint
if we get a value less than the minimum, we add the previous minimum to the
stack and remember the current one
"""
