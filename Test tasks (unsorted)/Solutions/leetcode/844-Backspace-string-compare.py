"""
https://leetcode.com/problems/backspace-string-compare/

Category - Easy

Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    @staticmethod
    def get_stack(string):
        stack = []
        for i in string:
            if i == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_stack(s) == self.get_stack(t)

"""
hint
use stack
"""
