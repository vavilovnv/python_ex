"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Category - Medium

Given two integers n and k, return an array of all the integers of length n
where the difference between every two consecutive digits is k. You may return
the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043
are not allowed.
"""

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = list(range(1,10))
        while n > 1:
            tmp = []
            for value in res:
                r = value % 10
                if r + k < 10:
                    tmp.append(value * 10 + r + k)
                if k != 0 and r - k >= 0:
                    tmp.append(value * 10 + r - k)
            res = tmp
            n -= 1
        return res
