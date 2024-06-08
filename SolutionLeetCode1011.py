import math
from typing import List


class Solution:
    def condition(self, weights, days, capacity):
        needed_days = 1
        transported_weight = 0

        for weight in weights:
            if weight > capacity:
                return False

            transported_weight += weight

            if transported_weight > capacity:
                needed_days += 1
                transported_weight = weight

        return needed_days <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        total_weight = weights[0]
        max_weight = weights[0]

        for i in range(1, n):
            weight_i = weights[i]

            total_weight += weight_i

            if weight_i > max_weight:
                max_weight = weight_i

        lower_bound = math.ceil(total_weight/days)
        upper_bound = max_weight*math.ceil(n/days)

        if self.condition(weights, days, lower_bound):
            return lower_bound

        while upper_bound - lower_bound > 1:
            mid = (upper_bound + lower_bound) // 2

            if self.condition(weights, days, mid):
                upper_bound = mid
            else:
                lower_bound = mid

        return lower_bound + 1


weights = [5,5,5,5,5,5,5,5,5,5]
days = 8
# lower_bound = ceil(8/4) = 2
# upper_bound = ceil(3*5/4) = 4
# search_space = [2, ..., 4]
# lower_bound doesn't solve
# mid = (2 + 4) // 2 = 3
# mid solves the problem => lower_bound = 2, upper_bound = 3
# mid = (11 + 15) // 2 = 13
# mid doesn't solve the problem => lower_bound = mid = 13, upper_bound = 15
# mid = (13 + 15) // 2 = 14
# mid doesn't solve the problem => lower_bound = mid = 14, upper_bound = 15
solution = Solution()
print(solution.shipWithinDays(weights, days))
