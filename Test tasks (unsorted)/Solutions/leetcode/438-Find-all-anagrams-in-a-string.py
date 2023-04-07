"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Category - Medium

Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, d, len_p = [], Counter(p), len(p)
        places = len_p
        for i, v in enumerate(s):
            d[v] -= 1
            if d[v] >= 0:
                places -= 1
            check_index = i - len_p
            if check_index >= 0:
                d[s[check_index]] += 1
                if d[s[check_index]] > 0:
                    places += 1
            if places == 0:
                res.append(check_index + 1)
        return res

"""
hint
no hint :( just the codesmells from debugger
"""
        