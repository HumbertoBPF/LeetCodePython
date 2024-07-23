VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s_vowels = []

        # Store all vowels of s
        for i in range(n):
            letter = s[i]

            if letter in VOWELS:
                s_vowels.append(letter)

        s_with_reversed_vowels = ""

        number_vowels = len(s_vowels)
        vowel_index = 0
        # Building output string (s with the vowels reversed)
        for i in range(n):
            letter = s[i]
            # If we find a vowel, we look in the list "vowels" to find the one in the symmetric relative position
            if letter in VOWELS:
                s_with_reversed_vowels += s_vowels[number_vowels - 1 - vowel_index]
                vowel_index += 1
                continue

            s_with_reversed_vowels += letter

        return s_with_reversed_vowels
