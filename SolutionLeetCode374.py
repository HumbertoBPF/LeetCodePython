import random

N = 1000
random_number = random.randint(1, N)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num < random_number:
        return -1

    if num == random_number:
        return 0

    return 1


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def guessNumber(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n

        if guess(lower_bound) == 0:
            return lower_bound

        if guess(upper_bound) == 0:
            return upper_bound

        while upper_bound - lower_bound > 1:
            mid = (upper_bound + lower_bound) // 2

            guess_result = guess(mid)
            # For such a case, the target number is mid
            if guess_result == 0:
                return mid
            # For such a case, the target number is lower than mid
            if guess_result == -1:
                upper_bound = mid
                continue
            # If this line is reached, guess_result = 1. For such a case, the target number is greater than mid.
            lower_bound = mid
        # This line should never be reached
        return -1
