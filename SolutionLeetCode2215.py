from typing import List


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    # where n = len(nums1) and m = len(nums2)
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [set(), set()]

        set_nums_1 = set()
        n = len(nums1)

        set_nums_2 = set()
        m = len(nums2)

        for i in range(n):
            set_nums_1.add(nums1[i])

        for i in range(m):
            set_nums_2.add(nums2[i])

        for i in range(n):
            # answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
            if nums1[i] not in set_nums_2:
                output[0].add(nums1[i])

        for i in range(m):
            # answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
            if nums2[i] not in set_nums_1:
                output[1].add(nums2[i])

        return [list(output[0]), list(output[1])]
