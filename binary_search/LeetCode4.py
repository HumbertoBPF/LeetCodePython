from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums_1 = nums1
        self.nums_2 = nums2

        self.n = len(nums1)
        self.m = len(nums2)

        len_first_half = (self.n + self.m) // 2

        lower = 0
        upper = self.m

        if self.is_valid_partition(lower):
            return self.compute_median(lower)

        if self.is_valid_partition(upper):
            return self.compute_median(upper)

        while True:
            mid = (upper + lower) // 2
            # We need to increase the partition of nums1 (i.e. decrease the partition of nums2)
            if self.get_item(nums2, mid - 1) > self.get_item(nums1, len_first_half - mid):
                upper = mid
                continue
            # We need to increase the partition of nums2
            if self.get_item(nums1, len_first_half - mid - 1) > self.get_item(nums2, mid):
                lower = mid
                continue
            break

        return self.compute_median(mid)

    def compute_median(self, p2):
        len_first_half = (self.n + self.m) // 2

        if (self.n + self.m) % 2 == 0:
            return (max(
                self.get_item(self.nums_1, len_first_half - p2 - 1),
                self.get_item(self.nums_2, p2 - 1)
            ) + min(
                self.get_item(self.nums_1, len_first_half - p2),
                self.get_item(self.nums_2, p2)
            )) / 2

        return min(
            self.get_item(self.nums_1, len_first_half - p2),
            self.get_item(self.nums_2, p2)
        )

    def is_valid_partition(self, p2):
        len_first_half = (self.n + self.m) // 2

        return (
                self.get_item(self.nums_2, p2 - 1) <= self.get_item(self.nums_1, len_first_half - p2)
        ) and (
                self.get_item(self.nums_1, len_first_half - p2 - 1) <= self.get_item(self.nums_2, p2)
        )

    def get_item(self, arr: List[int], index: int) -> float:
        n = len(arr)

        if index < 0:
            return float("-inf")

        if index > n - 1:
            return float("inf")

        return arr[index]

# solution = Solution()
# nums1 = [1,2,3]
# nums2 = []
# print(solution.findMedianSortedArrays(nums1, nums2))