class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_right_most_bit = n & 1

        while True:
            # Go to the next bit
            n = n >> 1

            if n == 0:
                break
            # Snapshot of the rightmost bit
            right_most_bit = n & 1
            # If n has alternating bits, neighbor bits must alternate
            if right_most_bit == last_right_most_bit:
                return False

            last_right_most_bit = right_most_bit

        return True
