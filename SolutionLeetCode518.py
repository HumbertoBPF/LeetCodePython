from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        return self.sub_problem(amount, n, coins, {})

    def sub_problem(self, amount, n, coins, memory):
        if (amount, n) in memory:
            return memory[(amount, n)]

        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if n == 1:
            return int(amount % coins[0] == 0)

        acc = 0

        for i in range(n):
            coin = coins[i]
            sub_problem = self.sub_problem(amount - coin, i + 1, coins, memory)
            acc += sub_problem

        memory[(amount, n)] = acc
        return acc


solution = Solution()
amount = 500
coins = [1, 2, 5]
print(solution.change(amount, coins))
