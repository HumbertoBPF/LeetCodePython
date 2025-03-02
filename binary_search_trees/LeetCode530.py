# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.in_order = []

        self.in_order_traversal(root)

        min_diff = float("inf")

        n = len(self.in_order)

        for i in range(1, n):
            min_diff = min(self.in_order[i] - self.in_order[i - 1], min_diff)

        return min_diff


    def in_order_traversal(self, node):
        left_child = node.left

        if left_child is not None:
            self.in_order_traversal(left_child)

        self.in_order.append(node.val)

        right_child = node.right

        if right_child is not None:
            self.in_order_traversal(right_child)

