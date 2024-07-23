from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) due to the recursion stack
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zig_zag = 0

        if root.left is not None:
            self.dfs(root.left, True, 1)

        if root.right is not None:
            self.dfs(root.right, False, 1)

        return self.longest_zig_zag

    def dfs(self, current_node, left, zig_zag_depth):
        self.longest_zig_zag = max(self.longest_zig_zag, zig_zag_depth)

        left_child = current_node.left

        if left_child is not None:
            # If we went left in the previous call, we reset the zigzag depth. Otherwise, we increment it by one.
            self.dfs(left_child, True, 1 if left else zig_zag_depth + 1)

        right_child = current_node.right

        if right_child is not None:
            # If we went left in the previous call, we increment the zigzag depth by one. Otherwise, we reset it.
            self.dfs(right_child, False, zig_zag_depth + 1 if left else 1)
