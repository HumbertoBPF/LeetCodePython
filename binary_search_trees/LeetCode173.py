from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Space complexity: O(h) due to the stack
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = [root]

        current_node = root
        # Start from the node with the minimum value of the BST
        while current_node.left is not None:
            self.stack.append(current_node.left)
            current_node = current_node.left
    # Time complexity: O(1) (average)
    def next(self) -> int:
        popped_node = self.stack.pop()
        current_node = popped_node
        # Search for the inorder successor of the popped node (go right and then full left)
        if current_node.right is not None:
            self.stack.append(current_node.right)
            current_node = current_node.right

            while current_node.left is not None:
                self.stack.append(current_node.left)
                current_node = current_node.left

        return popped_node.val
    # Time complexity: O(1) (average)
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()