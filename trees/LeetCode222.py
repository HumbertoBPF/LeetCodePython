from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O((log n)^2)
    # Space complexity: O(1)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Trivial case (empty tree)
        if root is None:
            return 0
        # Trivial case (tree with one node)
        if root.left is None:
            return 1

        height = self.get_height(root)
        # Search space = last level of the tree
        lower = 2**height
        upper = 2**(height + 1) - 1
        # If the upper index exists in the tree, the last layer is filled, and then it matches the number of nodes
        if self.is_in_tree(root, height, upper):
            return upper
        # We perform a binary search otherwise. At the end, the "lower" index is the last node of the binary tree
        while upper - lower > 1:
            mid = (upper + lower) // 2

            if self.is_in_tree(root, height, mid):
                lower = mid
                continue

            upper = mid

        return lower

    def is_in_tree(self, root, height, n):
        """
        Checks if the complete binary tree contains a nth node. This is done using bit manipulation to decide how to
        traverse the levels in order to look for the node we need.
        :param root: root of the concerned complete binary tree
        :param height: height of the binary tree
        :param n: index of the node whose existence must be verified
        :return: a boolean indicating if the node exists
        """
        current_node = root

        mask = 2**(height - 1)

        while mask > 0:
            if mask & n == mask:
                current_node = current_node.right
            else:
                current_node = current_node.left
            mask = mask >> 1

        return current_node is not None

    def get_height(self, root):
        """
        Gets the height of the complete binary tree. Because of the completeness, it's enough to go left all the time.
        :param root: root node of the tree whose height must be determined
        :return: the depth of the subtree starting at the specified root node
        """
        current_node = root
        height = 0

        while current_node.left is not None:
            current_node = current_node.left
            height += 1

        return height
