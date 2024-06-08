from typing import List


class SolutionArithmeticProgression:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        # For an arithmetic progression: an = a0 + n*r
        # Sn = (n + 1)*a0 + n*(n + 1)/2
        n = len(nums)
        expected_sum = n*(n + 1) // 2
        obtained_sum = 0

        for num in nums:
            obtained_sum += num

        return expected_sum - obtained_sum


class SolutionBitManipulation:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        missing_number = 0
        # XOR operator: let x be a number
        # x XOR 0 = x
        # x XOR x = 0
        # Consider nums = [0, 1, 3]:
        # (0 XOR 0) XOR (1 XOR 1) XOR (2) XOR (3 XOR 3) = 0 XOR 0 XOR 2 XOR 0 = O XOR 2 = 2
        # Hence, we just need to multiply the "complete list" (without any item missing) by the input list (with a
        # missing item). The result will be the missing item.
        for i in range(n):
            missing_number ^= i
            if i != n - 1:
                missing_number ^= nums[i]

        return missing_number
