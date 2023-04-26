"""
https://leetcode.com/problems/sort-the-people/

Category - Easy

You are given an array of strings names, and an array heights that consists of
distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the
ith person.

Return names sorted in descending order by the people's heights.
"""

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted(zip(names, heights), key=lambda x: -x[1])]
