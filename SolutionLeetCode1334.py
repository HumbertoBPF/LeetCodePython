import heapq
import sys
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = self.get_adjacency_list(n, edges)
        searched_city = (None, sys.maxsize)

        for i in range(n):
            nb_neighbors_in_threshold_dist = self.dijkstra(i, n, adj, distanceThreshold)

            if nb_neighbors_in_threshold_dist <= searched_city[1]:
                searched_city = (i, nb_neighbors_in_threshold_dist)

        return searched_city[0]

    def dijkstra(self, src, n, adj, distance_threshold):
        distances = self.get_distances(src, n)
        distances_heap = self.get_distances_heap(src, n)
        visited = set()

        while len(visited) < len(adj):
            current_distance, current_vertex = heapq.heappop(distances_heap)

            visited.add(current_vertex)
            neighbors = adj[current_vertex]

            for neighbor in neighbors:
                neighbor_vertex, neighbor_weight = neighbor
                updated_distance = current_distance + neighbor_weight

                if updated_distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = updated_distance
                    if neighbor_vertex not in visited:
                        heapq.heappush(distances_heap, (updated_distance, neighbor_vertex))

        nb_neighbors_in_threshold_dist = 0

        for city in distances:
            distance = distances[city]
            if distance <= distance_threshold:
                nb_neighbors_in_threshold_dist += 1

        return nb_neighbors_in_threshold_dist

    def get_distances(self, src, n):
        distances = {}

        for i in range(n):
            distances[i] = sys.maxsize

        distances[src] = 0
        return distances

    def get_distances_heap(self, src, n):
        distances_heap = []

        for i in range(n):
            distances_heap.append((sys.maxsize, i))

        distances_heap[src] = (0, src)
        heapq.heapify(distances_heap)
        return distances_heap

    def get_adjacency_list(self, n, edges):
        adj = []

        for i in range(n):
            adj.append(set())

        for edge in edges:
            v1, v2, weight = edge
            adj[v1].add((v2, weight))
            adj[v2].add((v1, weight))

        return adj


solution = Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distance_threshold = 4
print(solution.findTheCity(n, edges, distance_threshold))
