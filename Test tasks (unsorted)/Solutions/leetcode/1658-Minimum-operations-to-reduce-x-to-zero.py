"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Category - Medium

You are given an integer array nums and an integer x. In one operation, you
can either remove the leftmost or the rightmost element from the array nums
and subtract its value from x. Note that this modifies the array for future
operations.

Return the minimum number of operations to reduce x to exactly 0 if it is
possible, otherwise, return -1.
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        len_nums, sum_nums, temp = len(nums), sum(nums), {0: -1}
        new_len_nums, new_sum_nums, diff = 0, 0, sum_nums - x
        if diff == 0: 
            return len_nums
        for i, num in enumerate(nums):
            new_sum_nums += num
            if new_sum_nums - diff in temp:
                new_len_nums = max(new_len_nums, i - temp[new_sum_nums - diff])
            if new_sum_nums not in temp:
                temp[new_sum_nums] = i
        return [len_nums - new_len_nums, -1][new_len_nums == 0]
