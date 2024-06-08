from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left_products = [1] * n
        right_products = [1] * n

        for i in range(1, n):
            # Product of the items on the left of the ith element
            left_products[i] = nums[i - 1] * left_products[i - 1]
            # Product of the items on the right of the ith element
            right_products[n - i - 1] = nums[n - i] * right_products[n - i]

        for i in range(n):
            # Take the product of the items on the left and the items on the right
            nums[i] = left_products[i] * right_products[i]

        return nums


class ImprovedSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = []
        left_product = 1
        # Compute first the left-hand products and store them in the output array
        for i in range(n):
            output.append(left_product)
            left_product *= nums[i]

        right_product = 1
        # Then compute the right-hand products and multiply the items of the output array by them
        for i in range(n):
            output[n - i - 1] *= right_product
            right_product *= nums[n - i - 1]

        return output


solution = ImprovedSolution()
print(solution.productExceptSelf([2, 1, 2, 3, 4, 5]))
