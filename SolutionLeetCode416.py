class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0

        while x != 0 or y != 0:
            # When the ith bits of x and y match, the ith bit of x XOR y will be 0
            # The "AND 1" part takes a snapshot of the right most bit
            right_most_bits_match = (x ^ y) & 1 == 0
            if not right_most_bits_match:
                hamming_distance += 1
            x = x >> 1
            y = y >> 1

        return hamming_distance
