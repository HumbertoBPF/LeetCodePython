from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        We iterate over the input list while keeping a sliding window ending at the current index and beginning at a
        start index that we must track.
        """
        n = len(nums)
        # Track the beginning of the sliding window of zeroes
        start_index = 0

        for i in range(n):
            num = nums[i]
            # When finding an item different from zero, we place it at the beginning of the sliding window, and we update
            # the start index (since the sequence of consecutive zeroes starts now at start_index + 1)
            if num != 0:
                tmp = nums[i]
                nums[i] = nums[start_index]
                nums[start_index] = tmp
                start_index += 1
