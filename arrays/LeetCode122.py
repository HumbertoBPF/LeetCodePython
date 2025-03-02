from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfitBottomUpMemoryOptimized(self, prices: List[int]) -> int:
        n = len(prices)

        next_day = [prices[n - 1], 0]

        for i in range(1, n):
            day = n - 1 - i
            current_day = [0, 0]
            # Not buying
            current_day[0] = max(
                # Sell a stock
                next_day[1] + prices[day],
                # Do nothing
                next_day[0]
            )
            # Buying
            current_day[1] = max(
                # Bought a stock
                next_day[0] - prices[day],
                # Do nothing
                next_day[1]
            )

            next_day = current_day

        return next_day[1]

    # Time complexity: O(n)
    # Space complexity: O(n) due to the date structure for tabulation
    def maxProfitBottomUp(self, prices: List[int]) -> int:
        n = len(prices)

        cache = [[0, 0] for _ in range(n)]

        cache[n - 1] = [prices[n - 1], 0]

        for i in range(1, n):
            day = n - 1 - i
            # Not buying
            cache[day][0] = max(
                # Sell a stock
                cache[day + 1][1] + prices[day],
                # Do nothing
                cache[day + 1][0]
            )
            # Buying
            cache[day][1] = max(
                # Bought a stock
                cache[day + 1][0] - prices[day],
                # Do nothing
                cache[day + 1][1]
            )

        return cache[0][1]

    # Time complexity: O(n)
    # Space complexity: O(n) due to the date structure for tabulation/recursion stack
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.n = len(prices)
        self.cache = [[None, None] for _ in range(self.n)]
        return self.trade(0, True)

    def trade(self, day, buy):
        if day == self.n:
            return 0

        if self.cache[day][int(buy)] is not None:
            return self.cache[day][int(buy)]

        if buy:
            self.cache[day][int(buy)] = max(
                # Bought a stock
                self.trade(day + 1, not buy) - self.prices[day],
                # Do nothing
                self.trade(day + 1, buy)
            )
            return self.cache[day][int(buy)]

        self.cache[day][int(buy)] = max(
            # Sell a stock
            self.trade(day + 1, not buy) + self.prices[day],
            # Do nothing
            self.trade(day + 1, buy)
        )
        return self.cache[day][int(buy)]
