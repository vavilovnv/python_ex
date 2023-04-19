"""
https://leetcode.com/problems/summary-ranges/

Category - Easy

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the
array exactly. That is, each element of nums is covered by exactly one of the
ranges, and there is no integer x such that x is in one of the ranges but not
in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def output(a, b):
            if b > a:
                return f'{a}->{b}'
            return str(a)
        
        if not nums:
            return nums
        res, a, b = [], nums[0], nums[0]
        for num in nums[1:]:
            if b + 1 == num:
                b = num
            else:
                res.append(output(a, b))
                a = b = num
        res.append(output(a, b))
        return res
