# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cache = {"nb_good_nodes": 0}
        self.dfs(root, cache, -100000)
        return cache["nb_good_nodes"]

    def dfs(self, current_node, cache, max_value):
        new_max_value = max_value

        if current_node.val >= max_value:
            cache["nb_good_nodes"] += 1
            new_max_value = current_node.val

        left_child = current_node.left

        if left_child is not None:
            self.dfs(left_child, cache, new_max_value)

        right_node = current_node.right

        if right_node is not None:
            self.dfs(right_node, cache, new_max_value)