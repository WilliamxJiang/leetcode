# Last updated: 8/9/2025, 2:58:18 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if min_price > price:
                min_price = price
            profit = price - min_price
            if max_profit < profit:
                max_profit = profit
        return max_profit