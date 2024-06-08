class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        # Dictionary mapping a letter to a word
        bijection_dict = {}

        if len(pattern) != len(words):
            return False

        words_seen = set()
        n = len(pattern)

        for i in range(n):
            letter = pattern[i]
            word = words[i]

            if letter not in bijection_dict:
                # If a letter is seen for the first time, but the word has already been seen, we have a prob
                if word in words_seen:
                    return False

                bijection_dict[letter] = word
                words_seen.add(word)
                continue
            # We compare the current word to the word that has been mapped by the current letter
            if word != bijection_dict[letter]:
                return False

        return True
