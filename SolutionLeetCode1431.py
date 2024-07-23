from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) if we consider the space for the output, O(1) otherwise
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum_number_of_candies = float("-inf")
        output = []
        # Iterate once to get the maximum number of candies that a kid has
        for candy in candies:
            maximum_number_of_candies = max(maximum_number_of_candies, candy)
        # Iterate again to compute the output
        for candy in candies:
            output.append((candy + extraCandies) >= maximum_number_of_candies)

        return output
