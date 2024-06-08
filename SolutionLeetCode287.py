from typing import List


class Solution:
    def findDuplicateSquared(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 2:
            return nums[0]

        for i in range(n):
            current_item = nums[i]

            for j in range(i + 1, n):
                if current_item == nums[j]:
                    return current_item

        return n + 1

    def nb_items_in_interval(self, nums, lower_bound, upper_bound):
        nb_items = 0

        for num in nums:
            if lower_bound <= num <= upper_bound:
                nb_items += 1

        return nb_items

    def findDuplicateBinarySearch(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 2:
            return nums[0]

        lower_bound = 1
        upper_bound = n

        while upper_bound - lower_bound > 1:
            mid = (upper_bound + lower_bound) // 2

            nb_items_between_lower_and_mid = self.nb_items_in_interval(nums, lower_bound, mid)

            if nb_items_between_lower_and_mid > (mid - lower_bound + 1):
                upper_bound = mid
                continue

            lower_bound = mid

        is_lower_bound = self.nb_items_in_interval(nums, lower_bound, lower_bound) > 1

        return lower_bound if is_lower_bound else upper_bound


    def findDuplicateLinear(self, nums: List[int]) -> int:
        slow_pointer = 0
        fast_pointer = 0

        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]

            if slow_pointer == fast_pointer:
                break

        slow_pointer = 0

        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

        return fast_pointer


# [3,1,3,4,2]
# slow_pointer = 0
# fast_pointer = 0
# First iteration
# slow_pointer = nums[slow_pointer] = nums[0] = 3
# fast_pointer = nums[nums[fast_pointer]] = nums[nums[0]] = nums[3] = 4
# Second iteration
# slow_pointer = nums[slow_pointer] = nums[3] = 4
# fast_pointer = nums[nums[fast_pointer]] = nums[nums[4]] = nums[2] = 3
# Third iteration
# slow_pointer = nums[slow_pointer] = nums[4] = 2
# fast_pointer = nums[nums[fast_pointer]] = nums[nums[3]] = nums[4] = 2
# Reset slow pointer
# slow_pointer = 0
# fast_pointer = 2
# First iteration
# slow_pointer = nums[slow_pointer] = nums[0] = 3
# fast_pointer = nums[fast_pointer] = nums[3] = 3
solution = Solution()
nums = [1,3,4,2,2]
print(solution.findDuplicateSquared(nums))
