"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Category - Medium

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

Find the maximum profit you can achieve. You may complete as many transactions
as you like (i.e., buy one and sell one share of the stock multiple times)
with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e.,
cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cooldown = float("-inf"), 0, 0
        for price in prices:
            next_buy = max(buy, cooldown - price)
            next_sell = max(sell, buy + price)
            cooldown = max(cooldown, sell)
            buy, sell = next_buy, next_sell
        return sell
