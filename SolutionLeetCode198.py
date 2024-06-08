from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        # Trivial cases:
        # - n = 1 -> just pick the unique element available
        # - n = 2 -> pick the largest element
        return self.sub_problem(n, nums, { 1: nums[0], 2: max(nums[0], nums[1]) })

    def sub_problem(self, n, nums, cache):
        if n in cache:
            return cache[n]
        # P(n) = max(P(n - 2) + nums[n - 1], P(n - 1))
        # To prove the validity of the expression above, we distinguish two cases:
        # - P(n - 1) lets you pick nums[n - 1]. For that case, P(n - 1) doesn't include nums[n - 2], so
        # P(n - 2) = P(n - 1) and the expression holds.
        # - P(n - 1) doesn't let you pick nums[n - 1]. It happens when this solution includes nums[n - 2]. For such a
        # case, we need to compare the largest solution without this element + nums[n - 1] with P(n - 1) to see which
        # one is worthier.
        answer = max(self.sub_problem(n - 2, nums, cache) + nums[n-1], self.sub_problem(n - 1, nums, cache))
        cache[n] = answer
        return answer


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
