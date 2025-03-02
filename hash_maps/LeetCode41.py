from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Notice that the greatest missing positive is n + 1 since we have place for at most n distinct positive
        # numbers.
        #
        # To avoid using extra space, we will use the input itself as a hash set storing whether numbers in the interval
        # [1, n] that have been seen in nums.
        #
        # If a number i from [1, n] is in nums, we will store a negative number at nums[i - 1].
        #
        # Therefore, we have to get rid of the original negative numbers of nums. For that, we replace them with zeroes.
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            # Take the absolute value to address numbers that were originally positive, but whose sign was inverted
            num = abs(nums[i])
            # When a number i in the range [1, num] is in the input, we mark it as seen by inverting the sign of nums[i]
            if 0 < num <= n:
                # If nums[num - 1] contains currently a positive number, we will just invert its sign so that we can
                # check its original value later if needed (that's the purpose of the abs operation above)
                if nums[num - 1] > 0:
                    nums[num - 1] *= -1
                # If nums[num - 1] contains a zero, we will store -num. It ensures that when we arrive at this position
                # we will evaluate the number it maps.
                if nums[num - 1] == 0:
                    nums[num - 1] = -num

        first_missing_positive = 1

        while first_missing_positive <= n:
            # When nums[i] > 0, it means that the number i + 1 has not been seen in the input
            if nums[first_missing_positive - 1] >= 0:
                return first_missing_positive
            first_missing_positive += 1

        return first_missing_positive
