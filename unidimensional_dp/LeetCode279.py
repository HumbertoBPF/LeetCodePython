import sys


class Solution:
    # Time complexity: O(n^(3/2))
    # Space complexity: O(n)
    def numSquares(self, n: int) -> int:
        # Array for tabulation
        self.cache = [0] * (n + 1)
        self.cache[1] = 1

        for i in range(2, n + 1):
            min_num_squares = sys.maxsize

            for j in range(1, n):
                if j ** 2 > i:
                    break

                min_num_squares = min(min_num_squares, 1 + self.cache[i - j ** 2])

            self.cache[i] = min_num_squares

        return self.cache[-1]


class SolutionRecursive:
    # Time complexity: O(n^(3/2))
    # Space complexity: O(n)
    def numSquares(self, n: int) -> int:
        # Array for memoization
        self.cache = [0]*(n + 1)
        return self.dfs(n)

    def dfs(self, n: int) -> int:
        if n == 0:
            return 0
        # Check if we have already processed this value
        if self.cache[n] != 0:
            return self.cache[n]

        num_squares = sys.maxsize

        for i in range(1, 101):
            if i**2 > n:
                break

            num_squares = min(num_squares, 1 + self.dfs(n - i ** 2))
        # Cache the result of the computation
        self.cache[n] = num_squares
        return num_squares

solution = SolutionRecursive()
print(solution.numSquares(12))
