import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        min_start = 0
        min_end = sys.maxsize

        start = 0
        end = 0

        frequency_letters = self.get_letter_frequencies(t)

        if s[0] in frequency_letters:
            frequency_letters[s[0]] -= 1

        has_all_letters = self.sliding_window_has_all_letters(frequency_letters)

        if has_all_letters and (end - start < min_end - min_start):
                min_start = start
                min_end = end

        while start < n - 1:
            # If the current sliding window contains all the letters of t or if we can't expand the window anymore,
            # shrink it
            if (end >= n - 1) or has_all_letters:
                start += 1
                removed_letter = s[start - 1]

                if removed_letter in frequency_letters:
                    frequency_letters[removed_letter] += 1
            # If there is some letter of t that is not in the window, expand it
            else:
                end += 1
                added_letter = s[end]

                if added_letter in frequency_letters:
                    frequency_letters[added_letter] -= 1

            has_all_letters = self.sliding_window_has_all_letters(frequency_letters)
            # If the current sliding window contains all the letters from t, update the optimal start and end pointers
            if has_all_letters and (end - start < min_end - min_start):
                min_start = start
                min_end = end

        return "" if (min_end == sys.maxsize) else s[min_start:min_end + 1]

    def get_letter_frequencies(self, t):
        frequency_letters = {}

        for letter in t:
            if letter not in frequency_letters:
                frequency_letters[letter] = 0
            frequency_letters[letter] += 1

        return frequency_letters

    def sliding_window_has_all_letters(self, frequency_letters):
        for key in frequency_letters:
            if frequency_letters[key] > 0:
                return False
        return True
