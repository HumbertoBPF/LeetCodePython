from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = {}
        # Use hash map to compute the frequencies
        for num in arr:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        # Use hash set to check if the number of occurrences of multiple items is the same
        num_occurrences = set()

        for key in frequencies:
            value = frequencies[key]
            # Return false if the number of occurrences has already been seen
            if value in num_occurrences:
                return False

            num_occurrences.add(value)

        return True
