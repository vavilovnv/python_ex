"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Category - Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid
strings, or
It can be written as (A), where A is a valid string.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, res = [], list(s)
        for i, v in enumerate(res):
            if v == "(":
                stack.append(i)
            if v == ")":
                if stack:
                    stack.pop()
                else:
                    res[i] = ""
        while stack:
            res[stack.pop()] = ""
        return "".join(res)
