"""
https://leetcode.com/problems/group-anagrams/

Category - Medium

Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res, d = [], {}
        for s in strs:
            k = ''.join(sorted(list(s)))
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        for k in d:
            res.append(d[k])
        return res
