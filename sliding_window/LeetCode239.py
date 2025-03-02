from collections import deque
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        monotonic_queue = deque()

        output = []

        for end in range(n):
            num = nums[end]

            start = end - (k - 1)

            while (len(monotonic_queue) > 0) and ((nums[monotonic_queue[0]] <= num) or (monotonic_queue[0] < start)):
                monotonic_queue.popleft()

            while (len(monotonic_queue) > 0) and ((nums[monotonic_queue[-1]] <= num) or (monotonic_queue[-1] < start)):
                monotonic_queue.pop()

            monotonic_queue.append(end)

            if start >= 0:
                output.append(nums[monotonic_queue[0]])

        return output