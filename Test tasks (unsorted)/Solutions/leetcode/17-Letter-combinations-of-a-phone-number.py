"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Category - Medium

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent. Return the answer in any
order.

A mapping of digits to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(digits, combination):
            if len(combination) == len_digits:
                res.append(combination)
                return

            for i, v in enumerate(digits):
                if i != len_digits:
                    for j in d[v]:
                        helper(digits[i+1:], combination + j)

        if not digits:
            return []

        d = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        res, len_digits = [], len(digits)
        helper(digits, '')
        return res
