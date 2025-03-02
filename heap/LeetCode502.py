import heapq
from typing import List


class Solution:
    # Time complexity: O((n + k)*log n)
    # Space complexity: O(n)
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # Heap containing the products that we can finish. It is a max heap based on their profit because we want to
        # maximize it
        can_finish_heap = []
        # Heap containing the products that we cannot finish. It is a min heap because when our capital increases, we
        # want to transfer the items with the smallest price to the heap above.
        cannot_finished_heap = []

        for i in range(n):
            if capital[i] <= w:
                heapq.heappush(can_finish_heap, (-profits[i], i))
                continue
            heapq.heappush(cannot_finished_heap, (capital[i], i))

        current_capital = w
        nb_finished_products = 0

        while (len(can_finish_heap) > 0) and (nb_finished_products < k):
            finished_project = heapq.heappop(can_finish_heap)
            current_capital += (-finished_project[0])
            # Transfer the products that we can finish with the new capital to the appropriate heap
            while (len(cannot_finished_heap) > 0) and (cannot_finished_heap[0][0] <= current_capital):
                _, i = heapq.heappop(cannot_finished_heap)
                heapq.heappush(can_finish_heap, (-profits[i], i))

            nb_finished_products += 1

        return current_capital
