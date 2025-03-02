from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        values_to_indices = {}

        for i in range(n):
            num = nums[i]

            if num not in values_to_indices:
                values_to_indices[num] = i
                continue

            last_index_of_num = values_to_indices[num]
            # Check if the current index and the last occurrence of num are close enough
            if abs(i - last_index_of_num) <= k:
                return True
            # If the current index and the last index where num was seen are not close enough, replace the last
            # occurrence of num in the hash map
            values_to_indices[num] = i

        return False
