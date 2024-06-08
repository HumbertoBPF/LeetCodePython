from typing import List
import heapq


class KthLargestWithList:
    # O(n log n)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
    # O(n)
    def add(self, val: int) -> int:
        n = len(self.nums)
        item_to_be_inserted = val

        for i in range(n):
            current_item = self.nums[i]

            if current_item > item_to_be_inserted:
                self.nums[i] = item_to_be_inserted
                item_to_be_inserted = current_item

        self.nums.append(item_to_be_inserted)

        return self.nums[-self.k]


class KthLargest:
    # O(n log k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def parent(self, i):
        # i = 2p + 1 => p = (i - 1)/2
        p = (i - 1) / 2
        # i = 2p + 2 => p = (i - 2)/2
        if i % 2 == 0:
            p = (i - 2) / 2

        return int(p)

    def remove_from_min_heap_root(self):
        self.min_heap[0] = self.min_heap[-1]
        self.min_heap.pop()

        n = len(self.min_heap)
        i = 0

        while i < n:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            smallest = i

            if (left_index < n) and (self.min_heap[smallest] > self.min_heap[left_index]):
                smallest = left_index

            if (right_index < n) and (self.min_heap[smallest] > self.min_heap[right_index]):
                smallest = right_index

            if smallest != i:
                temp = self.min_heap[smallest]
                self.min_heap[smallest] = self.min_heap[i]
                self.min_heap[i] = temp

                i = smallest
                continue

            break

    def insert_in_min_heap(self, val):
        n = len(self.min_heap)

        self.min_heap.append(val)

        i = n

        while i > 0:
            parent_index = self.parent(i)
            parent_item = self.min_heap[parent_index]
            current_item = self.min_heap[i]

            if parent_item > current_item:
                self.min_heap[parent_index] = current_item
                self.min_heap[i] = parent_item

                i = parent_index

                continue

            break

    # O(log k)
    def add(self, val: int) -> int:
        n = len(self.min_heap)

        if n < self.k:
            self.insert_in_min_heap(val)
        elif val > self.min_heap[0]:
            self.insert_in_min_heap(val)
            self.remove_from_min_heap_root()

        return self.min_heap[0]


class KthLargestNativeHeap:
    # O(n log k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        heapq.heapify(self.min_heap)

        for num in nums:
            self.add(num)

    # O(log k)
    def add(self, val: int) -> int:
        n = len(self.min_heap)

        if n < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappush(self.min_heap, val)
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
