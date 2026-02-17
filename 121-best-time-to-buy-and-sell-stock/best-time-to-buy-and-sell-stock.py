class Solution(object):
    def maxProfit(self, prices):
        buy_price = prices[0]
        profits = 0
        for i in prices[1:]:
            if buy_price>i:
                buy_price = i

            profits = max(profits,i-buy_price)
        return profits
        
           
        
        
        
       