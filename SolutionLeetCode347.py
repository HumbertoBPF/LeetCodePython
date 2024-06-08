from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n == k:
            return nums

        occurrences_dict = self.get_occurrences_dict(nums)

        if k == len(occurrences_dict):
            return list(occurrences_dict.keys())

        most_frequents = []

        for j in range(k):
            most_frequent_key = self.get_most_frequent(occurrences_dict)

            most_frequents.append(most_frequent_key)

            del occurrences_dict[most_frequent_key]

        return most_frequents

    def get_occurrences_dict(self, nums):
        occurrences_dict = {}

        for num in nums:
            if occurrences_dict.get(num) is None:
                occurrences_dict[num] = 0

            occurrences_dict[num] += 1

        return occurrences_dict

    def get_most_frequent(self, occurrences_dict):
        most_frequent_key = None

        for key in occurrences_dict:
            if most_frequent_key is None:
                most_frequent_key = key

            value = occurrences_dict[key]

            if value > occurrences_dict[most_frequent_key]:
                most_frequent_key = key

        return most_frequent_key



# solution = Solution()
# nums = [1]
# k = 1
# print(solution.topKFrequent(nums, k))
