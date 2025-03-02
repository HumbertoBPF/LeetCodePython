from typing import List, Optional


class SolutionIterative:
    # Time complexity: O(n*sum(nums))
    # Space complexity: O(sum(nums))
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        # If the sum of the list items is not divisible by two, then the list cannot be split into two parts with the
        # same sum
        if sum(nums) % 2 != 0:
            return False

        target_sum = sum(nums) // 2

        partition_sums = {0}

        for num in nums:
            # We need a copy of the hash set because we cannot modify a hash set while iterating over it
            copy_partition_sums = partition_sums.copy()

            for item in copy_partition_sums:
                if item + num <= target_sum:
                    partition_sums.add(item + num)

        return target_sum in partition_sums


class SolutionRecursive:
    # Time complexity: O(n*sum(nums))
    # Space complexity: O(n*sum(nums))
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        # If the sum of the list items is not divisible by two, then the list cannot be split into two parts with the
        # same sum
        if sum(nums) % 2 != 0:
            return False

        n = len(self.nums)

        self.target = sum(self.nums) // 2
        self.cache = [None for _ in range(n)]

        return self.target in self.find_sum(0, 0)

    def find_sum(self, i: int, current_sum: int) -> Optional[set]:
        n = len(self.nums)
        # If we get a sum greater than the target, we don't need to store it because it will certainly result in a
        # unbalance the partitions
        if current_sum > self.target:
            return set()

        if i >= n:
            return {0}
        # Checking for cached results
        if self.cache[i] is not None:
            return self.cache[i]
        # Ignoring the ith item
        sums_1 = self.find_sum(i + 1, current_sum)
        # Adding the ith item to the partition
        tmp = self.find_sum(i + 1, current_sum + self.nums[i])
        sums_2 = set()
        # Adding the current item to cached sums
        for sum in tmp:
            if sum + self.nums[i] <= self.target:
                sums_2.add(sum + self.nums[i])
        # Cache the result
        self.cache[i] = sums_1.union(sums_2)
        return self.cache[i]