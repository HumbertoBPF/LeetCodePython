class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_dict = dict()

        for letter in s:
            if frequency_dict.get(letter) is None:
                frequency_dict[letter] = 1
            else:
                frequency_dict[letter] += 1

        for letter in t:
            frequency_letter = frequency_dict.get(letter)

            if frequency_letter is None or frequency_letter == 0:
                return False
            elif frequency_letter == 1:
                del frequency_dict[letter]
            else:
                frequency_dict[letter] -= 1

        return len(frequency_dict) == 0


s = "rat"
t = "car"
solution = Solution()
result = solution.isAnagram(s, t)
print(result)
