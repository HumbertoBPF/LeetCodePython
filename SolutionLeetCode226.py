from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        nodes_to_visit = deque()
        nodes_to_visit.append(root)

        while len(nodes_to_visit) != 0:
            current_node = nodes_to_visit.popleft()

            left_child = current_node.left
            right_child = current_node.right

            if left_child is not None:
                nodes_to_visit.append(left_child)

            if right_child is not None:
                nodes_to_visit.append(right_child)

            current_node.left = right_child
            current_node.right = left_child

        return root