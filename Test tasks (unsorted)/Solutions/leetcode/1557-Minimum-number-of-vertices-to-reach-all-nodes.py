"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

Category - Medium

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an
array edges where edges[i] = [fromi, toi] represents a directed edge from node
fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are
reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""

# TC: O(n) SC: O(n)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s1, s2 = set(), set()
        for i in edges:
            s1.add(i[0])
            s2.add(i[1])
        return list(s1 - s2)
