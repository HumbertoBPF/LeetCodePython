import math
from typing import List


class Solution:
    def condition(self, k, piles, h):
        needed_hours = 0

        for pile in piles:
            needed_hours += math.ceil(pile/k)

            if needed_hours > h:
                return False

        return True

    # Complexity is O(n*log(h))
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total_bananas = 0
        tallest_pile = piles[0]

        for pile in piles:
            total_bananas += pile

            if pile > tallest_pile:
                tallest_pile = pile
        # Search space = [lower_bound, upper_bound]
        # Lower bound corresponds to divide evenly the number of bananas by the number of hours
        lower_bound = math.ceil(total_bananas/h)
        # Upper bound corresponds to setting all piles' number of bananas to the highest one
        # We do a math.ceil because we can't split an hour in multiple piles
        upper_bound = tallest_pile * math.ceil(n/h)

        while upper_bound - lower_bound > 1:
            mid = (upper_bound + lower_bound) // 2

            if self.condition(mid, piles, h):
                upper_bound = mid
                continue

            lower_bound = mid
        # There is a possibility that both lower and upper bounds fulfill the condition at the end (when all the search
        # space fulfills it), so we return the lowest value between both
        if self.condition(lower_bound, piles, h):
            return lower_bound

        return upper_bound


solution = Solution()
print(solution.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
print(solution.minEatingSpeed(piles = [1000000000], h = 2))
