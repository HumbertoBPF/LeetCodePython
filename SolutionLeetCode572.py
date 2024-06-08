from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        match_list = []

        self.search(root, subRoot.val, match_list)

        if len(match_list) == 0:
            return False

        for initial_node in match_list:
            subtrees_match = self.search_for_matches(initial_node, subRoot)

            if subtrees_match:
                return True

        return False

    def are_nodes_equal(self, node1, node2):
        node1_is_none = node1 is None
        node2_is_none = node2 is None

        if node1_is_none is not node2_is_none:
            return False

        if not node1_is_none and not node2_is_none:
            return self.search_for_matches(node1, node2)

        return True

    def search_for_matches(self, node1, node2):
        if node1.val != node2.val:
            return False

        left_children_match = self.are_nodes_equal(node1.left, node2.left)

        right_children_match = self.are_nodes_equal(node1.right, node2.right)

        return left_children_match and right_children_match

    def search(self, root, x, match_list):
        current_node = root

        if current_node.val == x:
            match_list.append(current_node)

        if current_node.left is not None:
            self.search(current_node.left, x, match_list)

        if current_node.right is not None:
            self.search(current_node.right, x, match_list)
