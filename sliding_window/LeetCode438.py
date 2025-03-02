from typing import List


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(n) considering the output space, O(1) otherwise
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        # Trivial case (s is shorter than p, and consequently it cannot have anagrams of p)
        if m > n:
            return []
        # O(m)
        p_letter_freq = self.get_letter_frequency(p)
        sliding_window_letter_freq = self.get_letter_frequency(s[0:m])

        anagrams_start_indexes = []

        if p_letter_freq == sliding_window_letter_freq:
            anagrams_start_indexes.append(0)
        # O(n)
        for i in range(m, n):
            popped_letter = s[i - m]
            added_letter = s[i]
            # Taking into account the popped letter in the letter frequency hash map
            sliding_window_letter_freq[popped_letter] -= 1

            if sliding_window_letter_freq[popped_letter] == 0:
                del sliding_window_letter_freq[popped_letter]
            # Taking into account the added letter in the letter frequency hash map
            if added_letter not in sliding_window_letter_freq:
                sliding_window_letter_freq[added_letter] = 0

            sliding_window_letter_freq[added_letter] += 1

            if p_letter_freq == sliding_window_letter_freq:
                anagrams_start_indexes.append(i - m + 1)

        return anagrams_start_indexes

    def get_letter_frequency(self, s: str) -> dict:
        n = len(s)

        letter_frequency = {}

        for i in range(n):
            letter = s[i]

            if letter not in letter_frequency:
                letter_frequency[letter] = 0

            letter_frequency[letter] += 1

        return letter_frequency
