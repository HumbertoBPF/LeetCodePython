from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        self.target = target

        m = len(matrix)
        n = len(matrix[0])

        if (m == 1) and (n == 1):
            return matrix[0][0] == target

        return self.two_dimensional_binary_search((0, 0), (m - 1, n - 1))

    def is_in_boundaries(self, coord):
        m = len(self.matrix)
        n = len(self.matrix[0])
        return (0 <= coord[0] <= m - 1) and (0 <= coord[1] <= n - 1)

    def two_dimensional_binary_search(self, top_left, bottom_right):
        if (not self.is_in_boundaries(top_left)) or (not self.is_in_boundaries(bottom_right)):
            return False

        start = top_left
        end = bottom_right

        if (self.target < self.matrix[start[0]][start[1]]) or (self.target > self.matrix[end[0]][end[1]]):
            return False

        if self.matrix[start[0]][start[1]] == self.target:
            return True

        if self.matrix[end[0]][end[1]] == self.target:
            return True

        while (end[0] - start[0] > 1) or (end[1] - start[1] > 1):
            mid_row = (start[0] + end[0]) // 2
            mid_col = (start[1] + end[1]) // 2

            mid_item = self.matrix[mid_row][mid_col]

            if mid_item == self.target:
                return True

            if mid_item > self.target:
                end = mid_row, mid_col
                continue

            start = mid_row, mid_col

        return self.two_dimensional_binary_search(
            (top_left[0], start[1] + 1),
            (start[0], bottom_right[1])
        ) or self.two_dimensional_binary_search(
            (end[0], top_left[1]),
            (bottom_right[0], end[1] - 1)
        )

matrix = [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
solution = Solution()
print(solution.searchMatrix(matrix, 8))