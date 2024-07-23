class SolutionRecursive:
    # Time complexity: O(n**2)
    # Space complexity: O(n) due to the recursion stack
    def numTilings(self, n: int) -> int:
        cache = [None for _ in range(n + 1)]
        cache[0] = 1
        self.dfs(n, cache)
        return cache[-1] % (10**9 + 7)

    def dfs(self, n, cache):
        # Checking in the cache to check if we've already computed this sub-problem
        if cache[n] is not None:
            return cache[n]
        nb_tilings = 0
        # The last two iterations correspond to the tilings having:
        # - One 2 x 1 vertical domino tile. 2 x (n - 1) board remaining on the left.
        # - Two 2 x 1 domino tiles on the horizontal. 2 x (n - 2) board remaining on the left.
        # The other iterations take into account the two new tilings that we get when we increase the number of
        # columns of a tiling.
        for i in range(0, n):
            nb_tilings += self.dfs(i, cache) * (1 if (i == n - 1) or (i == n - 2) else 2)
        # Memorize the result to avoid redundant computations
        cache[n] = nb_tilings
        return nb_tilings


class SolutionIterative:
    # Time complexity: O(n)
    # Space complexity: O(n) due to the recursion stack
    def numTilings(self, n: int) -> int:
        cache = [None for _ in range(n + 1)]
        cache[0] = 1
        self.dfs(n, cache)
        return cache[-1] % (10**9 + 7)

    def dfs(self, n, cache):
        # Checking in the cache to check if we've already computed this sub-problem
        if cache[n] is not None:
            return cache[n]
        nb_tilings = 0
        # The last two iterations correspond to the tilings having:
        # - One 2 x 1 vertical domino tile. 2 x (n - 1) board remaining on the left.
        # - Two 2 x 1 domino tiles on the horizontal. 2 x (n - 2) board remaining on the left.
        # The other iterations take into account the two new tilings that we get when we increase the number of
        # columns of a tiling.
        for i in range(0, n):
            nb_tilings += self.dfs(i, cache) * (1 if (i == n - 1) or (i == n - 2) else 2)
        # Memorize the result to avoid redundant computations
        cache[n] = nb_tilings
        return nb_tilings
