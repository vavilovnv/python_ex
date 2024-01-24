"""
https://leetcode.com/problems/find-the-town-judge/

Category - Easy

In a town, there are n people labeled from 1 to n. There is a rumor that one
of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the
person labeled ai trusts the person labeled bi. If a trust relationship does
not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be
identified, or return -1 otherwise.
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d, v ={}, defaultdict(int)
        for i in trust:
            d[i[0]] = i[1]
            v[i[1]] += 1
        for i in range(1, n+1):
            if d.get(i) is None and v[i] == n-1:
                return i
        return -1
