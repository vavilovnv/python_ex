"""
https://leetcode.com/problems/4sum/

Category - Hard

Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution:
    def two_sum(self, start, target):
        left, right = start, len(self.nums) - 1
        while left < right:
            val = self.nums[left] + self.nums[right]
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                self.result.append(self.prefix + [self.nums[left], self.nums[right]])
                left += 1
                while left < right and self.nums[left] == self.nums[left - 1]:
                    left += 1

    def n_sum(self, n, start, target):
        if n == 2:
            self.two_sum(start, target)
            return

        for i in range(start, len(self.nums) - n + 1):
            if i > start and self.nums[i] == self.nums[i - 1]:
                continue
            self.prefix.append(self.nums[i])
            self.n_sum(n - 1, i + 1, target - self.nums[i])
            self.prefix.pop()


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.prefix = []
        self.nums = nums

        self.nums.sort()
        self.n_sum(4, 0, target)

        return self.result
