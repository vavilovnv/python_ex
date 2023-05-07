"""
https://leetcode.com/problems/generate-parentheses/

Category - Medium

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(brackets, open, closed):
            if len(brackets) == 2 * n:
                if open == closed:
                    res.append(brackets)
            if open < n:
                helper(brackets + '(', open + 1, closed)
            if closed < open:
                helper(brackets + ')', open, closed + 1)

        res = []
        helper('', 0, 0)
        return res
