import heapq
from typing import List


class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(1)
    def findKthLargestWithList(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    # Time complexity: O(n log k)
    # Space complexity: O(k) (space to store the min heap)
    def findKthLargestWithHeap(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        # O(n)
        for num in nums:
            if len(min_heap) < k:
                # O(log k)
                heapq.heappush(min_heap, num)
                continue

            if num > min_heap[0]:
                # O(log k)
                heapq.heappop(min_heap)
                # O(log k)
                heapq.heappush(min_heap, num)

        return min_heap[0]
