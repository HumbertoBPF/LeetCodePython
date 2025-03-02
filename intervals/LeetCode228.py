from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) if the output is taken into account, otherwise O(1)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n == 0:
            return []

        if n == 1:
            return [str(nums[0])]

        ranges = []

        lower = nums[0]

        for i in range(1, n):
            # Continue while the current item is the successor of the previous one
            if nums[i] == nums[i - 1] + 1:
                continue
            # If a discontinuity is found, it's time to append the output list
            if nums[i - 1] == lower:
                ranges.append(str(lower))
            else:
                ranges.append(f"{lower}->{nums[i - 1]}")

            lower = nums[i]
        # Appending the interval containing the last item of the input array
        if nums[n - 1] == lower:
            ranges.append(str(lower))
        else:
            ranges.append(f"{lower}->{nums[n - 1]}")

        return ranges
