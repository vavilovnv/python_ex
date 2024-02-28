"""
https://leetcode.com/problems/shuffle-the-array/

Category - Easy

Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst1, lst2, res = nums[:n], nums[n:], []
        m_len = min(len(lst1), len(lst2))
        for i in range(m_len):
            res.append(lst1[i])
            res.append(lst2[i])
        return res + (lst1[m_len:] if m_len == len(lst2) else lst2[m_len:])
