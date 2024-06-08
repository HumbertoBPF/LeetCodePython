class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        if n == 1:
            return 1

        frequency_dict = {}
        longest_length = 0

        for i in range(n):
            most_frequent_letter = s[i]

            for j in range(i + longest_length, n):
                letter = s[j]

                if letter not in frequency_dict:
                    frequency_dict[letter] = 0
                frequency_dict[letter] += 1

                if frequency_dict[letter] > frequency_dict[most_frequent_letter]:
                    most_frequent_letter = letter

                nb_letters = j - i + 1
                nb_replaced_letters = j - i + 1 - frequency_dict[most_frequent_letter]

                if nb_replaced_letters > k:
                    break

                longest_length = max(longest_length, nb_letters)

            frequency_dict[s[i]] -= 1

        return longest_length


solution = Solution()
s = "ABBB"
print(solution.characterReplacement(s, k = 2))
