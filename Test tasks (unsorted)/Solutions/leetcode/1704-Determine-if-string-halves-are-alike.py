"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/

Category - Easy

You are given a string s of even length. Split this string into two halves of
equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i1, i2 = 0, 0
        w1, w2 = s[:len(s) // 2], s[len(s) // 2:]
        vowel = 'aeiouAEIOU'
        for i in range(len(w1)):
            if w1[i] in vowel:
                i1 += 1
            if w2[i] in vowel:
                i2 += 1
        return i1 == i2
