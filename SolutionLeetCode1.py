from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        # Easy case
        if length == 2:
            return [0, 1]

        nums_dict = self.get_indices_dict(nums)

        for i in range(length):
            el = nums[i]
            complement = target - el

            complement_indices = nums_dict.get(complement)

            if complement_indices is not None:
                if el == complement:
                    # If the complement is equal to the current element, it needs to happen twice
                    if len(complement_indices) == 2:
                        return complement_indices
                else:
                    return [i, complement_indices[0]]

        return []
    
    def get_indices_dict(self, nums):
        indices_dict = {}

        for i in range(len(nums)):
            el = nums[i]
            if indices_dict.get(el) is None:
                indices_dict[el] = [i]
            else:
                indices_dict[el].append(i)

        return indices_dict
