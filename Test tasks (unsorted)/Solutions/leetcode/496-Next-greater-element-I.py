"""
https://leetcode.com/problems/next-greater-element-i/

Category - Easy

The next greater element of some element x in an array is the first greater
element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where
nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] ==
nums2[j] and determine the next greater element of nums2[j] in nums2. If
there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next
greater element as described above.
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, d, stack = [], {}, []
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                d[stack.pop()] = num2          
            stack.append(num2)
        for num1 in nums1:                        
            res.append(d.get(num1, -1))         
        return res
        