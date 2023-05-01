"""
https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

Category - Easy

You are given a 0-indexed integer array nums and an integer k. Your task is to
perform the following operation exactly k times in order to maximize your
score:
Select an element m from nums.
Remove the selected element m from the array.
Add a new element with a value of m + 1 to the array.
Increase your score by m.
Return the maximum score you can achieve after performing the operation
exactly k times.
"""

# TC: O(nlogn) SC: O(n+k)
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        for _ in range(k):
            m = nums.pop()
            nums.append(m + 1)
            res += m
        return res

# TC: O(n) SC: O(n)
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res, mx = 0, max(nums)
        for i in range(k):
            res += mx + i
        return res
