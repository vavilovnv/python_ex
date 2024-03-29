"""
https://leetcode.com/problems/jump-game-vi/

Category - Medium

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k
steps forward without going outside the boundaries of the array. That is, you
can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
inclusive.

You want to reach the last index of the array (index n - 1). Your score is the
sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.
"""

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums) - 1, -1, -1):
            while heap and heap[0][1] > i + k:
                heapq.heappop(heap)
            if heap:
                res = - nums[i] + heap[0][0]
            else:
                res = - nums[i]
            heapq.heappush(heap, (res, i))
        return -res
