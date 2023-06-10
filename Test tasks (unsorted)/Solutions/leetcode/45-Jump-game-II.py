"""
https://leetcode.com/problems/jump-game-ii/

Category - Medium

You are given a 0-indexed array of integers nums of length n. You are
initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from
index i. In other words, if you are at nums[i], you can jump to any
nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are
generated such that you can reach nums[n - 1].
"""

# recursive solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i):
            if i >= len(nums) - 1:
                return 0
            res = float('inf')
            for j in range(1, nums[i] + 1):
                res = min(res, helper(i + j) + 1)
            return res

        return helper(0)

# iterative solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = temp = end = 0
        for i in range(len(nums) - 1):
            temp = max(temp, i + nums[i])
            if i == end:
                end = temp
                res += 1
        return res
