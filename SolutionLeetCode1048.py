from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_by_length = {}

        for word in words:
            word_length = len(word)
            if word_length not in words_by_length:
                words_by_length[word_length] = set()
            words_by_length[word_length].add(word)

        max_depth = 0
        memory = {}

        for word in words:
            depth = self.dfs(word, memory, words_by_length)
            if depth + 1 > max_depth:
                max_depth = depth + 1

        return max_depth

    def dfs(self, target_word, memory, words_by_length):
        if target_word in memory:
            return memory[target_word]

        word_length = len(target_word)

        words_with_length = words_by_length.get(word_length + 1, set())

        max_depth = 0

        for word in words_with_length:
            if self.is_predecessor(target_word, word):
                depth = self.dfs(word, memory, words_by_length)
                # Summing one to the depth to take into account the layer where we are
                if depth + 1 > max_depth:
                    max_depth = depth + 1
        # We store the maximum depth that we can achieve from this word
        memory[target_word] = max_depth
        return max_depth

    def is_predecessor(self, predecessor_word, word):
        pointer = 0

        for letter in word:
            if pointer >= len(predecessor_word):
                return True

            if letter == predecessor_word[pointer]:
                pointer += 1

        return pointer == len(predecessor_word)


solution = Solution()
words = ["a","b","ba","bca","bda","bdca"]
print(solution.longestStrChain(words))

