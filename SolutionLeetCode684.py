from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = self.get_adjacency_list(edges)
        cycle_path = {}
        cycle_vertex = self.find_cycle(1, None, adj, set(), cycle_path)
        # We will store the edges in a set in order to optimize the search in the input list of edges
        cycle_edges = self.get_cycle_edges(cycle_vertex, cycle_path)
        # Returning the edge that is part of the cycle that we find last in the input list of edges
        for i in range(n):
            edge = edges[n - i - 1]
            v1, v2 = edge
            if ((v1, v2) in cycle_edges) or ((v2, v1) in cycle_edges):
                return edge
        # This return should never be reached in the context of the problem
        return []

    def get_adjacency_list(self, edges):
        """
        Builds an adjacency list from a list of graph edges
        :param edges: list of edges of the graph
        :return: the corresponding adjacency list (0-indexed)
        """
        n = len(edges)

        adjacency_list = [[] for _ in range(n)]

        for i, j in edges:
            # We have to subtract one because the nodes are 1-indexed
            adjacency_list[i - 1].append(j)
            adjacency_list[j - 1].append(i)

        return adjacency_list

    def find_cycle(self, vertex, last_vertex, adj, visited, path):
        """
        Uses DFS to search for a cycle in the graph.
        :param vertex: vertex where we are at the current iteration
        :param last_vertex: vertex of the previous recursive call
        :param adj: graph's adjacency list
        :param visited: graph nodes that have already been visited
        :param path: current DFS path
        :return: the vertex of the graph where the cycle starts
        """
        # If the current vertex has already been visited in this DFS path, we found the cycle
        if vertex in path:
            return vertex

        if vertex in visited:
            return

        visited.add(vertex)

        neighbors = adj[vertex - 1]

        for neighbor in neighbors:
            # This condition avoids the detection of the last binding the last vertex and the current one as a cycle
            if neighbor != last_vertex:
                # Path is a dict such that the keys are the cycle vertices and the values are the associated edges
                path[vertex] = (vertex, neighbor)
                cycle_vertex = self.find_cycle(neighbor, vertex, adj, visited, path)
                if cycle_vertex is not None:
                    return cycle_vertex
                del path[vertex]

    def get_cycle_edges(self, cycle_vertex, cycle_path):
        """
        :param cycle_vertex: The vertex where the cycle starts
        :param cycle_path: The DFS path that lead to the cycle
        :return: the list of edges that compose the cycle found in the graph.
        """
        cycle_edges = set()

        next_vertex = cycle_vertex

        while True:
            edge = cycle_path[next_vertex]
            cycle_edges.add(edge)
            next_vertex = cycle_path.get(next_vertex)[1]

            if next_vertex == cycle_vertex:
                break

        return cycle_edges


solution = Solution()
edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
print(solution.findRedundantConnection(edges))