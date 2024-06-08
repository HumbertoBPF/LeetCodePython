from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lower_bound = 0
        upper_bound = n - 1
        # Checking if the list is not rotated
        if nums[lower_bound] < nums[upper_bound]:
            return nums[lower_bound]

        while upper_bound - lower_bound > 1:
            mid = (lower_bound + upper_bound) // 2

            if nums[mid] < nums[upper_bound]:
                upper_bound = mid
                continue

            if nums[mid] > nums[upper_bound]:
                lower_bound = mid

        return nums[upper_bound]

# nums = [3,4,5,1,2]
# lower_bound = 0
# upper_bound = 4
# mid = (lower_bound + upper_bound) // 2 = 2
# nums[mid] = nums[2] = 5 > nums[4] = 2 => lower_bound = 2
# lower_bound = 2
# upper_bound = 4
# mid = (2 + 4) // 2 = 3
# nums[mid] = nums[3] = 1 < nums[4] = 2 => upper_bound = 3
# lower_bound = 2
# upper_bound = 3
# STOP
