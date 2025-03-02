from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0

        for num in nums:
            x2 ^= (num & x1)
            x1 ^= num

            mask = ~(x1 & x2)

            x2 &= mask
            x1 &= mask

        return x1
