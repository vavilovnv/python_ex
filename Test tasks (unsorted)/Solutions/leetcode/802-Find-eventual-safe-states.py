"""
https://leetcode.com/problems/find-eventual-safe-states/

Category - Medium

There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge
from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe
node if every possible path starting from that node leads to a terminal node
(or another safe node).

Return an array containing all the safe nodes of the graph. The answer should
be sorted in ascending order.
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def is_safe_node(node: int):
            if statuses[node] == 1:
                return False
            if statuses[node] == 2:
                return True
            statuses[node] = 1
            for outgoing_node in graph[node]:
                if not is_safe_node(outgoing_node):
                    return False
            statuses[node] = 2
            return True

        # 0 - not visited, 1 - visited, 2 - safe
        res, len_g  = [], len(graph) 
        statuses = [0] * len_g
        for i in range(len_g):
            if is_safe_node(i):
                res.append(i)
        return res
