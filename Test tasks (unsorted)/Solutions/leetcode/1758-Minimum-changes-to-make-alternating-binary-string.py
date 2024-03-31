"""
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

Category - Easy

You are given a string s consisting only of the characters '0' and '1'. In one
operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For
example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        first_0, temp = 0, 0
        for c in s:
            if int(c) != temp:
                first_0 += 1
            temp = not temp
        return min(first_0, len(s) - first_0)
