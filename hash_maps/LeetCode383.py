class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(m)
    # where n = len(ransomNote) and m = len(magazine)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_frequencies = {}

        for letter in magazine:
            if letter not in letters_frequencies:
                letters_frequencies[letter] = 0
            letters_frequencies[letter] += 1

        for letter in ransomNote:
            # Return false if we find a letter not present in magazine OR if the letter was in magazine but it is not
            # available anymore
            if (letter not in letters_frequencies) or (letters_frequencies[letter] == 0):
                return False
            letters_frequencies[letter] -= 1

        return True
