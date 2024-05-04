"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

Category - Easy

Given an integer array nums that does not contain any zeros, find the largest
positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
"""

# approach 1
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res, st = -1, set(nums)
        for num in nums:
            if num > 0 and -num in st:
                res = max(res, num)
        return res


# approach 2
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = {num for num in nums if num < 0}
        res = [num for num in nums if num > 0 and -num in neg]
        return max(res) if res else -1
