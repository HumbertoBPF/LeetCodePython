from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]

            return []

        triplets = set()
        nums.sort()

        for i in range(n - 2):
            nums_i = nums[i]
            p1 = i + 1
            p2 = n - 1

            while p1 != p2:
                nums_p1 = nums[p1]
                nums_p2 = nums[p2]

                current_sum = nums_i + nums_p1 + nums_p2

                if current_sum > 0:
                    p2 -= 1
                elif current_sum < 0:
                    p1 += 1
                else:
                    triplet = (nums_i, nums_p1, nums_p2)
                    triplets.add(triplet)
                    p1 += 1

        return [list(triplet) for triplet in triplets]
