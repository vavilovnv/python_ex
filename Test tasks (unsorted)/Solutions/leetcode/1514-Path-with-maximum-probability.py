"""
https://leetcode.com/problems/path-with-maximum-probability/

Category - Medium

You are given an undirected weighted graph of n nodes (0-indexed), represented
by an edge list where edges[i] = [a, b] is an undirected edge connecting the
nodes a and b with a probability of success of traversing that edge
succProb[i].

Given two nodes start and end, find the path with the maximum probability of
success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted
if it differs from the correct answer by at most 1e-5.
"""

class Solution:
    def maxProbability(
            self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int
    ) -> float:
        prob_node = [0] * n
        prob_node[start] = 1
        node_paths = defaultdict(list)
        for i, [node, another_node] in enumerate(edges):
            node_paths[node].append((another_node, i))
            node_paths[another_node].append((node, i))
        
        paths = deque([start])
        while paths:
            node = paths.popleft()
            for next_node, prob_i in node_paths[node]:
                if next_node == node:
                    continue
                cost = prob_node[node] * succProb[prob_i]
                if cost > prob_node[next_node]:
                    prob_node[next_node] = cost
                    paths.append(next_node)
        return prob_node[end]
