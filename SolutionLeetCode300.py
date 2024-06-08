from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        memory = [0]*n

        self.find_increasing_sequence_from(0, nums, memory)

        length_lis = 1

        for i in range(n):
            length_lis = max(length_lis, memory[i])

        return length_lis

    def find_increasing_sequence_from(self, index, nums, memory):
        if memory[index] != 0:
            return memory[index]

        n = len(nums)

        max_length = 1

        for i in range(index + 1, n):
            length = self.find_increasing_sequence_from(i, nums, memory)
            if nums[i] > nums[index]:
                max_length = max(max_length, 1 + length)

        memory[index] = max_length
        return max_length


nums = [4,10,4,3,8,9]
solution = Solution()
print(solution.lengthOfLIS(nums))
