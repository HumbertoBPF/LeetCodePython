class Solution:
    # Time complexity: O(1) because the number of bits is a bounded value
    # Space complexity: O(1)
    def minFlips(self, a: int, b: int, c: int) -> int:
        current_result = a | b
        number_flips = 0

        while c > 0 or current_result > 0:
            c_last_bit = c % 2
            current_result_last_bit = current_result % 2

            if c_last_bit != current_result_last_bit:
                # If we need a 1, but we got a 0, then one flip is needed for this position
                if (c_last_bit == 1) and (current_result_last_bit == 0):
                    number_flips += 1
                # If we need a 0, but we got a 1, then the number of flips needed for this position is equal to the
                # number of ones
                else:
                    a_last_bit = a % 2
                    b_last_bit = b % 2
                    number_flips += a_last_bit + b_last_bit
            # Go to the next bit
            a = a >> 1
            b = b >> 1
            c = c >> 1
            current_result = current_result >> 1

        return number_flips
