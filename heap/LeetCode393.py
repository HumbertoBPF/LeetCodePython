import heapq
from typing import List


class Solution:
    # Time complexity: O(n*m*log k)
    # Space complexity: O(k)
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []

        for num1 in nums1:
            for num2 in nums2:
                item = (-(num1 + num2), num1, num2)

                if len(max_heap) < k:
                    heapq.heappush(max_heap, item)
                    continue

                if item[0] > max_heap[0][0]:
                    heapq.heappushpop(max_heap, item)
                    continue
                # If we get a sum greater than the maximum sum of the heap, we can leave the inner loop, since the sums
                # are non-decreasing
                break

        return [[item[1], item[2]] for item in max_heap]

    # Time complexity: O(k*log k)
    # Space complexity: O(k)
    def kSmallestPairsOptimized(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        output = []
        candidates_heap = []
        visited = set()

        heapq.heappush(candidates_heap, (nums1[0] + nums2[0], 0, 0))

        while len(output) < k:
            _, i, j = heapq.heappop(candidates_heap)
            output.append([nums1[i], nums2[j]])
            # As candidates of the lowest sum greater than the current one, we have:
            # - nums1[i + 1] + nums2[j]
            # - nums1[i] + nums2[j + 1]
            # - All other sums that we have already included to the heap
            # We must check the bounds ot the array and track pairs that have already been added to the heap to avoid
            # duplicates
            if (i + 1 < n) and ((i + 1, j) not in visited):
                heapq.heappush(candidates_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if (j + 1 < m) and ((i, j + 1) not in visited):
                heapq.heappush(candidates_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return output
