class Solution(object):
    """
    :type prices: List[int]
    :rtype: int
    """
    def maxProfit(self, prices):
        n = len(prices)

        buy_index = 0
        sell_index = 0
        best_profit = 0

        for i in range(1, n):
            # If we find a better buy price, we pick it as buy price. We have to set it as sell price either since
            # we cannot sell before buying
            if prices[i] < prices[buy_index]:
                buy_index = i
                sell_index = i
            # If we find a better sell price, we pick it as sell price.
            elif prices[i] > prices[sell_index]:
                sell_index = i
            # Check if we got a better profit
            if prices[sell_index] - prices[buy_index] > best_profit:
                best_profit = prices[sell_index] - prices[buy_index]

        return best_profit


o1 = Solution()
print(o1.maxProfit([6,7,1,5,3,4,6]))
