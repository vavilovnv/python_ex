"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Category - Hard

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k
transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float("-inf") for _ in range(k)]
        sell = [0 for _ in range(k+1)]
        
        for price in prices:
            next_buy = [float("-inf") for _ in range(k)]
            next_sell = [0 for _ in range(k+1)]
            for i in range(k):
                next_buy[i] = max(buy[i], sell[i] - price)
                next_sell[i+1] = max(sell[i+1], buy[i] + price)
            buy, sell = next_buy, next_sell
        
        return max(sell)
