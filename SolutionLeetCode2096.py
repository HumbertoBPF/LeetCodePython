from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        self.in_order_traversal(root, startValue, destValue, path, set())

        if len(path) == 0:
            self.in_order_traversal(root, startValue, destValue, path, set(), reverse=True)

        return self.get_directions_from_path(path)

    def get_directions_from_path(self, path):
        directions = ""

        for direction in path:
            directions += direction

        return directions

    def go_left(self, current_node, start_value, dest_value, path, visited, reverse):
        left_child = current_node.left

        if left_child is not None:
            # Verifies if we are in the path from start_value to dest_value
            if (start_value in visited) and (dest_value not in visited):
                path.append("L")

            self.in_order_traversal(left_child, start_value, dest_value, path, visited, reverse)

            if (start_value in visited) and (dest_value not in visited):
                # It this edge has already been traversed on the opposite direction, remove it from the path
                if len(path) > 0 and path[-1] == "L":
                    path.pop()
                else:
                    path.append("U")

    def go_right(self, current_node, start_value, dest_value, path, visited, reverse):
        right_child = current_node.right

        if right_child is not None:
            # Verifies if we are in the path from start_value to dest_value
            if (start_value in visited) and (dest_value not in visited):
                path.append("R")

            self.in_order_traversal(right_child, start_value, dest_value, path, visited, reverse)

            if (start_value in visited) and (dest_value not in visited):
                # It this edge has already been traversed on the opposite direction, remove it from the path
                if len(path) > 0 and path[-1] == "R":
                    path.pop()
                else:
                    path.append("U")

    def in_order_traversal(self, current_node, start_value, dest_value, path, visited, reverse=False):
        if reverse:
            self.go_right(current_node, start_value, dest_value, path, visited, reverse)
        else:
            self.go_left(current_node, start_value, dest_value, path, visited, reverse)

        visited.add(current_node.val)

        if current_node.val == dest_value:
            return

        if reverse:
            self.go_left(current_node, start_value, dest_value, path, visited, reverse)
        else:
            self.go_right(current_node, start_value, dest_value, path, visited, reverse)


# root = TreeNode(5)
#
# left_child = TreeNode(1)
# root.left = left_child
#
# left_child_1 = TreeNode(3)
# left_child.left = left_child_1
#
# right_child = TreeNode(2)
# root.right = right_child
#
# left_child_2 = TreeNode(6)
# right_child.left = left_child_2
#
# right_child_1 = TreeNode(4)
# right_child.right = right_child_1

# root = TreeNode(3)
#
# left_child = TreeNode(1)
# root.left = left_child
#
# right_child = TreeNode(2)
# root.right = right_child
#
# solution = Solution()
# print(solution.getDirections(root, 2, 1))
