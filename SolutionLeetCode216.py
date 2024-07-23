from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.combinations = []
        self.k = k
        self.n = n
        # If the target sum is out of this interval, no combination will be valid
        if self.get_smallest_sum(k) <= self.n <= self.get_largest_sum(k):
            self.get_combinations([], 0)

        return self.combinations

    def get_smallest_sum(self, k):
        smallest_sum = 0
        # The smallest sum is obtained by summing up [1, 2, ..., k]
        for i in range(1, k):
            smallest_sum += i

        return smallest_sum

    def get_largest_sum(self, k):
        greatest_sum = 0
        # The largest sum is obtained by summing up [10 - k, 9 - k, ..., 9]
        for i in range(10 - k, 10):
            greatest_sum += i

        return greatest_sum

    # Time complexity: O(k)
    # Space complexity: O(k) otherwise due to the recursion stack (not considering the space needed for the output)
    def get_combinations(self, combination, current_sum):
        # If the sum has already been exceeded, there is no point in going on
        if current_sum > self.n:
            return
        # When we've added k values, check if the target value is obtained from the sum
        if len(combination) == self.k:
            if current_sum == self.n:
                self.combinations.append(combination)
            return

        for i in range(1, 10):
            # We only add values greater than the lastly added value
            if (len(combination) == 0) or (i > combination[-1]):
                self.get_combinations(combination + [i], current_sum + i)
