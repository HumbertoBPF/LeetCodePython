from typing import List


class Solution:
    # Time complexity: O(n*(n + k))
    # Space complexity: O(n)
    # where n is the number of words and k is the maximum size of a word
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        max_product = 0
        # O(n*k) (n for the iteration over all the words and k for storing the letters of a word in the set)
        words_letters = [self.get_letters_set(word) for word in words]
        # O(n^2) (n^2 because we check every pair of words)
        for i in range(n):
            for j in range(i, n):
                word_1 = words[i]
                word_2 = words[j]

                word_1_letters = words_letters[i]
                word_2_letters = words_letters[j]
                # This is constant time, because the sets have at most 32 items (O(32) = O(1))
                if len(word_1_letters.intersection(word_2_letters)) == 0:
                    product = len(word_1) * len(word_2)
                    max_product = max(product, max_product)

        return max_product

    def get_letters_set(self, word):
        letters_word = set()

        for letter in word:
            letters_word.add(letter)

        return letters_word