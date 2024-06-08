from typing import List


class SolutionHashMap:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        duplicated_num = 0
        absent_num = 0

        num_set = set()

        for i in range(n):
            num_set.add(i + 1)

        for num in nums:
            if num not in num_set:
                duplicated_num = num
                continue
            num_set.remove(num)

        for num in num_set:
            absent_num = num

        return [duplicated_num, absent_num]

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 2:
            if nums[0] == n:
                return [2, 1]
            return [1, 2]

        last_num = -1
        duplicated_num = 0
        predecessor_num = -1

        for i in range(n):
            num = nums[i]

            if num == last_num:
                duplicated_num = num
                if i - 2 >= 0:
                    predecessor_num = nums[i - 2]
                break

            last_num = num

        if (predecessor_num == -1) or (predecessor_num == duplicated_num - 1):
            return [duplicated_num, duplicated_num + 1]

        return [duplicated_num, duplicated_num - 1]
