"""
https://leetcode.com/problems/letter-case-permutation/

Category - Medium

Given a string s, you can transform every letter individually to be lowercase
 or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in
any order.
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def helper(temp="", i=0):
            if len(temp) == len(s):
                res.append(temp)
            else:
                if s[i].isalpha():
                    helper(temp + s[i].swapcase(), i + 1)
                helper(temp + s[i], i + 1)
        res = []
        helper()
        return res

"""
hint
use backtracking
"""
