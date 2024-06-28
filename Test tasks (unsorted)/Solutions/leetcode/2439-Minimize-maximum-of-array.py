"""
https://leetcode.com/problems/minimize-maximum-of-array/

Category - Medium

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after
performing any number of operations.
"""

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res, left, right = 0, 1, max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            tmp = nums[:]
            for i in range(len(nums)-1, 0, -1):
                if tmp[i] > mid:
                    tmp[i-1] += tmp[i] - mid
                    tmp[i] = mid
            if max(tmp) <= mid:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
