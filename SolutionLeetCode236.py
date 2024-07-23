class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS path needed to reach the nodes with value p and q
        path_p = []
        path_q = []

        self.dfs(root, p.val, path_p)
        self.dfs(root, q.val, path_q)

        min_depth = min(len(path_p), len(path_q))

        lowest_common_ancestor = None

        for i in range(min_depth):
            node_p = path_p[i]
            node_q = path_q[i]
            # Find the last common node between the two DFS paths
            if node_p.val == node_q.val:
                lowest_common_ancestor = node_p

        # This line of code should never be reached because both nodes exist in the tree
        return lowest_common_ancestor

    def dfs(self, current_node, target, path):
        # Checking if we've reached a leaf
        if current_node is None:
            return

        path.append(current_node)
        # If the target value is found, we stop the search
        if current_node.val == target:
            return

        self.dfs(current_node.left, target, path)
        # Checking if we've already found the target node
        if (len(path) > 0) and (path[-1].val == target):
            return

        self.dfs(current_node.right, target, path)
        # Checking if we've already found the target node
        if (len(path) > 0) and (path[-1].val == target):
            return

        path.pop()
