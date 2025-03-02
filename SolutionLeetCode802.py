from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = set()
        unsafe_nodes = set()

        for i in range(n):
            if i not in visited:
                self.has_cycle(i, graph, set(), visited, unsafe_nodes)

        safe_nodes = []

        for i in range(n):
            if i not in unsafe_nodes:
                safe_nodes.append(i)

        return safe_nodes

    def has_cycle(self, vertex, adj, path, visited, unsafe_nodes):
        """
        Uses DFS to detect cycles in the specified graph.
        :param vertex: current vertex
        :param adj: adjacency list representation of the graph
        :param path: path being explored
        :param visited: visited vertices
        :param unsafe_nodes: unsafe vertices detected so far (vertices that lead to a cycle)
        :return: a boolean indicating if the current vertex is safe
        """
        # We found a cycle
        if vertex in path:
            unsafe_nodes.add(vertex)
            return True
        # If vertex has already been visited, we don’t need to explore it
        if vertex in visited:
            return False

        visited.add(vertex)

        neighbors = adj[vertex]

        path.add(vertex)

        for neighbor in neighbors:
            if neighbor in unsafe_nodes:
                unsafe_nodes.add(vertex)
                return True
            # If some neighbor leads to a cycle, the current vertex is unsafe
            if self.has_cycle(neighbor, adj, path, visited, unsafe_nodes):
                unsafe_nodes.add(vertex)
                return True

        path.delete(vertex)
        return False


solution = Solution()
print(solution.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
