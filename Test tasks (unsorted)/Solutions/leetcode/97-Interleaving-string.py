"""
https://leetcode.com/problems/interleaving-string/

Category - Medium

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are
divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or 
t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def check(x, y, z):
            if x == len(s1) and y == len(s2) and z == len(s3):
                return True
            res1 = res2 = False
            if x < len(s1) and s1[x] == s3[z]:
                res1 = check(x+1, y, z+1)
                if res1: 
                    return True
            if y < len(s2) and s2[y] == s3[z]:
                res2 = check(x, y+1, z+1)
            return res1 or res2

        if len(s1) + len(s2) != len(s3):
            return False
        return check(0, 0, 0)
