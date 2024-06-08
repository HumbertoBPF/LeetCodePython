from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = self.group_by_frequency_of_letters(strs)

        anagrams_grouped = []

        for key in anagram_dict:
            anagrams = anagram_dict[key]
            anagrams_grouped.append(anagrams)

        return anagrams_grouped

    def group_by_frequency_of_letters(self, words):
        anagram_dict = {}

        for word in words:
            frequency_list = self.get_frequency_list(word)
            hashable_frequency_list = str(frequency_list)

            if anagram_dict.get(hashable_frequency_list) is None:
                anagram_dict[hashable_frequency_list] = [word]
            else:
                anagram_dict[hashable_frequency_list].append(word)

        return anagram_dict


    def get_frequency_list(self, word):
        frequency_list = [0 for _ in range(26)]

        for letter in word:
            letter_index = ord(letter) - ord("a")
            frequency_list[letter_index] += 1

        return frequency_list



solution = Solution()
strs = ["a"]
print(solution.groupAnagrams(strs))
