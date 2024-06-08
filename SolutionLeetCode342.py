class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # A negative number can't be the power of a positive number
        if n < 1:
            return False

        bit_position = 0

        while n > 0:
            # Bit is set
            if n & 1 == 1:
                # Odd bit position
                if bit_position % 2 == 1:
                    return False
                # We must have only one bit set
                if n != 1:
                    return False
            # Check the next bit
            n = n >> 1
            bit_position += 1

        return True


class SolutionWithoutLoopsAndRecursion:
    def isPowerOfFour(self, n: int) -> bool:
        # A negative number can't be the power of a positive number
        if n < 1:
            return False
        has_one_bit_set = n & (n - 1) == 0
        # Mask = ...101010101
        mask = int((4**16-1)/(4 - 1))
        is_bit_set_at_even_position = mask & n != 0
        return has_one_bit_set and is_bit_set_at_even_position
