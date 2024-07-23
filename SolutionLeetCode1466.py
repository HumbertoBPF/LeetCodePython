from typing import List


class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.undirected_graph = [set() for _ in range(n)]
        self.directed_graph = [set() for _ in range(n)]

        for connection in connections:
            src, dst = connection

            self.undirected_graph[src].add(dst)
            self.undirected_graph[dst].add(src)

            self.directed_graph[src].add(dst)

        self.visited = set()
        self.number_reorders = 0

        self.dfs(0)

        return self.number_reorders

    def dfs(self, current_node):
        self.visited.add(current_node)

        neighbors = self.undirected_graph[current_node]

        for neighbor in neighbors:
            if neighbor not in self.visited:
                # Checking if this edge needs to be reversed
                if neighbor in self.directed_graph[current_node]:
                    self.number_reorders += 1

                self.dfs(neighbor)
