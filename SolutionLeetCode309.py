from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memory = []

        for i in range(n):
            memory.append([None] * 2)
        # We have two choices in the first day
        return max(
            # Start buying
            -prices[0] + self.dfs(0, True, prices, memory),
            # Start with cooldown
            self.dfs(1, False, prices, memory)
        )

    def dfs(self, day, just_bought, prices, memory):
        n = len(prices)

        if day > n - 1:
            return 0

        if memory[day][int(just_bought)] is not None:
            return memory[day][int(just_bought)]
        # You always can choose to cooldown
        profit_cooldown = self.dfs(day + 1, just_bought, prices, memory)

        max_profit = profit_cooldown
        # If you just bought, you can't buy again
        if just_bought:
            # After selling, you have an enforced cooldown, so we skip one day
            profit_sell = prices[day] + self.dfs(day + 2, False, prices, memory)
            # Take the decision that maximizes your profit
            max_profit = max(max_profit, profit_sell)
        # If you didn't buy, you can buy again
        else:
            profit_buy = - prices[day] + self.dfs(day + 1, True, prices, memory)
            # Take the decision that maximizes your profit
            max_profit = max(max_profit, profit_buy)

        memory[day][int(just_bought)] = max_profit
        return max_profit