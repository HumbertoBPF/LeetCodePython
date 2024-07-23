import heapq
from typing import List


class Solution:
    # Time complexity: O(n*(log n + log k))
    # Space complexity: O(n)
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        # We build a list zipping nums1 and nums2. This list will contain the values that we need to compute the score.
        nums = [(nums1[i], nums2[i]) for i in range(n)]
        # We sort the list in the descending order based on the value obtained from nums2.
        nums.sort(key=lambda x: x[1], reverse=True)
        # This heap will contain the k largest values from nums1 from 0 to i (when iterating over nums)
        heap_nums_1 = []

        max_score = float("-inf")
        max_sum = 0
        # O(n*log k)
        for i in range(n):
            num1, num2 = nums[i]

            heapq.heappush(heap_nums_1, num1)
            max_sum += num1
            # We start computing scores when we have k items
            if len(heap_nums_1) == k:
                # Since we sorted nums based on nums2, the minimum value from num2 at is nums2[i] when we consider the
                # items from 0 to i
                max_score = max(max_score, max_sum*num2)
                # Pop the smallest item from the heap and decrement the sum by it. This value will be replaced with
                # nums[i + 1][0], which is a mandatory value to be taken into account in the sum (because we will pick
                # nums[i + 1][1])
                max_sum -= heapq.heappop(heap_nums_1)

        return max_score


solution = Solution()
nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
print(solution.maxScore(nums1, nums2, 2))
