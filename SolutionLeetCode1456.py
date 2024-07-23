class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        
        start = 0
        end = k - 1

        max_vowels = 0
        nb_vowels = 0

        for i in range(k):
            if self.is_vowel(s[i]):
                nb_vowels += 1

        max_vowels = max(max_vowels, nb_vowels)

        while True:
            # Checking if we will have to remove a vowel when moving the sliding window
            if self.is_vowel(s[start]):
                nb_vowels -= 1
            # Moving the sliding window
            end += 1
            start += 1
            # Checking if we've exceeded the bounds
            if end >= n:
                break
            # Checking if we have added a vowel when we moved the sliding window
            if self.is_vowel(s[end]):
                nb_vowels += 1
            # Update the maximum number of vowels
            max_vowels = max(max_vowels, nb_vowels)

        return max_vowels
    
    def is_vowel(self, char):    
        return (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u")
            