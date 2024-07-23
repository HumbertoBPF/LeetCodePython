class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequencies_word_1 = self.get_letter_frequencies(word1)
        frequencies_word_2 = self.get_letter_frequencies(word2)

        return (self.keys_match(frequencies_word_1, frequencies_word_2) and
                self.get_values_frequencies(frequencies_word_1) == self.get_values_frequencies(frequencies_word_2))

    def get_letter_frequencies(self, word):
        frequencies = {}

        for letter in word:
            if letter not in frequencies:
                frequencies[letter] = 0
            frequencies[letter] += 1

        return frequencies

    def keys_match(self, dictionary1, dictionary2):
        keys_dictionary_1 = set()

        for key in dictionary1:
            keys_dictionary_1.add(key)

        for key in dictionary2:
            if key not in keys_dictionary_1:
                return False

        return True

    def get_values_frequencies(self, dictionary):
        values_frequencies = {}

        for key in dictionary:
            value = dictionary[key]
            if value not in values_frequencies:
                values_frequencies[value] = 0
            values_frequencies[value] += 1

        return values_frequencies
