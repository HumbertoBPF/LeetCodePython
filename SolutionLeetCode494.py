from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.sub_problem(n, target, nums, {})

    def abs(self, val):
        if val < 0:
            return -val

        return val

    def sub_problem(self, n, target, nums, memory):
        if (n, target) in memory:
            return memory[(n, target)]

        if n == 1:
            return (int(nums[0] == 0) + 1) if (self.abs(nums[0]) == self.abs(target)) else 0

        part_1 = self.sub_problem(n - 1, target - nums[n - 1], nums, memory)
        part_2 = self.sub_problem(n - 1, target + nums[n - 1], nums, memory)
        nb_possibilities = part_1 + part_2

        memory[(n, target)] = nb_possibilities
        return nb_possibilities