"""
https://leetcode.com/problems/occurrences-after-bigram/

Category - Easy

Given two strings first and second, consider occurrences in some text of the
form "first second third", where second comes immediately after first, and
third comes immediately after second.

Return an array of all the words third for each occurrence of "first second
third".
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res, lst = [], text.split()
        for i in range(len(lst)-2):
            if lst[i] == first and lst[i + 1] == second:
                res.append(lst[i + 2])
        return res
