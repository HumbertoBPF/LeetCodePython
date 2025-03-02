from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.s = s
        self.n = len(s)
        self.nb_words = len(words)
        self.word_len = len(words[0])

        words_frequency = {}

        for word in words:
            if word not in words_frequency:
                words_frequency[word] = 0
            words_frequency[word] += 1

        start = 0
        end = self.word_len

        output = []

        while start <= (self.n - self.word_len*self.nb_words):
            if self.check_concatenated_str(words_frequency, start, end):
                output.append(start)

            start += 1
            end += 1

        return output

    def check_concatenated_str(self, words_frequency, start, end):
        sliding_str = self.s[start:end]

        words_frequency_copy = words_frequency.copy()

        while sliding_str in words_frequency_copy:
            # Take into account the usage of a word
            words_frequency_copy[sliding_str] -= 1
            # If we can't use this word anymore, delete it from the copy
            if words_frequency_copy[sliding_str] == 0:
                del words_frequency_copy[sliding_str]
            # If all the words have been used, we found a concatenated string
            if len(words_frequency_copy) == 0:
                return True
            # Moving the sliding window
            start += self.word_len
            end += self.word_len
            # Checking if we got out of bounds
            if (start > self.n) or (end > self.n):
                break

            sliding_str = self.s[start:end]

        return False

class OptimizedSolution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.s = s
        self.n = len(s)
        self.nb_words = len(words)
        self.word_len = len(words[0])

        words_frequency = {}

        for word in words:
            if word not in words_frequency:
                words_frequency[word] = 0
            words_frequency[word] += 1

        output = []

        for i in range(0, self.word_len):
            start = i
            end = i + self.nb_words * self.word_len

            if end > self.n:
                break

            words_frequency_copy = words_frequency.copy()

            for j in range(self.nb_words):
                sliding_str = self.s[i + j * self.word_len:i + (j + 1) * self.word_len]

                if sliding_str in words_frequency_copy:
                    words_frequency_copy[sliding_str] -= 1

            if self.all_words_used(words_frequency_copy):
                output.append(start)

            while True:
                start += self.word_len
                end += self.word_len

                if end > self.n:
                    break

                removed_word = s[start - self.word_len:start]
                added_word = s[end - self.word_len:end]

                if removed_word in words_frequency:
                    words_frequency_copy[removed_word] = min(
                        words_frequency_copy[removed_word] + 1,
                        words_frequency[removed_word]
                    )

                if added_word in words_frequency:
                    words_frequency_copy[added_word] -= 1

                if self.all_words_used(words_frequency_copy):
                    output.append(start)

        return output

    def all_words_used(self, words_frequency):
        for key in words_frequency:
            if words_frequency[key] != 0:
                return False
        return True
