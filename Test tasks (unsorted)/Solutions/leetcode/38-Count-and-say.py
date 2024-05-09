"""
https://leetcode.com/problems/count-and-say/

Category - Medium

The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run). For example, to compress the string "3322251"
we replace "33" with "23", replace "222" with "32", replace "5" with "15" and
replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say
sequence.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(1, n):
            tmp, count, prev = [], 1, res[0]
            for curr in res[1:]:
                if curr == prev:
                    count += 1
                    continue
                tmp.extend([str(count), prev])
                count, prev = 1, curr
            tmp.extend([str(count), prev])   
            res = "".join(tmp)
        return res
