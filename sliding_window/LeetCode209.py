import sys
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0 if nums[0] < target else 1

        start = 0
        end = 0

        current_sum = nums[0]
        min_len = sys.maxsize

        while start < n:
            # If the current sum is greater than or equal to the target sum, we move the start of the sliding window
            # (remove its first item)
            if current_sum >= target:
                min_len = min(min_len, end - start + 1)
                current_sum -= nums[start]
                start += 1
                continue
            # If the current sum is lower than the target sum, we move the end of the sliding window (add a new item)
            # if we haven't reached the end of the input array
            if end < n - 1:
                end += 1
                current_sum += nums[end]
                continue
            # If we have reached the end of the sliding window, we can only move the start pointer
            current_sum -= nums[start]
            start += 1

        return 0 if min_len == sys.maxsize else min_len