from typing import List

class DynamicProgrammingSolutionSpaceOptimized:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Here, we saved some space since we only need to keep a cache for the next day
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        next_day_cache = [max(0, prices[n - 1] - fee), 0]
        # Edge case (if the number of days is one, we can't make some profit since the unique option would be buying
        # the stock)
        if n == 1:
            return 0

        for i in range(1, n - 1):
            price = prices[n - i - 1]
            # If we are not buying (selling), we decide between:
            # - Doing nothing (in the next day, we will be selling again)
            # - Selling (in the next day, we will be buying)
            max_profit_selling = max(next_day_cache[0], price - fee + next_day_cache[1])
            # If we are buying, we decide between:
            # - Doing nothing (in the next day, we will be buying again)
            # - Buying (in the next day, we will be selling)
            max_profit_buying = max(next_day_cache[1], - price + next_day_cache[0])
            next_day_cache = [max_profit_selling, max_profit_buying]
        # In the first day, we can only be buying (to be selling we would need to have a stock bought)
        return max(next_day_cache[1], - prices[0] + next_day_cache[0])


class DynamicProgrammingSolution:
    # Time complexity: O(n)
    # Space complexity: O(n) due to the data structure for memoization
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cache = [[0, 0] for _ in range(n)]
        cache[n - 1] = [max(0, prices[n - 1] - fee), 0]
        # Edge case (if the number of days is one, we can't make some profit since the unique option would be buying
        # the stock)
        if n == 1:
            return 0

        for i in range(1, n - 1):
            price = prices[n - i - 1]
            # If we are not buying (selling), we decide between:
            # - Doing nothing (in the next day, we will be selling again)
            # - Selling (in the next day, we will be buying)
            max_profit_selling = max(cache[n - i][0], price - fee + cache[n - i][1])
            # If we are buying, we decide between:
            # - Doing nothing (in the next day, we will be buying again)
            # - Buying (in the next day, we will be selling)
            max_profit_buying = max(cache[n - i][1], - price + cache[n - i][0])
            cache[n - 1 - i] = [max_profit_selling, max_profit_buying]
        # In the first day, we can only be buying (to be selling we would need to have a stock bought)
        cache[0][1] = max(cache[1][1], - prices[0] + cache[1][0])

        return cache[0][1]


class BruteForceSolution:
    # Time complexity: O(2^n)
    # Space complexity: O(n) due to the recursion stack
    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.prices = prices
        self.fee = fee
        self.max_profit = 0
        self.dfs(0, 0, True)
        return self.max_profit

    def dfs(self, money, day, buying):
        if day == len(self.prices):
            self.max_profit = max(self.max_profit, money)
            return

        if buying:
            self.dfs(money - self.prices[day], day + 1, False)
        else:
            self.dfs(money + self.prices[day] - self.fee, day + 1, True)

        self.dfs(money, day + 1, buying)
