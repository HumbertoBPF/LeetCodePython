from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(log n)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)

    def dfs(self, current_node, target):
        if current_node is None:
            return None

        if current_node.val == target:
            return current_node

        if target < current_node.val:
            left_child = current_node.left
            return self.dfs(left_child, target)

        if target > current_node.val:
            right_child = current_node.right
            return self.dfs(right_child, target)