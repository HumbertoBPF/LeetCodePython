from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, { "k": 0 }, k)

    def dfs(self, current_node, constraints, target_k):
        left_child = current_node.left

        if left_child is not None:
            kth_smallest = self.dfs(left_child, constraints, target_k)

            if kth_smallest is not None:
                return kth_smallest

        constraints["k"] += 1

        if constraints["k"] == target_k:
            return current_node.val

        right_child = current_node.right

        if right_child is not None:
            constraints["k"] += 1

            if constraints["k"] == target_k:
                return right_child.val

            kth_smallest = self.dfs(right_child, constraints, target_k)

            if kth_smallest is not None:
                return kth_smallest
