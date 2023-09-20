"""
https://leetcode.com/problems/reconstruct-itinerary/

Category - Hard

You are given a list of airline tickets where tickets[i] = [fromi, toi] 
represent the departure and the arrival airports of one flight. 
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the 
itinerary must begin with "JFK". If there are multiple valid itineraries, 
you should return the itinerary that has the smallest lexical order when read
as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than 
["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all
the tickets once and only once.
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res, d = ["JFK"], defaultdict(list)

        def dfs(start):
            if len(res) == len(tickets) + 1:
                return True
            for i, finish in enumerate(d[start][::]):
                d[start].pop(i)
                res.append(finish)
                if dfs(finish):
                    return True
                d[start].insert(i, finish)
                res.pop()
        
        for start, finish in sorted(tickets):
            d[start].append(finish)
        dfs("JFK")
        return res
