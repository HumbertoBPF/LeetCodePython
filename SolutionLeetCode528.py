import random
from typing import List


# Space complexity: O(n)
class Solution:
    # Time complexity: O(n)
    def __init__(self, w: List[int]):
        self.limits = []
        self.sum_weights = 0

        for weight in w:
            self.limits.append(self.sum_weights)
            self.sum_weights += weight

        self.limits.append(self.sum_weights - 1)
    # Time complexity: O(log n)
    def pickIndex(self) -> int:
        n = len(self.limits)

        if n == 2:
            return 0

        # Generate a random number (uniform distribution)
        random_number = random.randint(0, self.sum_weights - 1)
        # Check where is it in the interval using binary search
        if n == 3:
            return 0 if random_number < self.limits[1] else 1

        lower = 0
        upper = n - 1

        while upper - lower > 1:
            mid = (upper + lower) // 2

            if self.limits[mid] < random_number:
                lower = mid
                continue

            if self.limits[mid] > random_number:
                upper = mid
                continue

            if self.limits[mid] == random_number:
                return mid

        return lower


w = [188,927,949,95,151,659,405,906,481,363,728,839]
solution = Solution(w)
for i in range(len(w)):
    weight = w[i]
    print("Should yield", i)
    for j in range(weight):
        print(solution.pickIndex())
