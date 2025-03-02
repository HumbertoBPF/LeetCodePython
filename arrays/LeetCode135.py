from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        self.ratings = ratings
        # The number of candies is at least n due to the first constraint (each child must have at least one candy)
        self.candies = [1]*n

        diff = 0
        start = 0

        for i in range(n):
            previous_rating = ratings[i] if (i == 0) else ratings[i - 1]

            previous_diff = diff
            diff = ratings[i] - previous_rating
            # If it is a peak or a valley
            if ((previous_diff > 0) and (diff <= 0)) or ((previous_diff < 0) and (diff >= 0)):
                self.solve(start, i - 1)
                start = i - 1
        # Solving a potential last interval
        self.solve(start, n - 1)

        return sum(self.candies)

    def solve(self, lower, upper):
        # Increasing interval
        if self.ratings[lower] < self.ratings[upper]:
            self.solve_increasing_interval(lower, upper)

        # Decreasing interval
        if self.ratings[lower] > self.ratings[upper]:
            self.solve_decreasing_interval(lower, upper)

    def solve_decreasing_interval(self, lower, upper):
        current = upper - 1
        while current >= lower:
            if self.ratings[current] > self.ratings[current + 1]:
                next_nb_candies = self.candies[current + 1]
                self.candies[current] = max(self.candies[current], next_nb_candies + 1)
            current -= 1

    def solve_increasing_interval(self, lower, upper):
        current = lower + 1
        while current <= upper:
            if self.ratings[current - 1] < self.ratings[current]:
                previous_nb_candies = self.candies[current - 1]
                self.candies[current] = max(self.candies[current], previous_nb_candies + 1)
            current += 1
