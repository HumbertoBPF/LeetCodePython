# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def dfs_traversal(self, node, total_sum, sum_path):

        if node.left is not None:
            self.dfs_traversal(node.left, total_sum, sum_path + node.left.val)

        if node.right is not None:
            self.dfs_traversal(node.right, total_sum, sum_path + node.right.val)
