"""
https://leetcode.com/problems/left-and-right-sum-differences/

Category - Easy

Given a 0-indexed integer array nums, find a 0-indexed integer array answer
where:
answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array
nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array
nums. If there is no such element, rightSum[i] = 0.
Return the array answer.
"""

# TC: O(n:2) SC: O(n)
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i]) - sum(nums[i+1:])) for i in range(len(nums))]

# TC: O(n) SC: O(n)
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_nums, curr_left = [0], 0
        right_nums, curr_right = [0], 0
        for i in range(len(nums)-1):
            curr_left += nums[i]
            left_nums.append(curr_left)
            curr_right += nums[-i-1]
            right_nums.append(curr_right)
        return [abs(left_nums[i] - right_nums[-i-1]) for i in range(len(nums))]
