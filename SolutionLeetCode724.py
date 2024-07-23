from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # At the beginning, the right sum is the total sum
        right_sum = 0

        for num in nums:
            right_sum += num
        # At the beginning, the left sum is 0
        left_sum = 0
        # At each iteration, we check if "i" is the pivot index
        for i in range(n):
            num = nums[i]
            # We remove the pivot item from the right sum before checking (it must not be included in the sums)
            right_sum -= num

            if left_sum == right_sum:
                return i
            # We add the pivot item to the left sum after the checking (it must not be included in the sums)
            left_sum += num

        return -1
