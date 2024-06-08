from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        if n == 2:
            return min(height[0],height[1])

        max_amount_water = 0

        for i in range(n-1):
            for j in range(i+1, n):
                amount_water = min(height[i], height[j])*(j-i)

                if amount_water > max_amount_water:
                    max_amount_water = amount_water

        return max_amount_water
