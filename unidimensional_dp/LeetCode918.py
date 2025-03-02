from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = sum(nums)
        # Solving the classic problem (contiguous subarray in the middle)
        local_max_subarray_in_the_middle = nums[0]
        global_max = local_max_subarray_in_the_middle

        for i in range(1, n):
            local_max_subarray_in_the_middle = max(nums[i], local_max_subarray_in_the_middle + nums[i])
            global_max = max(local_max_subarray_in_the_middle, global_max)
        # Solving the problem for split sub arrays (complete array with a hole in the middle)
        local_max_split_subarray = total_sum

        for i in range(1, n - 1):
            local_max_split_subarray = max(total_sum - nums[i], local_max_split_subarray - nums[i])
            global_max = max(local_max_split_subarray, global_max)

        return global_max
