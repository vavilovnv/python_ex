"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Category - Easy

Given an array arr, replace every element in that array with the greatest
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > mx:
                arr[i], mx = mx, arr[i]
            else:
                arr[i] = mx
        arr[-1] = -1
        return arr
            