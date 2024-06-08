from typing import List
import heapq


class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(1)
    def kClosestWithList(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(n log n)
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # O(n)
        return points[:k]
    # Time complexity: O (n log k)
    # Space complexity: O(k)
    def kClosestHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        # O(n)
        for point in points:
            priority = point[0] ** 2 + point[1] ** 2
            # O(log k)
            if len(max_heap) < k:
                # We add the minus sign to convert the Python native heapq min heap into a max heapq
                heapq.heappush(max_heap, [-priority, point])
                continue

            max_priority_item = max_heap[0]
            max_priority = -max_priority_item[0]
            # O(log k)
            if priority < max_priority:
                heapq.heappop(max_heap)
                # We add the minus sign to convert the Python native heapq min heap into a max heapq
                heapq.heappush(max_heap, [-priority, point])

        k_closest = [item[1] for item in max_heap]

        return k_closest
