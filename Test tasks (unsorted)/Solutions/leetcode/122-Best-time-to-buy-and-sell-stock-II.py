"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Category - Medium

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at
most one share of the stock at any time. However, you can buy it then
immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        return res

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float("-inf"), 0  # in sell we have current balance - that's the point
        for price in prices:
            next_buy = max(buy, sell - price)
            next_sell = max(sell, buy + price)
            buy, sell = next_buy, next_sell
        return sell