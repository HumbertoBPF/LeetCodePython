# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors_p = set()
        self.search(root, p.val, ancestors_p)

        cache = { "lca": root }
        self.search_lca(root, q.val, ancestors_p, cache)

        return cache["lca"]

    def search_lca(self, current_node, target, ancestors, cache):
        # We only need to check the common ancestors, so if they start to diverge, stop the search
        if current_node.val not in ancestors:
            return

        cache["lca"] = current_node

        if current_node.val == target:
            return

        if current_node.val < target:
            self.search_lca(current_node.right, target, ancestors, cache)
            return

        self.search_lca(current_node.left, target, ancestors, cache)

    def search(self, current_node, target, ancestors):
        ancestors.add(current_node.val)

        if current_node.val == target:
            return

        if current_node.val < target:
            self.search(current_node.right, target, ancestors)
            return

        self.search(current_node.left, target, ancestors)
