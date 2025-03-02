from typing import Optional

MIN_VAL = -10 ** 8


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) due to the recursion stack
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = MIN_VAL
        self.dfs(root)
        return self.max_path_sum

    def dfs(self, node):
        left_child = node.left
        right_child = node.right

        node_val = node.val
        max_path_left_child = MIN_VAL
        max_path_right_child = MIN_VAL

        if left_child is not None:
            max_path_left_child = self.dfs(left_child)

        if right_child is not None:
            max_path_right_child = self.dfs(right_child)
        # Update the maximum path sum considering only the nodes below the current node
        # We distinguish four cases:
        # - Path with only the current node
        # - Path going from the current node to a left leaf
        # - Path going from the current node to a right leaf
        # - Path going from a left leaf to a right leaf
        self.max_path_sum = max(
            self.max_path_sum,
            node_val,
            node_val + max_path_left_child + max_path_right_child,
            node_val + max_path_right_child,
            node_val + max_path_left_child
        )
        # We return the best path containing only one leaf for the level above
        return max(
            node_val,
            node_val + max_path_right_child,
            node_val + max_path_left_child
        )