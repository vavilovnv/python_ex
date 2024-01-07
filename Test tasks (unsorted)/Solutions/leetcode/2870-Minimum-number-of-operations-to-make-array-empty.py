"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

Category - Medium

You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number
of times:
Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or
-1 if it is not possible.
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        res = 0
        for v in d.values():
            if v == 1:
                return -1
            res += v // 3
            if v % 3:
                res += 1
        return res
