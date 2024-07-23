import heapq


class SmallestInfiniteSet:
    # Time complexity: O(1)
    def __init__(self):
        # Lower bound such that all numbers in [counter, +inf) are in the SmallestInfiniteSet
        self.counter = 1
        # Heap to track items that are added again to the data structure after being popped
        self.min_heap = []
        # Hash set to guarantee that we don't have duplicates in the heap
        self.added_numbers = set()
        heapq.heapify(self.min_heap)
    # Time complexity: O(1) considering that the heap will have at most 1000 items due to a maximum of 1000 calls of
    # the data structure methods. For a heap with a number arbitrary of items n, the complexity would be O(log n)
    def popSmallest(self) -> int:
        # If the heap is empty, we pop the smallest item in the interval [counter, +inf)
        if len(self.min_heap) == 0:
            smallest = self.counter
            self.counter += 1
            return smallest
        # If the heap is not empty, the smallest item in the data structure is on the top of it
        smallest = heapq.heappop(self.min_heap)
        # Update the hash set with the heap items
        self.added_numbers.remove(smallest)
        return smallest
    # Time complexity: O(1) considering that the heap will have at most 1000 items due to a maximum of 1000 calls of
    # the data structure methods. For a heap with a number arbitrary of items n, the complexity would be O(log n)
    def addBack(self, num: int) -> None:
        # If the number is not in the interval [counter, +inf), we add it back by pushing the heap and adding it to the
        # hash set
        if (num < self.counter) and (num not in self.added_numbers):
            heapq.heappush(self.min_heap, num)
            self.added_numbers.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)