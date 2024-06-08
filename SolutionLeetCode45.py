from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge case: you are already at the last position
        if n == 1:
            return 0

        target_index = n - 1
        path = {}
        i = n - 2
        # Iterate over the list in the reverse order
        while i >= 0:
            # Give the largest jump that you can
            while nums[i] >= target_index - i:
                path[i] = target_index

                if target_index not in path:
                    break

                target_index = path[target_index]

            if i in path:
                target_index = i

            i -= 1
        # Counting the minimum number of jumps needed to arrive at the last position
        nb_jumps = 0
        current_position = 0

        while current_position != n - 1:
            nb_jumps += 1
            current_position = path[current_position]

        return nb_jumps


nums = [2,3,0,1,4]
solution = Solution()
print(solution.jump(nums))
