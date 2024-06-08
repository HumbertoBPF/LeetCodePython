NUMBER_BITS = 12


class Solution:
    def getSum(self, a: int, b: int) -> int:
        binary_a = self.get_twos_complement(a)
        binary_b = self.get_twos_complement(b)
        binary_sum = self.sum_twos_complement(binary_a, binary_b)
        return self.integer_from_twos_complement(binary_sum)

    def integer_from_twos_complement(self, bits):
        is_negative = bits[0] == 1

        if is_negative:
            self.flip_bits(bits)
            return -self.integer_from_binary(
                self.sum_twos_complement(bits, [0] * (NUMBER_BITS - 1) + [1])
            )

        return self.integer_from_binary(bits)

    def integer_from_binary(self, bits):
        n = len(bits)

        integer = 0
        power_of_two = 1

        for i in range(n):
            bit = bits[n - i - 1]
            if bit == 1:
                integer += power_of_two
            power_of_two *= 2

        return integer

    def sum_twos_complement(self, bits_1, bits_2):
        carry = 0
        bits = [0]*NUMBER_BITS

        for i in range(NUMBER_BITS):
            bit_1 = bits_1[NUMBER_BITS - i - 1]
            bit_2 = bits_2[NUMBER_BITS - i - 1]

            bit_sum = bit_1 + bit_2 + carry
            carry = 0

            if bit_sum > 1:
                carry = 1
                bit_sum = bit_sum % 2

            bits[NUMBER_BITS - i - 1] = bit_sum

        return bits

    def flip_bits(self, bits):
        n = len(bits)

        for i in range(n):
            bits[i] = 1 if bits[i] == 0 else 0

    def get_twos_complement(self, n):
        bits = [0] * NUMBER_BITS

        i = 0
        is_negative = n < 0
        quotient = abs(n)

        while quotient != 0:
            remainder = quotient % 2
            bits[NUMBER_BITS - i - 1] = remainder
            i += 1
            quotient = quotient // 2

        if is_negative:
            self.flip_bits(bits)
            return self.sum_twos_complement(bits, [0] * (NUMBER_BITS - 1) + [1])

        return bits


solution = Solution()
print(solution.getSum(1, 2))
