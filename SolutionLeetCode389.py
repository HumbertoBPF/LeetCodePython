class SolutionHashMap:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findTheDifference(self, s: str, t: str) -> str:
        frequency_map = {}

        for letter in s:
            if letter not in frequency_map:
                frequency_map[letter] = 0
            frequency_map[letter] += 1

        for letter in t:
            if letter not in frequency_map:
                return letter

            frequency_map[letter] -= 1

            if frequency_map[letter] == 0:
                del frequency_map[letter]

        return ""

class SolutionAsciiSum:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findTheDifference(self, s: str, t: str) -> str:
        sum_ascii = 0

        for letter in t:
            sum_ascii += ord(letter)

        for letter in s:
            sum_ascii -= ord(letter)

        return chr(sum_ascii)
