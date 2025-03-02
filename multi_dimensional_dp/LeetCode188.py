from typing import List


class Solution:
    # Time complexity: O(n*k)
    # Space complexity: O(n*k)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.prices = prices
        self.n = len(prices)
        self.k = k
        self.cache = [[None]*(2*k) for _ in range(self.n)]
        return self.dfs(0, True, 0)

    def get_column_index(self, buying: bool, completed_transactions: int) -> int:
        return int(buying) * self.k + completed_transactions

    def dfs(self, day: int, buying: bool, completed_transactions: int):
        if (day == self.n) or (completed_transactions == self.k):
            return 0

        if self.cache[day][self.get_column_index(buying, completed_transactions)] is not None:
            return self.cache[day][self.get_column_index(buying, completed_transactions)]

        max_profit = self.dfs(day + 1, buying, completed_transactions)

        if buying:
            max_profit = max(max_profit, self.dfs(day + 1, not buying, completed_transactions) - self.prices[day])
        else:
            max_profit = max(max_profit, self.dfs(day + 1, not buying, completed_transactions + 1) + self.prices[day])

        self.cache[day][self.get_column_index(buying, completed_transactions)] = max_profit
        return max_profit
