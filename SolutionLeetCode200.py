from typing import List


class SolutionGraphModeling:
    # Time complexity: O(m x n)
    # Space complexity: O(m x n)
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = self.get_adjacency_list(grid)

        visited_nodes = set()
        number_islands = 0

        for node in adj:
            if node not in visited_nodes:
                self.dfs(node, adj, visited_nodes)
                number_islands += 1

        return number_islands
    # Time complexity: O(m x n)
    # Space complexity: O(m x n)
    def get_adjacency_list(self, grid):
        """
        Get adjacency list of the graph that represents the island grid. Instead of a list, we use a hash map to
        ignore places with water easier.
        """
        m = len(grid)
        n = len(grid[0])

        adj = {}

        for i in range(m):
            for j in range(n):
                index = self.get_label(i, j, grid)

                if grid[i][j] == "1":
                    neighbors = set()

                    if (j - 1 >= 0) and (grid[i][j - 1] == "1"):
                        neighbors.add(self.get_label(i, j - 1, grid))

                    if (j + 1 < n) and (grid[i][j + 1] == "1"):
                        neighbors.add(self.get_label(i, j + 1, grid))

                    if (i - 1 >= 0) and (grid[i - 1][j] == "1"):
                        neighbors.add(self.get_label(i - 1, j, grid))

                    if (i + 1 < m) and (grid[i + 1][j] == "1"):
                        neighbors.add(self.get_label(i + 1, j, grid))

                    adj[index] = neighbors

        return adj
    # Time complexity: O(m x n)
    # Space complexity: O(m x n)
    def dfs(self, current_node, adj, visited_nodes):
        """
        Visits all nodes accessible from the current node.
        """
        if current_node in visited_nodes:
            return

        visited_nodes.add(current_node)
        neighbors = adj[current_node]

        for neighbor in neighbors:
            self.dfs(neighbor, adj, visited_nodes)

    def get_label(self, i, j, grid):
        n = len(grid[0])
        return n*i + j


class Solution:
    # Time complexity: O(m x n)
    # Space complexity: O(1)
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        number_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    number_islands += 1
                    self.dfs(i, j, grid)

        return number_islands
    def dfs(self, i, j, grid):
        """
        Visits all nodes accessible from the current node.
        """
        m = len(grid)
        n = len(grid[0])
        # Checking if indices are on the boundaries of the matrix
        if (i < 0) or (i >= m) or (j < 0) or (j >= n):
            return
        # If the current node is not a neighbor (value = 0) or if it has already been visited (value = -1)
        if grid[i][j] != "1":
            return
        # Set the current position to -1 to indicate it has already been visited
        grid[i][j] = -1
        # Trying to visit the item above
        self.dfs(i, j - 1, grid)
        # Trying to visit the item below
        self.dfs(i, j + 1, grid)
        # Trying to visit the item on the left
        self.dfs(i - 1, j, grid)
        # Trying to visit the item on the right
        self.dfs(i + 1, j, grid)
