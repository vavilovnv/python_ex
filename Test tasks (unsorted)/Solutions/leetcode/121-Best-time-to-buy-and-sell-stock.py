"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Category - Easy

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i - 1])
            profit = max(profit, prices[i] - min_price)
        return profit
