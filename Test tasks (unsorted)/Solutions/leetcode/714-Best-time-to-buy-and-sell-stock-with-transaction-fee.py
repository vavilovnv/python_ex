"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Category - Medium

You are given an array prices where prices[i] is the price of a given stock on
the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions
as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must
sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float("-inf"), 0
        for price in prices:
            next_buy = max(buy, sell - price)
            next_sell = max(sell, buy + price - fee)
            buy, sell = next_buy, next_sell
        return sell
