from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = {}

        current_sum = 0

        for num in nums:
            current_sum += num

            if current_sum not in sums:
                sums[current_sum] = 0

            sums[current_sum] += 1
        # At this point, "sums" contains as keys the sum of the sub-arrays containing the item at position 0 and as
        # values their number of occurrences
        nb_sub_arrays_with_sum = sums.get(k, 0)
        accumulated_sum = 0
        # Getting the sum of the sub-arrays starting at position i + 1 corresponds to remove the item at position i
        # from the subarray. Since modifying all the items of the hash map would take additional time, we increment the
        # target sum, which has the same effect
        for i in range(n - 1):
            accumulated_sum += nums[i]
            target_sum = k + accumulated_sum
            # Removing sub-arrays that become empty
            sums[accumulated_sum] -= 1

            if sums[accumulated_sum] == 0:
                del sums[accumulated_sum]

            nb_sub_arrays_with_sum += sums.get(target_sum, 0)

        return nb_sub_arrays_with_sum
