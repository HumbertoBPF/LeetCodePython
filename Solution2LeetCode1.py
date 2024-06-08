from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        if length == 2:
            return [0, 1]

        el1, el2 = self.find_indices(sorted(nums), target)

        return self.find_original_indices(nums, el1, el2)


    def find_indices(self, nums, target):
        p1 = 0
        p2 = len(nums) - 1

        while nums[p1] + nums[p2] != target:
            if nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                p1 += 1

        return [nums[p1], nums[p2]]

    def find_original_indices(self, nums, el1, el2):
        original_i1 = None
        original_i2 = None

        for i in range(0, len(nums)):
            if (original_i1 is None) and (nums[i] == el1):
                    original_i1 = i
            elif nums[i] == el2:
                    original_i2 = i

            if original_i1 is not None and original_i2 is not None:
                return [original_i1, original_i2]

        return [original_i1, original_i2]