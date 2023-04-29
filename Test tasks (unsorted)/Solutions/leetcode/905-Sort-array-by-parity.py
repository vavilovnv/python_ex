"""
https://leetcode.com/problems/sort-array-by-parity/

Category - Easy

Given an integer array nums, move all the even integers at the beginning of
the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

# TC: O(n^2), SC: O(1)
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
    
# TC: O(n), SC: O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        curr = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1
        return nums
