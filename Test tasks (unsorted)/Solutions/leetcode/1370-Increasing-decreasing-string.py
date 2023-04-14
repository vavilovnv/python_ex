"""
https://leetcode.com/problems/increasing-decreasing-string/

Category - Easy

You are given a string s. Reorder the string using the following algorithm:
Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended
character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended
character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once
you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""

class Solution:
    def sortString(self, s: str) -> str:
        res, d = [], Counter(s)
        keys = sorted(d)
        len_k, changed = len(keys), True
        while changed:
            changed = False
            for k in keys:
                if d[k] > 0:
                    res.append(k)
                    d[k] -= 1
                    changed = True
            for i in range(len_k-1, -1, -1):
                if d[keys[i]] > 0:
                    res.append(keys[i])
                    d[keys[i]] -= 1
                    changed = True
        return ''.join(res)
