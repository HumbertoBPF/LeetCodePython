from typing import List


class Solution:
    # Time complexity: O(n) due to the for loop. The while loop doesn't interfere in the complexity because we
    # pop and append the stack at most once
    # Space complexity: O(n) due to the stack size
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # This stack will store the histogram bars that we can extend
        stack = []
        max_area = 0

        for i in range(n):
            height = heights[i]

            extending_from_index = i
            # The condition (stack[-1][0] > height) means the current bar is shorter than the top bar
            # on the stack
            while (len(stack) != 0) and (stack[-1][0] > height):
                popped_height, popped_index = stack.pop()
                # We need to track the earliest index which we can start extending from for the current bar
                extending_from_index = popped_index
                # Compute the maximum area we got with the popped bar
                max_area = max(max_area, popped_height * (i - popped_index))

            stack.append([height, extending_from_index])
        # We need to compute the maximum area for the items that remained on the stack
        while len(stack) != 0:
            popped_height, popped_index = stack.pop()
            extending_from_index = popped_index
            max_area = max(max_area, popped_height * (i + 1 - popped_index))

        return max_area