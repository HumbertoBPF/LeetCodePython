from typing import List


class Solution:
    # time complexity: O(n!) (in the worst case, n - i + 1 decisions are possible at the ith call of the recursive function)
    # space complexity: O(n!) (in the worst case, we add n - i + 1 subsets at the ith call of the recursive function)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        frequency_map = self.get_frequency_map(nums)
        self.compute_subsets_containing_subset([], frequency_map, subsets)
        return subsets

    def compute_subsets_containing_subset(self, subset, frequency_map, subsets):
        for chosen_num in frequency_map:
            # Insert numbers in the non-decreasing order to avoid taking into account duplicated subsets
            if len(subset) > 0 and subset[-1] > chosen_num:
                continue

            subsets.append(subset + [chosen_num])
            # Create a copy of the dictionary not to change it during iteration
            copy_frequency_map = frequency_map.copy()

            copy_frequency_map[chosen_num] -= 1

            if copy_frequency_map.get(chosen_num) == 0:
                del copy_frequency_map[chosen_num]

            self.compute_subsets_containing_subset(subset + [chosen_num], copy_frequency_map, subsets)

    def get_frequency_map(self, nums):
        frequency_map = {}

        for num in nums:
            if frequency_map.get(num) is None:
                frequency_map[num] = 0

            frequency_map[num] += 1

        return frequency_map

solution = Solution()
print(solution.subsetsWithDup([0]))