class Solution:
    # Time complexity: O(log left)
    # Space complexity: O(1)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = left

        number_bits_left = self.get_number_bits(left)
        # We don't need to check values greater than 2*number_bits_left + 1, because the left already has the bits
        # after number_bits_left set as 0
        upper_bound = min(2**number_bits_left + 1, right)

        i = left
        exponent = 0
        # We don't need to operate with all the points inside the interval [left, upper_bound]. Instead, we just check
        # the values the closest to "left" that can set te bits of "left" to zero
        while i <= upper_bound:
            result &= i

            if result == 0:
                return result

            i = left + 2**exponent
            exponent += 1
        # We also need to explicitly check the upper bound
        result &= upper_bound

        return result

    def get_number_bits(self, n):
        """
        :param n: number whose binary representation you want to know
        :return: number of bits of the binary representation of n
        """
        number_bits = 0

        while n > 0:
            number_bits += 1
            n = n >> 1

        return number_bits


solution = Solution()
print(solution.rangeBitwiseAnd(1073741824, 2147483647))
