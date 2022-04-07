from typing import List


class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = n - 3
        # Go from the right to the left with a sliding window of 3 elements checking if the three items of the sliding
        # window form a triangle
        while i >= 0:
            if nums[i+2] - nums[i+1] < nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
            i -= 1

        return 0


o1 = Solution()
print(o1.largestPerimeter([2, 1, 2]))
