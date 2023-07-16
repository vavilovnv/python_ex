"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Category - Hard

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

Find the maximum profit you can achieve. You may complete at most two
transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float("-inf"), float("-inf")
        sell1 = sell2 = 0
        for price in prices:
            next_buy1 = max(buy1, 0 - price)
            next_buy2 = max(buy2, sell1 - price)
            next_sell1 = max(sell1, buy1 + price)
            next_sell2 = max(sell2, buy2 + price)

            buy1, buy2 = next_buy1, next_buy2
            sell1, sell2 = next_sell1, next_sell2
        
        return max(sell1, sell2)
