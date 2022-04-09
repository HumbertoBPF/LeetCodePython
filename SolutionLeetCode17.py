from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_digit_letters = {"2": ["a", "b", "c"],
                             "3": ["d", "e", "f"],
                             "4": ["g", "h", "i"],
                             "5": ["j", "k", "l"],
                             "6": ["m", "n", "o"],
                             "7": ["p", "q", "r", "s"],
                             "8": ["t", "u", "v"],
                             "9": ["w", "x", "y", "z"]}
        # No digits, return empty list
        if len(digits) == 0:
            return []
        # When there is only one digit, return the correspondent list of letters
        if len(digits) == 1:
            return map_digit_letters[digits[0]]

        return self.get_combinations_containing_substring(map_digit_letters, deque(digits), "", [])

    def get_combinations_containing_substring(self, map_digit_letters, digitsQueue, substring, combinations):
        # When we used all the digits of the input string, we have obtained one combination
        if len(digitsQueue) == 0:
            combinations.append(substring)
            return combinations

        current_digit = digitsQueue.popleft()
        current_letters = map_digit_letters[current_digit]
        # Append the substring with each letter that can is mapped for the current digit and get all the combinations
        # containing this substring
        for letter in current_letters:
            self.get_combinations_containing_substring(map_digit_letters, digitsQueue.copy(), substring + letter, combinations)

        return combinations


o1 = Solution()
print(o1.letterCombinations("2"))
