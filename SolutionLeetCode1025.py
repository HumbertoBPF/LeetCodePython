import math


class Solution(object):
    """
    :type n: int
    :rtype: bool
    """
    def divisorGame(self, n):
        player_wins_with_number = {1: False, 2: True, 3: False}         # Base cases
        self.game_turn(n, player_wins_with_number)
        return player_wins_with_number[n]

    def game_turn(self, n, player_wins_with_number):
        player_wins_with_number[n] = False

        for i in range(1, math.floor(n/2)+1):
            if n % i == 0:
                # If we have not computed what happen when a player picks n-i, compute it
                if player_wins_with_number.get(n - i) is None:
                    self.game_turn(n - i, player_wins_with_number)
                # If at least one of the next possible choices results in a defeat of the other player, this player wins
                if not player_wins_with_number[n - i]:
                    player_wins_with_number[n] = True
                    break


o1 = Solution()
print(o1.divisorGame(3))
