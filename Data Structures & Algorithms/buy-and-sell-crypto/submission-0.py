class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        max_profit=0
        for price in prices:
            profit=price-minprice
            max_profit=max(profit,max_profit)
            minprice=min(minprice,price)
        return max_profit
        