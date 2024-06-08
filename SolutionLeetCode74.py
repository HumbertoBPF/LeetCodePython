from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if (matrix[0][0] == target) or (matrix[m-1][n-1] == target):
            return True

        start = 0
        end = n*m - 1

        while end - start > 1:
            middle = (start + end) //  2
            middle_coordinate = self.translate_index_into_coordinates(middle, n)

            middle_item = matrix[middle_coordinate[0]][middle_coordinate[1]]

            if middle_item == target:
                return True

            if middle_item > target:
                end = middle
                continue

            if middle_item < target:
                start = middle

        return False

    def translate_index_into_coordinates(self, index, n):
        quotient = index // n
        remainder = index % n
        return [quotient, remainder]


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 30
solution = Solution()
print(solution.searchMatrix(matrix, target))
# m = 3, n = 4
# start = 0, end = m*n - 1 = 11
# middle = 11 // 2 = 5
# middle_coordinates = 5 // 4, 5 % 4 = 1, 1
# middle_item = matrix[1][1] = 11 > target = 3 => end = 5
# middle = 5 // 2 = 2
# middle_coordinates = 2 // 4, 2 % 4 = 0, 2
# middle_item = matrix[0][2] = 5 > target = 3 => end = 2
# middle = 2 // 2 = 1
# middle_coordinates = 1 // 4, 1 % 4 = 0, 1
# middle_item = matrix[0][1] = 3 = target
