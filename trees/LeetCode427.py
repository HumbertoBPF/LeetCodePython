from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        n = len(grid)
        return self.construct_sub_tree(0, n - 1, 0, n - 1)

    def construct_sub_tree(self, start_row, end_row, start_col, end_col):
        same_value = True
        first_value = self.grid[start_row][start_col]

        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if self.grid[i][j] != first_value:
                    same_value = False
                    break

        if same_value:
            return Node(first_value, True, None, None, None, None)

        root_node = Node(1, False, None, None, None, None)

        delta = end_row - start_row + 1
        mid_row = start_row + delta//2 - 1
        mid_col = start_col + delta//2 - 1

        root_node.topLeft = self.construct_sub_tree(start_row, mid_row, start_col, mid_col)
        root_node.topRight = self.construct_sub_tree(start_row, mid_row, mid_col + 1, end_col)
        root_node.bottomLeft = self.construct_sub_tree(mid_row + 1, end_row, start_col, mid_col)
        root_node.bottomRight = self.construct_sub_tree(mid_row + 1, end_row, mid_col + 1, end_col)

        return root_node


solution = Solution()
grid = [[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]]
print(solution.construct(grid))
