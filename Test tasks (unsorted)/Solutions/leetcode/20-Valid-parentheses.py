"""
https://leetcode.com/problems/valid-parentheses/

Category - Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            if i in ')]}':
                if not stack:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack


"""
hint
just use stack
"""
