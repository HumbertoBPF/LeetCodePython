from typing import List


class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # Index of the current minimum of the array
        min_index = 0
        # - 0 > nums[min_index] : when this condition is false, it means that there are no negative numbers in the array
        # anymore and as a consequence we will keep multiplying the same item in the next remaining iterations
        # - k > 0 : condition due to the number of inversions of sign that we can perform
        # - min_index < n : when min_index reaches n, we do not have more items in the array to reverse the sign
        while min_index < n and k > 0 > nums[min_index]:
            nums[min_index] *= -1
            min_index += 1
            k -= 1
        # Case when k is even. If k is 0, we are done. If k is not 0, we are going to reverse the sign of the current
        # minimum of nums an even number of times, which does not change the sum. For both cases, we just return the sum
        if k % 2 == 0:
            return sum(nums)
        # Correction for the case where all the items of the input array had their sign reversed
        if min_index == n:
            min_index = n-1
        # k is odd. So, at the end, the lowest item of the array will have its sign reversed, which makes the sum of the
        # elements to be decreased of twice the value of the minimum
        return sum(nums) - 2*min(nums[min_index], nums[min_index-1])


o1 = Solution()
print(o1.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
