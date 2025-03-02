import heapq


# Space complexity: O(n)
class MedianFinder:
    # Time complexity: O(1)
    def __init__(self):
        # Max heap storing the items of the first half of the sorted array
        self.first_half = []
        # Min heap storing the items of the second half of the sorted array
        self.second_half = []
        # We will use heaps because we are only interested in identifying two items: the greatest one from the first
        # half and the lowest one from the second half
    # Time complexity: O(log n)
    def addNum(self, num: int) -> None:
        # The "first_half" heap must receive a new item
        if len(self.first_half) == len(self.second_half):
            # If the input is lower than or equal to the greatest item of the first half, it can go directly to the
            # first half
            if (len(self.first_half) == 0) or (num <= -self.first_half[0]):
                heapq.heappush(self.first_half, -num)
                return
            # Otherwise, we add the input to the second half, and we move its lowest item to the first half to
            # re-distribute/re-balance the items between the halves
            lowest_item_from_second_half = heapq.heappushpop(self.second_half, num)
            heapq.heappush(self.first_half, -lowest_item_from_second_half)
            return
        # If the first half has more items than the second one, the second half must receive a new item
        # If the input is greater than or equal to the greatest item of the first, it can go directly to the second half
        if num >= -self.first_half[0]:
            heapq.heappush(self.second_half, num)
            return
        # Otherwise, we add the input to the first half, and we move its greatest item to the second half to
        # re-distribute/re-balance the items between the halves
        greatest_item_from_first_half = -heapq.heappushpop(self.first_half, -num)
        heapq.heappush(self.second_half, greatest_item_from_first_half)
    # Time complexity: O(1)
    def findMedian(self) -> float:
        # We will store the items in the "first_half" heap with a reversed sign because Python's built-in
        # implementation of a heap is a min heap
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2
        return -self.first_half[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()