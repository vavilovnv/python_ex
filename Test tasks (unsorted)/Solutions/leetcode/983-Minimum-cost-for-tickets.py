"""
https://leetcode.com/problems/minimum-cost-for-tickets/

Category - Medium

You have planned some train traveling one year in advance. The days of the
year in which you will travel are given as an integer array days. Each day is
an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days:
2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given
list of days.
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        money = [0] * (last_day + 1)
        for i in range(1, last_day + 1):
            if i not in days:
                money[i] = money[i - 1]
            else:
                cost_1 = money[i - 1] + costs[0]
                cost_7 = money[max(0, i - 7)] + costs[1]
                cost_30 = money[max(0, i - 30)] + costs[2]
                money[i] = min(cost_1, cost_7, cost_30)
        return money[last_day]

"""
hint
Create a list of 0 values. Then each travel day we choose the lowest price as
the sum of the previous day + cost1 | the previous 7 days + cost2| the
previous 30 days + cost3 and write to the list.
"""
