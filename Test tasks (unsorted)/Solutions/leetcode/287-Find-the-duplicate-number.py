"""
https://leetcode.com/problems/find-the-duplicate-number/

Category - Medium

Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only
constant extra space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

"""
hint
the problem is solved in the same way as the problem with the looped linked
list (142-Linked-list-cycle-II)
"""