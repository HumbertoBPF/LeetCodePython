from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        counter = 0

        left_pointer = 0
        right_pointer = n - 1

        while left_pointer < right_pointer:
            left_item = nums[left_pointer]
            right_item = nums[right_pointer]
            # Two pointers technique (refer to two sum problem)
            current_sum = left_item + right_item
            # Move the right pointer to increase the sum
            if current_sum > k:
                right_pointer -= 1
                continue
            # Move the left pointer to decrease the sum
            if current_sum < k:
                left_pointer += 1
                continue
            # Here, we consider that we performed an operation
            counter += 1
            right_pointer -= 1
            left_pointer += 1

        return counter
