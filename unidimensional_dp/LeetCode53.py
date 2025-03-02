from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        local_max = nums[0]
        global_max = local_max

        for i in range(1, n):
            local_max = max(nums[i], local_max + nums[i])
            global_max = max(global_max, local_max)

        return global_max
