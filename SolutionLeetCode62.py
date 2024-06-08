class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.factorial(m + n - 2) / (self.factorial(n - 1)*self.factorial(m - 1)))

    def factorial(self, n):
        acc = 1

        for i in range(2, n + 1):
            acc *= i

        return acc