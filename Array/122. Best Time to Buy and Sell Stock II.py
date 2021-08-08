# Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i, price in enumerate(prices):
            if i+1 == len(prices): break
            if prices[i+1]>price:
                profit+= prices[i+1]-price
        return profit

sol = Solution()
max_profit = sol.maxProfit([7,1,5,3,6,4])
print(max_profit)
