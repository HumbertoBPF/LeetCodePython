from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]

        current_max = 1
        current_min = 1
        # Example: [-3, 1, -2, -1]
        for num in nums:
            if num == 0:
                # Reset the current max and min to a "neutral value"
                current_max = 1
                current_min = 1
                max_product = max(max_product, 0)
                continue

            current_max *= num
            current_min *= num
            # Current max and min will keep storing the positive and negative product respectively
            # 1st iteration: current_max = 1, current_min = -3
            # 2nd iteration: current_max = 1, current_min = -3
            # 3rd iteration: current_max = 6, current_min = -2
            # 4th iteration: current_max = 2, current_min = -6
            temp = current_max
            current_max = max(num, current_max, current_min,)
            current_min = min(num, temp, current_min)
            # Keep the maximum product updated
            # 1st iteration: max_product = 1
            # 2nd iteration: current_max = 1
            # 3rd iteration: current_max = 6
            # 4th iteration: current_max = 6
            max_product = max(max_product, current_max)

        return max_product



solution = Solution()
nums = [2,3,-2,10,-5,40,-4]
print(solution.maxProduct(nums))
