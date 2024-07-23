import heapq

# Space complexity of the data structure: O(1) since a heap with at most 3000 items is kept
class RecentCounter:

    def __init__(self):
        self.min_heap = []
        heapq.heapify(self.min_heap)
    # Time complexity: O(log n)
    def ping(self, t: int) -> int:
        heapq.heappush(self.min_heap, t)
        # The number of iterations is at most 3000
        while len(self.min_heap) > 0 and self.min_heap[0] < t - 3000:
            heapq.heappop(self.min_heap)

        return len(self.min_heap)
