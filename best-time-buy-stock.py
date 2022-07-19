class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price = prices[0]
        profit = -1

        for current_price in prices:
            price = min(price, current_price)
            current_profit = current_price - price
            profit = max(profit, current_profit)

        return profit
