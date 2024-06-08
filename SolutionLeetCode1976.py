import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = self.get_adjacency_list(n, roads)
        times = self.dijkstra(adj)
        dag = self.get_shortest_path_dag(adj, times)
        path_counter = self.get_number_of_paths_to_dst(0, n - 1, dag, {})
        return path_counter % (10**9 + 7)

    def get_shortest_path_dag(self, adj, times):
        n = len(times)

        dag = [[] for _ in range(n)]

        for i in range(n):
            edges = adj[i]
            for edge in edges:
                neighbor_vertex, neighbor_time = edge

                if neighbor_time == times[neighbor_vertex] - times[i]:
                    dag[i].append(neighbor_vertex)

        return dag

    def get_number_of_paths_to_dst(self, vertex, dst, dag, memory):
        n = len(dag)

        if vertex == n - 1:
            return 1

        if vertex in memory:
            return memory[vertex]

        neighbors = dag[vertex]
        counter = 0
        # Exploring neighbors of vertex
        for neighbor in neighbors:
            number_paths_to_dst = self.get_number_of_paths_to_dst(neighbor, dst, dag, memory)
            counter += number_paths_to_dst

        memory[vertex] = counter
        return counter

    def dijkstra(self, adj):
        n = len(adj)
        times = self.get_times(0, n)
        time_heap = self.get_time_heap(0, n)
        visited = set()
        # While we haven’t visited every vertex of the graph
        while len(visited) < n:
            time, vertex = heapq.heappop(time_heap)

            neighbors = adj[vertex]
            visited.add(vertex)

            for neighbor in neighbors:
                neighbor_vertex, time_to_neighbor = neighbor
                updated_time = time + time_to_neighbor

                if updated_time < times[neighbor_vertex]:
                    times[neighbor_vertex] = updated_time
                    if neighbor_vertex not in visited:
                        heapq.heappush(time_heap, (updated_time, neighbor_vertex))
        # This list will contain the smallest time to arrive from vertex 0 to other vertices
        return times

    def get_time_heap(self, src, n):
        # Heap used to get the smallest time that we have computed so far
        time_heap = [(float("inf"), i) for i in range(n)]
        time_heap[src] = (0, src)
        heapq.heapify(time_heap)
        return time_heap

    def get_times(self, src, n):
        # The ith time corresponds to the best distance found from the vertex src to i
        times = [float("inf") for _ in range(n)]
        times[src] = 0
        return times

    def get_adjacency_list(self, n, roads):
        adj = []

        for _ in range(n):
            adj.append(set())

        for road in roads:
            u, v, time = road
            adj[u].add((v, time))
            adj[v].add((u, time))

        return adj


solution = Solution()
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(solution.countPaths(7, roads))
