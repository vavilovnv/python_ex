"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

Category - Easy

You are given a string s formed by digits and '#'. We want to map s to English
lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        d, count, res = {}, 1, []
        for i in ascii_lowercase:
            d[str(count) if count < 10 else f'{count}#'] = i
            count += 1
        while len(s) > 0:
            limit = 3 if s[:3] in d else 1
            res.append(d[s[:limit]])
            s = s[limit:]
        return ''.join(map(str, res))
