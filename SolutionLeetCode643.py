from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        sliding_window_sum = 0

        for i in range(k):
            sliding_window_sum += nums[i]
        # We need to find the sliding window with the greatest sum
        maximum_sum = sliding_window_sum

        for i in range(k, n):
            # Pop the first item of the sliding window
            sliding_window_sum -= nums[i - k]
            # Add an item to the end of the sliding window
            sliding_window_sum += nums[i]
            maximum_sum = max(maximum_sum, sliding_window_sum)
        # Compute the maximum average
        return maximum_sum/k
