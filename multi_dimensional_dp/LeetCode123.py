from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.n = len(prices)
        # We need 6 columns to store cached values taking into account the buying state and the number of completed
        # transactions (buying state = two values, number of completed transactions = three values)
        self.cache = [[None]*6 for _ in range(self.n)]
        return self.dfs(0, True, 0)

    def get_column_index(self, buying: bool, completed_transactions: int) -> int:
        return int(buying) * 3 + completed_transactions

    def dfs(self, day: int, buying: bool, completed_transactions: int):
        if (day == self.n) or (completed_transactions == 2):
            return 0
        # Check for cached computations
        if self.cache[day][self.get_column_index(buying, completed_transactions)] is not None:
            return self.cache[day][self.get_column_index(buying, completed_transactions)]
        # Do nothing (increment the day and keep the current state of buying)
        max_profit = self.dfs(day + 1, buying, completed_transactions)
        # Buy
        if buying:
            max_profit = max(max_profit, self.dfs(day + 1, not buying, completed_transactions) - self.prices[day])
        # Sell (we complete a transaction when we sell a stock)
        else:
            max_profit = max(max_profit, self.dfs(day + 1, not buying, completed_transactions + 1) + self.prices[day])
        # Caching the maximum profit that we can make for this function call
        self.cache[day][self.get_column_index(buying, completed_transactions)] = max_profit
        return max_profit
