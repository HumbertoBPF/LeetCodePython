import heapq
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Trivial case (only one permutation)
        if n == 1:
            return

        first_to_be_incr = n - 2
        # Finding the leftmost item that will be incremented
        # O(n)
        while (first_to_be_incr >= 0) and (nums[first_to_be_incr] >= nums[first_to_be_incr + 1]):
            first_to_be_incr -= 1
        # If right_pointer is -1, then the next permutation is the first one
        # Otherwise we have to search the smallest item after the position to be incremented holding a value greater
        # than nums[first_to_be_incr]
        if first_to_be_incr != -1:
            replacer = float("inf")
            replacer_index = -1
            # Searching the lowest item on the right of the element to be incremented
            # O(n)
            for i in range(first_to_be_incr + 1, n):
                if (nums[i] > nums[first_to_be_incr]) and (nums[i] <= replacer):
                    replacer = nums[i]
                    replacer_index = i

            nums[replacer_index] = nums[first_to_be_incr]
            nums[first_to_be_incr] = replacer
        # All the items after the first element to be incremented must be in the increasing order
        # Because actually they are in the decreasing order, we just need to revert the subarray going from
        # [first_to_be_incr + 1, n - 1]
        # O(n)
        length_subarray = n - (first_to_be_incr + 1)

        for i in range(0, length_subarray // 2):
            real_index = first_to_be_incr + 1 + i

            tmp = nums[n - i - 1]
            nums[n - i - 1] = nums[real_index]
            nums[real_index] = tmp


class SolutionBubbleSort:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Trivial case (only one permutation)
        if n == 1:
            return

        first_to_be_incr = n - 2
        # Finding the leftmost item that will be incremented
        # O(n)
        while (first_to_be_incr >= 0) and (nums[first_to_be_incr] >= nums[first_to_be_incr + 1]):
            first_to_be_incr -= 1
        # If right_pointer is -1, then the next permutation is the first one
        # Otherwise we have to search the smallest item after the position to be incremented holding a value greater
        # than nums[first_to_be_incr]
        if first_to_be_incr != -1:
            replacer = float("inf")
            replacer_index = -1
            # Searching the lowest item on the right of the element to be incremented
            # O(n)
            for i in range(first_to_be_incr + 1, n):
                if (nums[i] > nums[first_to_be_incr]) and (nums[i] < replacer):
                    replacer = nums[i]
                    replacer_index = i

            nums[replacer_index] = nums[first_to_be_incr]
            nums[first_to_be_incr] = replacer
        # All the items after the first element to be incremented must be in the increasing order
        # O(n^2)
        for i in range(first_to_be_incr + 1, n):
            replacer_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[replacer_index]:
                    replacer_index = j

            tmp = nums[replacer_index]
            nums[replacer_index] = nums[i]
            nums[i] = tmp


class SolutionHeap:
    # Time complexity: O(n*log n)
    # Space complexity: O(n)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Trivial case (only one permutation)
        if n == 1:
            return

        first_to_be_incr = n - 2
        # Finding the leftmost item that will be incremented
        # O(n)
        while (first_to_be_incr >= 0) and (nums[first_to_be_incr] >= nums[first_to_be_incr + 1]):
            first_to_be_incr -= 1
        # If right_pointer is -1, then the next permutation is the first one
        # Otherwise we have to search the smallest item after the position to be incremented holding a value greater
        # than nums[first_to_be_incr]
        if first_to_be_incr != -1:
            replacer = float("inf")
            replacer_index = -1
            # Searching the lowest item on the right of the element to be incremented
            # O(n)
            for i in range(first_to_be_incr + 1, n):
                if (nums[i] > nums[first_to_be_incr]) and (nums[i] < replacer):
                    replacer = nums[i]
                    replacer_index = i

            nums[replacer_index] = nums[first_to_be_incr]
            nums[first_to_be_incr] = replacer
        # Using a min heap to sort the items from [first_to_be_incr + 1, n - 1]
        # O(n*log n)
        min_heap = []

        for i in range(first_to_be_incr + 1, n):
            heapq.heappush(min_heap, nums[i])

        for i in range(first_to_be_incr + 1, n):
            nums[i] = heapq.heappop(min_heap)
