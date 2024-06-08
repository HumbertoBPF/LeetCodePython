import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {}
        # If the amount is zero, then we don't need any coin to reach it
        if amount == 0:
            return 0
        memory[0] = 0

        for coin in coins:
            # If the amount is equal to a coin that we have, we just need one coin
            memory[coin] = 1
        # Trying to break the problem into smaller problems by subtracting the values of the coins we have
        for i in range(1, amount + 1):
            smallest_number_coins = sys.maxsize

            for coin in coins:
                sub_amount = i - coin

                if sub_amount in memory:
                    number_coins = 1 + memory[sub_amount]
                    if number_coins < smallest_number_coins:
                        smallest_number_coins = number_coins
            # Among the solutions for the sub amount (amount - value of the coin), we pick the smallest one
            if smallest_number_coins != sys.maxsize:
                memory[i] = smallest_number_coins

        return memory.get(amount, -1)


solution = Solution()
coins = [186,419,83,408]
print(solution.coinChange(coins, 6249))