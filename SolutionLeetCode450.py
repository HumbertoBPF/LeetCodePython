from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(log n)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Empty BST
        if root is None:
            return root

        node_to_delete, parent_node = self.search(root, None, key)
        # If the node is not found in the BST, there is nothing to be done
        if node_to_delete is None:
            return root

        if (node_to_delete.left is None) and (node_to_delete.right is None):
            # If the parent node is not None, we need to clear the reference to the node to be deleted
            if parent_node is not None:
                if (parent_node.right is not None) and (parent_node.right.val == node_to_delete.val):
                    parent_node.right = None

                if (parent_node.left is not None) and (parent_node.left.val == node_to_delete.val):
                    parent_node.left = None

                return root
            # If the parent node is None, then the node to be deleted is the root and this is a one node BST
            return None
        # Node to delete has only the right child
        if (node_to_delete.left is None) and (node_to_delete.right is not None):
            if parent_node is not None:
                if (parent_node.right is not None) and (parent_node.right.val == node_to_delete.val):
                    parent_node.right = node_to_delete.right
                    node_to_delete.right = None

                if (parent_node.left is not None) and (parent_node.left.val == node_to_delete.val):
                    parent_node.left = node_to_delete.right
                    node_to_delete.right = None

                return root
            # If the parent node is None, then we are deleting the root and its unique child must be the new root
            return node_to_delete.right
        # Node to delete has only the left child
        if (node_to_delete.left is not None) and (node_to_delete.right is None):
            if parent_node is not None:
                if (parent_node.right is not None) and (parent_node.right.val == node_to_delete.val):
                    parent_node.right = node_to_delete.left
                    node_to_delete.left = None

                if (parent_node.left is not None) and (parent_node.left.val == node_to_delete.val):
                    parent_node.left = node_to_delete.left
                    node_to_delete.left = None

                return root
            # If the parent node is None, then we are deleting the root and its unique child must be the new root
            return node_to_delete.left
        # The case below matches the case where the node to be deleted has two children
        node_to_delete.val = self.delete_in_order_successor(root, node_to_delete)
        return root

    def delete_in_order_successor(self, root, node):
        current_node = node.right

        while current_node.left is not None:
            current_node = current_node.left

        self.deleteNode(root, current_node.val)
        return current_node.val

    def search(self, current_node, parent_node, target):
        if current_node.val == target:
            return current_node, parent_node

        if target < current_node.val:
            left_child = current_node.left

            if left_child is not None:
                return self.search(left_child, current_node, target)

        if target > current_node.val:
            right_child = current_node.right

            if right_child is not None:
                return self.search(right_child, current_node, target)

        return None, None
