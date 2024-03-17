"""
https://leetcode.com/problems/maximum-erasure-value/

Category - Medium

You are given an array of positive integers nums and want to erase a subarray
containing unique elements. The score you get by erasing the subarray is
equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous
subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some
(l,r).
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        m, s, j, u = 0, 0, 0, set()
        for i in range(len(nums)):
            while j < i and nums[i] in u:
                u.remove(nums[j])
                s -= nums[j]
                j += 1
            s += nums[i]
            m = max(m, s)
            u.add(nums[i])
        return m
