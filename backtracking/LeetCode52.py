class Solution:
    # Time complexity: O(n^n)
    # Space complexity: O(n)
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.total = 0
        self.placed_queens = []

        for i in range(n):
            self.place_queen(0, i)

        return self.total

    def place_queen(self, i: int, j: int):
        self.placed_queens.append((i, j))

        if i == self.n - 1:
            self.total += 1
        else:
            forbidden_cols = set()

            for row, col in self.placed_queens:
                delta = i + 1 - row
                forbidden_cols.add(col)
                forbidden_cols.add(col + delta)
                forbidden_cols.add(col - delta)

            for k in range(self.n):
                if k not in forbidden_cols:
                    self.place_queen(i + 1, k)

        self.placed_queens.pop()
