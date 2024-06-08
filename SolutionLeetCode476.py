class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        power_of_two = 1

        while num > 0:
            right_most_bit = num & 1
            # If num has a zero at the ith bit, the complement must have a one
            if right_most_bit == 0:
                complement += power_of_two
            # Go to the next bit
            num = num >> 1
            power_of_two *= 2

        return complement
