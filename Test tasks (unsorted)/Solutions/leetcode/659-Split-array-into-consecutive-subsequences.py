"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

Category - Medium

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such
that both of the following conditions are true:
- Each subsequence is a consecutive increasing sequence (i.e. each integer is
exactly one more than the previous integer).
- All subsequences have a length of 3 or more.

Return true if you can split nums according to the above conditions, or false
otherwise.

A subsequence of an array is a new array that is formed from the original
array by deleting some (can be none) of the elements without disturbing the
relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence
of [1,2,3,4,5] while [1,3,2] is not).
"""

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = {n: 0 for n in range(min(nums), max(nums)+2)}
        for n in nums:
            count[n] += 1
        subseq = {n: 0 for n in range(min(nums)-1, max(nums)+1)}
        for n in nums:
            if count[n]:
                count[n] -= 1
                if subseq[n - 1]:
                    subseq[n - 1] -= 1
                    subseq[n] += 1
                elif count[n + 1] and count[n + 2]:
                    count[n + 1] -= 1
                    count[n + 2] -= 1
                    subseq[n + 2] += 1
                else:
                    return False
        return True
