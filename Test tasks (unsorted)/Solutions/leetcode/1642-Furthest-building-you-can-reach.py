"""
https://leetcode.com/problems/furthest-building-you-can-reach/

Category - Medium

You are given an integer array heights representing the heights of
buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by
possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next
building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you
can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the
given ladders and bricks optimally.
"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        res = []
        heapq.heapify(res)
        builds = len(heights)
        for i in range(builds - 1):
            if heights[i + 1] > heights[i]:
                heapq.heappush(res, heights[i + 1] - heights[i]) 
                if len(res) > ladders: 
                    bricks -= heapq.heappop(res) 
                    if bricks < 0:
                        return i
        return builds - 1
