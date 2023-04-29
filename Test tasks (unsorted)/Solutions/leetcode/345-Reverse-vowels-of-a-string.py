"""
https://leetcode.com/problems/reverse-string/

Category - Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        letters, lst = 'aeiouAEIOU', list(s)
        left, right = 0, len(lst) - 1
        while left < right:
            if lst[left] in letters and lst[right] in letters:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            elif lst[left] not in letters:
                left += 1
            elif lst[right] not in letters:
                right -= 1
        return ''.join(lst)
