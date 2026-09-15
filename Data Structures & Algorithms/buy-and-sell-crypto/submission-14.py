class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        temp = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = prices[i] - min_price
            temp = max(temp, max_profit)
        return temp
            
