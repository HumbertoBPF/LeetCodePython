from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        results = []
        adj = self.get_adjacency_list(equations, values)

        for query in queries:
            origin, destination = query
            # Unknown term (that is not in the graph) appeared
            if (origin not in adj) or (destination not in adj):
                results.append(-1)
                continue
            # Division of a coefficient by itself
            if origin == destination:
                results.append(1)
                continue

            cache = {"acc": 1}
            if self.dfs(origin, destination, adj, set(), cache):
                results.append(cache["acc"])
            else:
                results.append(-1)

        return results

    def get_adjacency_list(self, equations, values):
        adj = {}
        n = len(equations)

        for i in range(n):
            equation = equations[i]
            c1, c2 = equation
            value = values[i]
            # Relationship representing c1/c2 = value
            if c1 not in adj:
                adj[c1] = set()
            adj[c1].add((c2, value))
            # Relationship representing c2/c1 = 1/value
            if c2 not in adj:
                adj[c2] = set()
            adj[c2].add((c1, 1 / value))

        return adj

    def dfs(self, vertex, destination, adj, visited, cache):
        if vertex in visited:
            return False

        if vertex == destination:
            return True

        neighbors = adj[vertex]
        visited.add(vertex)

        for neighbor in neighbors:
            coefficient, weight = neighbor
            # When going from a vertex to another, multiply
            cache["acc"] *= weight
            if self.dfs(coefficient, destination, adj, visited, cache):
                return True
            # When backtracking, divide
            cache["acc"] /= weight

        return False