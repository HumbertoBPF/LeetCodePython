import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int
    ) -> float:
        adj = self.get_adjacency_list(n, edges, succProb)
        probabilities = self.get_probabilities(n, start_node)
        probabilities_heap = self.get_probabilities_heap(n, start_node)
        visited = set()

        while len(visited) < n:
            current_probability, current_node = heapq.heappop(probabilities_heap)

            neighbors = adj[current_node]
            visited.add(current_node)

            for neighbor_node, neighbor_probability in neighbors:
                if neighbor_node not in visited:
                    # The minus here is due to the fact that we store negative probabilities in the heap
                    probability = -current_probability * neighbor_probability
                    # We want to maximize the probability
                    if probability > probabilities[neighbor_node]:
                        probabilities[neighbor_node] = probability
                        # Reverse the sign when storing in the heap
                        heapq.heappush(probabilities_heap, (-probability, neighbor_node))

        return probabilities[end_node]

    def get_adjacency_list(self, n, edges, success_probabilities):
        adj = [set() for _ in range(n)]

        k = len(edges)

        for i in range(k):
            v1, v2 = edges[i]
            success_probability = success_probabilities[i]
            adj[v1].add((v2, success_probability))
            adj[v2].add((v1, success_probability))

        return adj

    def get_probabilities(self, n, start_node):
        probabilities = {}

        for i in range(n):
            probabilities[i] = 0

        probabilities[start_node] = 1
        return probabilities

    def get_probabilities_heap(self, n, start_node):
        # We store the probabilities with negative sign since the built-in heap in Python is a min heap while we
        # want to maximize probabilities (so we need a max heap)
        # The maximum value here is 0 instead of infinity as usual (because of negative values)
        probabilities_heap = [(0, i) for i in range(n)]
        probabilities_heap[start_node] = (-1, start_node)
        heapq.heapify(probabilities_heap)
        return probabilities_heap
