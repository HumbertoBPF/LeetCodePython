from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []

        last_depth = 0
        current_sum = 0
        current_n = 0

        queue = deque()

        queue.append((root, 0))

        while len(queue) > 0:
            current_node, depth = queue.popleft()

            left_child = current_node.left

            if left_child is not None:
                queue.append((left_child, depth + 1))

            right_child = current_node.right

            if right_child is not None:
                queue.append((right_child, depth + 1))

            if depth != last_depth:
                # When we just changed the level, we have to append the average of the last level to the output list
                output.append(current_sum/current_n)
                current_sum = 0
                current_n = 0

            last_depth = depth
            current_sum += current_node.val
            current_n += 1
        # Taking into account the last level
        output.append(current_sum/current_n)

        return output
