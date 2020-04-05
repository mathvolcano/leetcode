"""
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


def maxProfit(prices):
    if len(prices) <= 1: return 0

    best_profit = 0
    min_idx_so_far = 0
    max_idx_after_min = 0

    for i in range(1, len(prices)):
        if prices[i] <= prices[i-1]:
            min_idx_so_far = i
            max_idx_after_min = i
        if prices[i] > prices[max_idx_after_min]:
            best_profit += prices[i] - prices[max_idx_after_min]
            max_idx_after_min = i

    return best_profit


maxProfit([1,2,3,4,5])
maxProfit([7,1,5,3,6,4])
maxProfit([7,6,4,3,1])
