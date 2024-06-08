from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge case: if there is only one house, pick it
        if n == 1:
            return nums[0]

        cache = {}
        # Since there is no valid solution with both items at the extremities, solve for the subsets without the last
        # item and without the first one, and take the maximum value
        return max(
            self.sub_problem(0, n - 2, nums, cache),
            self.sub_problem(1, n - 1, nums, cache)
        )

    def sub_problem(self, start, end, nums, cache):
        """
        Solves the problem for the houses between the start and the end index (both bounds included). This code is
        adapted from LeetCode problem 198 with the difference that we accept an initial index different from 0.
        :param start: start index
        :param end: end index
        :param nums: input list containing the houses and their associated amount of money
        :param cache: dictionary for memoization
        :return: maximum value that the robber can get
        """
        if (start, end) in cache:
            return cache[(start, end)]

        if end - start == 0:
            answer = nums[start]
        elif end - start == 1:
            answer = max(nums[start], nums[end])
        else:
            answer = max(
                self.sub_problem(start, end - 2, nums, cache) + nums[end],
                self.sub_problem(start, end - 1, nums, cache)
            )

        cache[(start, end)] = answer
        return answer
