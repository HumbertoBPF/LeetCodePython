# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTreeBfs(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        map_in_order = {}

        for i in range(0, n):
            val = inorder[i]
            map_in_order[val] = i

        current_layer = []
        preorder_index = 0

        head = None
        current_layer.append((None, None, 0, n - 1))

        while len(current_layer) != 0:
            previous_node, previous_node_index, start_index, end_index = current_layer.pop()

            current_value = preorder[preorder_index]
            current_index = map_in_order.get(current_value)
            current_node = TreeNode(current_value)
            # Binding the current node to previous node based on their indices
            if previous_node is not None:
                if current_index < previous_node_index:
                    previous_node.left = current_node

                if current_index > previous_node_index:
                    previous_node.right = current_node
            # There are nodes on the right
            if current_index != end_index:
                current_layer.append((current_node, current_index, current_index + 1, end_index))
            # There are nodes on the left
            if current_index != start_index:
                current_layer.append((current_node, current_index, start_index, current_index - 1))
            # Getting the head at the first iteration
            if previous_node is None:
                head = current_node

            preorder_index += 1

        return head

    def buildTreeDfs(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        map_in_order = {}

        for i in range(0, n):
            val = inorder[i]
            map_in_order[val] = i

        return self.divide_and_conquer(preorder, inorder, map_in_order, 0, n - 1)


    def divide_and_conquer(self, preorder, inorder, map_in_order, start_in_order, end_in_order):
        if start_in_order == end_in_order:
            value = inorder[end_in_order]
            return TreeNode(value)

        head_value = None

        for item in preorder:
            in_order_index = map_in_order.get(item)
            if (in_order_index is not None) and (start_in_order <= in_order_index <= end_in_order):
                head_value = item
                break

        head_index = map_in_order.get(head_value)

        head_node = TreeNode(head_value)

        left_child = None

        if head_index != start_in_order:
            left_child = self.divide_and_conquer(preorder, inorder, map_in_order, start_in_order, head_index - 1)

        right_child = None

        if head_index != end_in_order:
            right_child = self.divide_and_conquer(preorder, inorder, map_in_order, head_index + 1, end_in_order)

        head_node.left = left_child
        head_node.right = right_child

        return head_node

preorder = [3,1,2,4]
inorder = [1,2,3,4]
solution = Solution()
head = solution.buildTreeBfs(preorder, inorder)
print(head.val)
print(head.left.val)
print(head.left.right.val)
print(head.right.val)

# preorder = [3, 1, 2, 4]
# inorder = [1, 2, 3, 4]

# head = 3

# left_subtree = [1, 2]
# right_subtree = [4]

# left_child = [1]

# left_subtree = []
# right_subtree = [2]

# right_child

# right_child = []
