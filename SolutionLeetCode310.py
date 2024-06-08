from collections import deque
from typing import List


class SolutionDfs:
    # Time complexity: O(V*(V + E))
    # Space complexity: O(V + E)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # O(V + E) time complexity
        # O(V + E) space complexity
        adj = self.get_adjacency_list(n, edges)
        # O(V) space complexity
        depths = [0]*n
        min_depth = float("inf")
        # O(V*(V + E)) time complexity - doing DFS V times
        for vertex in range(n):
            memory = {"max_depth": 0, "depth": 0}
            self.dfs(vertex, adj, set(), memory)
            depths[vertex] = memory["max_depth"]
            min_depth = min(min_depth, memory["max_depth"])
        # O(V) space complexity
        max_height_trees = []
        # O(V) time complexity
        for vertex in range(n):
            if depths[vertex] == min_depth:
                max_height_trees.append(vertex)

        return max_height_trees

    def dfs(self, vertex, adj, visited, memory):
        if vertex in visited:
            memory["max_depth"] = max(memory["max_depth"], memory["depth"])
            return

        neighbors = adj[vertex]
        visited.add(vertex)

        memory["depth"] += 1
        for neighbor in neighbors:
            self.dfs(neighbor, adj, visited, memory)
        memory["depth"] -= 1

    def get_adjacency_list(self, n, edges):
        adj = {}

        for vertex in range(n):
            adj[vertex] = set()

        for edge in edges:
            v1, v2 = edge
            adj[v1].add(v2)
            adj[v2].add(v1)

        return adj

class SolutionTopologicalSorting:
    # Time complexity: O(V + E) = O(n) since V = n and E = n - 1
    # Space complexity: O(V + E) = O(n) since V = n and E = n - 1
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # O(V + E) time and space complexity
        adj = self.get_adjacency_list(n, edges)
        # O(V) space complexity
        in_degree = [0]*n
        # O(V + E) time complexity
        for i in range(n):
            for j in adj[i]:
                in_degree[j] += 1

        queue = deque()
        # O(V) time complexity
        for i in range(n):
            # Start from the leaves
            if in_degree[i] == 1:
                queue.append(i)
        # We track the visited nodes to avoid visiting them again (since the graph is undirected, this risk exists)
        # O(V) space complexity
        visited = set()
        # O(V + E) time complexity
        # We always have 1 or 2 MHTs
        while n - len(visited) > 2:
            # Number of vertices remaining in the queue
            k = len(queue)

            for _ in range(k):
                vertex = queue.popleft()
                visited.add(vertex)

                neighbors = adj[vertex]

                for neighbor in neighbors:
                    # Removing vertex from the in
                    in_degree[neighbor] -= 1
                    # Add vertices to the queue as soon as they become leaves
                    if (neighbor not in visited) and (in_degree[neighbor] == 1):
                        queue.append(neighbor)
        # The remaining non-visited nodes are the roots of Minimum Height Trees
        roots_mht = []
        # O(V) space complexity
        for i in range(n):
            if i not in visited:
                roots_mht.append(i)

        return roots_mht

    def get_adjacency_list(self, n, edges):
        adj = {}

        for vertex in range(n):
            adj[vertex] = set()

        for edge in edges:
            v1, v2 = edge
            adj[v1].add(v2)
            adj[v2].add(v1)

        return adj


solution = SolutionTopologicalSorting()
print(solution.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))
