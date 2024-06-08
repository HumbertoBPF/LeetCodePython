from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n == k:
            return nums

        occurrences_list = self.get_occurrences_list(nums)

        occurrences_list = sorted(occurrences_list, key=lambda x: x[1])
        number_unique_el = len(occurrences_list)

        most_frequents = []

        for i in range(k):
            ith_most_frequent = occurrences_list[number_unique_el-1-i][0]
            most_frequents.append(ith_most_frequent)

        return most_frequents


    def get_occurrences_list(self, nums):
        occurrences_dict = {}

        for num in nums:
            if occurrences_dict.get(num) is None:
                occurrences_dict[num] = 0

            occurrences_dict[num] += 1

        return [[key, occurrences_dict[key]] for key in occurrences_dict]


# solution = Solution()
# nums = [1]
# k = 1
# print(solution.topKFrequent(nums, k))
