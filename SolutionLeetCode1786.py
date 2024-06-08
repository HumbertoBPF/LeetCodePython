import heapq
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = self.get_adjacency_list(n, edges)
        # Getting the shortest distance from n to the other vertices
        distances = self.dikstra(adj, n - 1)
        # Use cached DFS to count the restricted paths. The number of restricted paths will be stored as the value of a
        # key -1
        memory = {-1: 0}
        self.dfs(0, n - 1, adj, distances, memory)
        return memory[-1] % (10**9 + 7)

    def dikstra(self, adj, src):
        n = len(adj)
        distances = self.get_distances(src, n)
        distance_heap = self.get_distance_heap(src, n)
        visited = set()

        while len(visited) < n:
            current_distance, vertex = heapq.heappop(distance_heap)

            neighbors = adj[vertex]
            visited.add(vertex)

            for neighbor in neighbors:
                neighbor_vertex, neighbor_weight = neighbor
                distance = current_distance + neighbor_weight
                if distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = distance
                    if neighbor_vertex not in visited:
                        heapq.heappush(distance_heap, (distance, neighbor_vertex))

        return distances

    def dfs(self, vertex, dst, adj, distances, memory):
        # If we reach the destination, we find a new restricted path
        if vertex == dst:
            memory[-1] += 1
            return
        # We use memoization to avoid re-exploring paths
        if vertex in memory:
            memory[-1] += memory[vertex]
            return

        neighbors = adj[vertex]

        counter_before_visiting_vertex = memory[-1]

        for neighbor in neighbors:
            neighbor_vertex, neighbor_weight = neighbor
            # Only visit a neighbor under the restricted path condition
            if distances[vertex] > distances[neighbor_vertex]:
                self.dfs(neighbor_vertex, dst, adj, distances, memory)

        counter_after_visiting_vertex = memory[-1]
        # The difference between the number of restricted paths before exploring the vertex neighbors and after doing
        # so corresponds to the number of restricted paths accessible from it
        memory[vertex] = counter_after_visiting_vertex - counter_before_visiting_vertex

    def get_distance_heap(self, src, n):
        distance_heap = [(float("inf"), i) for i in range(n)]
        distance_heap[src] = (0, src)
        heapq.heapify(distance_heap)
        return distance_heap

    def get_distances(self, src, n):
        distances = [float("inf")]*n
        distances[src] = 0
        return distances

    def get_adjacency_list(self, n, edges):
        adj = [set() for _ in range(n)]

        for edge in edges:
            v1, v2, weight = edge
            adj[v1 - 1].add((v2 - 1, weight))
            adj[v2 - 1].add((v1 - 1, weight))

        return adj