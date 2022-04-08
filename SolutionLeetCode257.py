from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.dfs_traversal(root, "", [])

    def dfs_traversal(self, node, path, paths):
        if len(path) != 0:
            path += "->"
        path += str(node.val)
        # Check if the current node is a leaf
        if (node.left is None) and (node.right is None):
            paths.append(path)
        # Check if we can go left
        if node.left is not None:
            self.dfs_traversal(node.left, path, paths)
        # Check if we can go right
        if node.right is not None:
            self.dfs_traversal(node.right, path, paths)

        return paths


o1 = Solution()
tree = TreeNode(1)
print(o1.binaryTreePaths(tree))
