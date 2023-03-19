"""
https://leetcode.com/problems/sort-array-by-parity/

Category - Easy

Given an integer array nums, move all the even integers at the beginning of
the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] % 2 == 1:
                value = nums.pop(left)
                nums.append(value)
                right -= 1
            else:
                left += 1
        return nums
