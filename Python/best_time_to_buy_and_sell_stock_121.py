class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # update min buying price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # update max profit
                
        return max_profit
