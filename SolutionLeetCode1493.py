from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        start = 0
        end = 0

        number_zeroes = 0
        last_zero_index = 0

        longest_subarray_of_ones = 0

        while end < n:
            if nums[end] == 0:
                # When we see the second zero
                if number_zeroes == 1:
                    # Update the maximum based on the number of ones in the sliding window [start, end-1]
                    # (the -1 is due to the zero in it)
                    longest_subarray_of_ones = max(longest_subarray_of_ones, end - start - 1)
                    # Start a new sliding window right after the last zero seen
                    start = last_zero_index + 1
                    number_zeroes = 0
                # Increment the number of zeroes and track its index
                number_zeroes += 1
                last_zero_index = end

            end += 1
        # Last update to take into account the sliding window being built at the end of the while loop
        longest_subarray_of_ones = max(longest_subarray_of_ones, end - start - 1)
        return longest_subarray_of_ones