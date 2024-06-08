import heapq
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Because there are no negative weights, we will use Dijkstra Algorithm to find the minimum delay time
        vertex_distances = self.get_vertex_distances(n, k)
        distance_heap = self.get_distance_heap(n, k)
        visited = set()
        adj = self.get_adjacency_list(times, n)

        while len(visited) < n:
            _, current_vertex = heapq.heappop(distance_heap)
            visited.add(current_vertex)
            current_distance = vertex_distances[current_vertex]

            neighbors = adj[current_vertex]

            for neighbor in neighbors:
                vertex, weight = neighbor
                distance = current_distance + weight

                if distance < vertex_distances[vertex]:
                    vertex_distances[vertex] = distance
                    heapq.heappush(distance_heap, (distance, vertex))

        return self.get_maximum_distance(vertex_distances)

    def get_maximum_distance(self, vertex_distances):
        max_distance = -1

        for vertex in vertex_distances:
            distance = vertex_distances[vertex]

            if distance == sys.maxsize:
                return -1

            if distance > max_distance:
                max_distance = distance

        return max_distance

    def get_distance_heap(self, n, k):
        # Iterate from 1 to n because the vertices labels are 1-indexed
        distances = [(sys.maxsize, i) for i in range(1, n + 1)]
        # Modify the k - 1 item because the list is 0-indexed while the graph vertices are 1-indexed
        distances[k - 1] = (0, k)
        heapq.heapify(distances)
        return distances

    def get_vertex_distances(self, n, k):
        distances = {}
        # Iterate from 1 to n because the vertices labels are 1-indexed
        for i in range(1, n + 1):
            if i == k:
                distances[i] = 0
                continue

            distances[i] = sys.maxsize

        return distances

    def get_adjacency_list(self, times, n):
        adj = {}
        # Iterate from 1 to n because the vertices labels are 1-indexed
        for i in range(1, n + 1):
            adj[i] = set()

        for time in times:
            u, v, w = time
            adj[u].add((v, w))

        return adj


times = [[1,2,1]]
n = 2
k = 2
solution = Solution()
print(solution.networkDelayTime(times, n, k))
