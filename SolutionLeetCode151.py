class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverseWords(self, s: str) -> str:
        words = []
        current_word = ""

        for letter in s:
            # Don't include spaces in words
            if letter == " ":
                # When the current word is not empty, we should add it to the list "words" and start building a new word
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
                    continue
                continue

            current_word += letter
        # If we exit the iteration with a word being built add it to the list
        if current_word != "":
            words.append(current_word)

        number_of_words = len(words)
        reversed_words = ""
        # Build "reversed_words" by iterating over "words" in the reverse order
        for i in range(number_of_words):
            word = words[number_of_words - 1 - i]
            reversed_words += word
            # We don't add a space for the final index to avoid a trailing space
            if i != number_of_words - 1:
                reversed_words += " "

        return reversed_words
