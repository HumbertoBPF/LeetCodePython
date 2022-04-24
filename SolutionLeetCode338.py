class Solution(object):
    """
    :type n: int
    :rtype: List[int]
    """
    # Solution O(n log n)
    def countBits(self, n):
        ones_count_list = [0]

        for i in range(1, n+1):
            ones_count = 1
            remainder = i % 2
            quotient = i // 2
            # Compute the number of ones of the binary equivalent of "i" by dividing i by 2 progressively
            while quotient != 0:
                if remainder == 1:
                    ones_count += 1

                remainder = quotient % 2
                quotient = quotient // 2

            ones_count_list.append(ones_count)

        return ones_count_list

    # Solution O(n)
    def countBitsDP(self, n):
        if n == 0:
            return [0]
        # The item at the ith position corresponds to the number of ones of the binary equivalent of i
        ones_count = [0, 1]
        # The item at the ith position corresponds to the number of ones at the end of the binary equivalent of i
        ones_at_end = [0, 1]
        # Last power of two whose number of ones was counted
        last_power_two = 0
        # Last power of two to have the number of ones counted
        next_power_two = 2

        for i in range(2, n+1):
            # When a power of two is reached, update last_power_two and next_power_two
            if i == next_power_two:
                last_power_two = next_power_two
                next_power_two *= 2
            # The number of ones of an odd number is always the number of zeros of its predecessor plus 1 since we just
            # have to replace the 0 at the end with a 1
            if i % 2 != 0:
                ones_count.append(ones_count[-1] + 1)
            # If "i" is even, we have to verify the length of the sequence of ones at the end of its predecessor. For example
            # if i = 12, its predecessor is 11, whose binary equivalent has a sequence of two ones at the end(1011)
            else:
                # When we add a one to a binary sequence of ones, all the ones of the sequence become 0 and 1 bit is put
                # at the bit right before the sequence (example: 1011 + 1 = 1100). Hence, we subtract all the 1s of the sequence
                # of ones and add a new 1
                ones_count.append(ones_count[-1] + 1 - ones_at_end[-1])
            # The number of ones at the end of the binary equivalent of "i" is the same as "i-last_power_two" except for when
            # the binary equivalent of "i-last_power_two" is composed only of ones. For this exceptional case, we have an additional
            # one correspondent to the left most one of "i"
            if (i - last_power_two) == (last_power_two - 1):
                ones_at_end.append(ones_at_end[i - last_power_two] + 1)
            else:
                ones_at_end.append(ones_at_end[i - last_power_two])

        return ones_count


o1 = Solution()
for n in range(0, 10):
    print(o1.countBitsDP(n) == o1.countBits(n))
