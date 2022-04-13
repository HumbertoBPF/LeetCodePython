from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        # Hash Table to indicate if a given number was already used for the permutation that is being built
        nums_available = {}
        for num in nums:
            nums_available[num] = True
        return self.get_permutation(nums, nums_available, [], [])

    def get_permutation(self, nums, nums_available, permutation, permutations):
        # If the current permutation has the same number of items as the input list, we have used all the items and then
        # we add it to the list of permutations
        if len(permutation) == len(nums):
            permutations.append(permutation)
            return permutations

        for num in nums:
            # If the current number is still available
            if nums_available[num]:
                # Mark it as not available and add it to the permutation array
                nums_available[num] = False
                self.get_permutation(nums, nums_available, permutation+[num], permutations)
                # When we return from the recursion call, make the current number available again
                nums_available[num] = True

        return permutations


o1 = Solution()
print(o1.permute([1]))
