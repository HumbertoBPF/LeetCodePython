from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        while end - start > 1:
            middle = (end + start) // 2

            nums_middle = nums[middle]

            if nums_middle == target:
                return middle

            if nums_middle > target:
                end = middle
                continue

            if nums_middle < target:
                start = middle

        return -1


solution = Solution()
nums = [-1,0,3,5,9,12]
target = 3
print(solution.search(nums, target))
