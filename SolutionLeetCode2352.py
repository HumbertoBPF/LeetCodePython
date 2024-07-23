from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        frequency_columns = {}
        frequency_rows = {}
        # Compute rows and store how many times each one appears
        for i in range(n):
            row = ""

            for j in range(n):
                row += str(grid[i][j])
                row += ","

            if row not in frequency_rows:
                frequency_rows[row] = 0
            frequency_rows[row] += 1
        # Compute columns and store how many times each one appears
        for i in range(n):
            column = ""

            for j in range(n):
                column += str(grid[j][i])
                column += ","

            if column not in frequency_columns:
                frequency_columns[column] = 0
            frequency_columns[column] += 1

        number_equal_pairs = 0
        # Check for rows that match columns and compute the number of equal pairs
        for row in frequency_rows:
            if row in frequency_columns:
                number_equal_pairs += frequency_rows[row]*frequency_columns[row]

        return number_equal_pairs
