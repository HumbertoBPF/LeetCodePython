from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # Edge case: if you have only one item in the array, you are already at the last position
        if n == 1:
            return True

        target_index = n - 1

        i = n - 2
        # Trying to arrive to the last item through intermediate positions
        while i >= 0:
            # Can I arrive at target_index through the item at index i?
            is_target_index_reachable_from_i = (target_index - i <= nums[i])

            if is_target_index_reachable_from_i:
                target_index = i

            i -= 1
        # len(path) != 0 → it means we have a path to the last item through intermediate items
        # path[0] != 0 → the path starts at the first position (index 0)
        return target_index == 0


solution = Solution()
nums = [0,2,3]
print(solution.canJump(nums))