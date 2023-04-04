"""
https://leetcode.com/problems/rotting-oranges/

Category - Medium

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a
fresh orange. If this is impossible, return -1.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res, fresh, rotten = 0, set(), deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        while fresh and rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft() 
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in fresh:
                        fresh.remove(coord)
                        rotten.append(coord)
            res += 1
        return res if not fresh else -1

"""
hint
use set for fresh oranges and queue for rotten, then if there are fresh
oranges next to the rotten ones, remove them from the fresh ones and add them
to the rotten ones
"""
