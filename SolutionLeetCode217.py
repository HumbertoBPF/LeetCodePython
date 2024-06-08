from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        already_seen = set()

        for num in nums:
            if num in already_seen:
                return True

            already_seen.add(num)

        return False


solution = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
result = solution.containsDuplicate(nums)
print(result)
