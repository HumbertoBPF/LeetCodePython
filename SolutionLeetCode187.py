from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        # If the DNA sequence is not longer than 10, it's impossible that a 10-letter-long sequence appears more
        # than once
        if n <= 10:
            return []

        frequency_of_sequences = {}
        # O(n)
        for i in range(0, n - 9):
            # Take the 10-letter-long sequence starting at the current index (0(10) = O(1))
            sequence = s[i:i + 10]
            # Update the number of times it has been seen
            if sequence not in frequency_of_sequences:
                frequency_of_sequences[sequence] = 0

            frequency_of_sequences[sequence] += 1

        repeated_sequences = []
        # We are interested in the sequences that have been seen more than once
        # O(n)
        for sequence in frequency_of_sequences:
            if frequency_of_sequences[sequence] > 1:
                repeated_sequences.append(sequence)

        return repeated_sequences
