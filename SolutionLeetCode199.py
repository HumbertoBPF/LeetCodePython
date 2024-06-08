from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        level_nodes = deque()
        level_nodes.append(root)

        right_side_list = []

        while len(level_nodes) != 0:
            n = len(level_nodes)

            for i in range(n):
                current_node = level_nodes.popleft()

                left_child = current_node.left

                if left_child is not None:
                    level_nodes.append(left_child)

                right_child = current_node.right

                if right_child is not None:
                    level_nodes.append(right_child)
                # Add the last node in the current level to the right side list (right most node)
                if i == n - 1:
                    right_side_list.append(current_node.val)

        return right_side_list


# level_nodes = [1]
#
# level_nodes = [3]
# right_side_list = [1]
#
# level_nodes = [4, 5]
# right_side_list = [1, 3]
#
# level_nodes = [7, 6]
# right_side_list = [1, 3, 5]
#
# level_nodes = [8]
# right_side_list = [1, 3, 5, 6]
#
# level_nodes = [9]
# right_side_list = [1, 3, 5, 6, 8]
#
# level_nodes = []
# right_side_list = [1, 3, 5, 6, 8, 9]