from collections import deque
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(k) due to the queue
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Queue storing the indices of the zeroes in the sliding window. It should never contain more than k items
        index_of_zeroes = deque()
        i = 0

        while i < n:
            if len(index_of_zeroes) == k:
                break

            if nums[i] == 0:
                index_of_zeroes.append(i)

            i += 1
        # If the number of zeroes in the ist is lower than k, the longest sequence of ones is the list itself
        if len(index_of_zeroes) != k:
            return n

        max_number_ones = 0
        # Start of the sliding window
        start = 0

        while i < n:
            # When finding a zero, the queue will must be updated
            if nums[i] == 0:
                # number of ones = length of the sliding window from start to i - 1 = i - 1 - start + 1 = i - start
                max_number_ones = max(max_number_ones, i - start)
                # Add the current index (newest zero)
                index_of_zeroes.append(i)
                # Remove the index of the zero that was added first to the queue
                first_zero = index_of_zeroes.popleft()
                # The new start index of the sliding window is at the item coming after the removed zero
                # (no matter if a zero or a one)
                start = first_zero + 1
            i += 1
        # Enforce to compute the size of the last sliding window
        max_number_ones = max(max_number_ones, i - start)
        return max_number_ones