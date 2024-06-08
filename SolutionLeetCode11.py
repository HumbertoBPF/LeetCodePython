from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        if n == 2:
            return min(height[0],height[1])

        max_amount_water = 0
        p1 = 0
        p2 = n - 1

        while p2 - p1 > 0:
            amount_water = (p2 - p1) * min(height[p2], height[p1])

            if amount_water > max_amount_water:
                max_amount_water = amount_water

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_amount_water
