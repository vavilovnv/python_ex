"""
https://leetcode.com/problems/valid-parenthesis-string/

Category - Medium

Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string "".
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        st1, st2 = [], []
        for i, v in enumerate(s):
            if v == "(":
                st1.append(i)
            elif v == "*":
                st2.append(i)
            else:
                if st1:
                    st1.pop()
                elif st2:
                    st2.pop()
                else:
                    return False
        while st1 and st2:
            if st1.pop() > st2.pop():
                return False
        return not st1
