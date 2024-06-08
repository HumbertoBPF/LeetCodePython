from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        shared_data = {"diameter": 0}
        self.dfs(root, shared_data)
        return shared_data["diameter"]

    def dfs(self, current_node, shared_data):
        left_child = current_node.left
        right_child = current_node.right
        # If node is a leaf, its depth is zero
        if (left_child is None) and (right_child is None):
            return 0

        max_left_depth = 0
        max_right_depth = 0

        if left_child is not None:
            max_left_depth = self.dfs(left_child, shared_data)
            # Takes into account that we are going up in the hierarchy of the tree
            max_left_depth += 1

        if right_child is not None:
            max_right_depth = self.dfs(right_child, shared_data)
            # Takes into account that we are going up in the hierarchy of the tree
            max_right_depth += 1
        # The longest path links the deepest node on the left to the deepest node on the right
        longest_path = max_left_depth + max_right_depth

        if longest_path > shared_data["diameter"]:
            shared_data["diameter"] = longest_path
        # Returns the greatest depth
        return max(max_left_depth, max_right_depth)


solution = Solution()
root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# node3 = TreeNode(4)
# root.left = node1
# root.right = node2
# node2.right = node3
print(solution.diameterOfBinaryTree(root))
