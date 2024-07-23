# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 1))

        max_level = 0
        max_sum = float("-inf")
        previous_level = 0
        current_sum = float("-inf")

        while len(queue) > 0:
            current_node, current_level = queue.popleft()
            # If a new level is processed
            if current_level != previous_level:
                # Update the maximum sum if needed
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_level = previous_level
                # Reset the current sum
                current_sum = 0
            # Updating the current_sum and the last visited level
            current_sum += current_node.val
            previous_level = current_level
            # Appending children
            left_child = current_node.left

            if left_child is not None:
                queue.append((left_child, current_level + 1))

            right_child = current_node.right

            if right_child is not None:
                queue.append((right_child, current_level + 1))
        # Check if the maximum sum needs to be updated for a last time
        if current_sum > max_sum:
            max_level = previous_level

        return max_level
