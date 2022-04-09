from collections import deque
from typing import List


class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        return self.compute_xor_subset(0, deque(nums), 0)

    def compute_xor_subset(self, xor_previous_subset, stack, xor_sum):
        # Compute the XOR between the previous XOR and each one of the items of the input stack
        while len(stack) != 0:
            current_number = stack.pop()
            # Compute XOR between the previously computed XOR and the current item of the stack
            xor_current_subset = xor_previous_subset ^ current_number
            # Add the XOR computed at this iteration to the sum
            xor_sum += xor_current_subset
            # Computes the XOR sum of the subsets containing the subset corresponding to xor_current_subset and add them
            # to the total XOR sum
            xor_sum = self.compute_xor_subset(xor_current_subset, stack.copy(), xor_sum)

        return xor_sum


o1 = Solution()
print(o1.subsetXORSum([1, 3]))
