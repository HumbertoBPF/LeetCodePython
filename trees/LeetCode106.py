from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n) due to the time to build the "inorder_map"
    # Space complexity: O(n) due to the auxiliar hash map "inorder_map"
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder

        n = len(inorder)
        # We map the values of the inorder list into their corresponding indices to speed up things
        self.inorder_map = self.get_inorder_map()

        return self.divide_and_conquer(0, n - 1, 0, n - 1)

    def get_inorder_map(self):
        inorder_map = {}

        n = len(self.inorder)

        for i in range(n):
            val = self.inorder[i]
            inorder_map[val] = i

        return inorder_map
    # Time complexity: O(log n)
    # Space complexity: O(log n) due to the recursion stack
    def divide_and_conquer(self, inorder_start, inorder_end, postorder_start, postorder_end):
        # Condition that indicates that there is nowhere to go (there is no child on this direction)
        if inorder_start > inorder_end:
            return None
        # The end of the postorder list is the head of a subtree
        head_val = self.postorder[postorder_end]
        # Find the index of this node on the inorder list
        head_index = self.inorder_map[head_val]
        head = TreeNode(head_val)
        # The nodes that come before the head node in the inorder list are the nodes of the left subtree
        nb_nodes_on_left = head_index - 1 - inorder_start
        head.left = self.divide_and_conquer(
            inorder_start,
            head_index - 1,
            # Take "nb_nodes_on_left" first items of the postorder list (these are the nodes of the left subtree)
            postorder_start,
            postorder_start + nb_nodes_on_left
        )
        # The nodes that come after the head node in the inorder list are the nodes of the right subtree
        nb_nodes_on_right = inorder_end - (head_index + 1)
        head.right = self.divide_and_conquer(
            head_index + 1,
            inorder_end,
            # Take "nb_nodes_on_right" first items of the postorder list (these are the nodes of the right subtree)
            (postorder_end - 1) - nb_nodes_on_right,
            postorder_end - 1
        )

        return head
