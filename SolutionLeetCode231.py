class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Negative numbers can't be a power of a positive number
        if n <= 0:
            return False

        shifted_value = n

        for i in range(32):
            if shifted_value == 1:
                return True
            # Having an odd number different from one means to have at least two bits 1 in the binary form
            if shifted_value % 2 == 1:
                return False

            shifted_value = shifted_value >> 1

        return False

class SolutionWithoutLoops:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0
