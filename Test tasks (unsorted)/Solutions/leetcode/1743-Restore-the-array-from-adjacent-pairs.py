"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

Category - Medium

There is an integer array nums that consists of n unique elements, but you
have forgotten it. However, you do remember every pair of adjacent elements in
nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each
adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent
in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1]
will exist in adjacentPairs, either as [nums[i], nums[i+1]] or 
[nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of
them.
"""

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res, cache = [], defaultdict(list)
        
        for a, b in adjacentPairs:
            cache[a].append(b)
            cache[b].append(a)

        for k, v in cache.items():
            if len(v) == 1:
                res.append(k)
                res.append(v[0])
                break

        while len(res) <= len(adjacentPairs):
            last, prev = res[-1], res[-2]
            if cache[last][0] == prev:
                res.append(cache[last][1])
            else:
                res.append(cache[last][0])

        return res
