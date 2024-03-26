"""
https://leetcode.com/problems/maximum-units-on-a-truck/

Category - Easy

You are assigned to put some amount of boxes onto one truck. You are given a
2D array boxTypes, where 
boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes
that can be put on the truck. You can choose any boxes to put on the truck as
long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        for boxes in sorted(boxTypes, key=lambda x:x[1], reverse=True):
            if boxes[0] >= truckSize:
                res += boxes[1] * truckSize
                return res
            truckSize -= boxes[0]
            res += boxes[1] * boxes[0]
        return res
