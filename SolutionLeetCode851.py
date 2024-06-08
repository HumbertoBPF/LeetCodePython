from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = self.get_adjacency_list(n, richer)
        output = [-1]*n

        for i in range(n):
            if output[i] == -1:
                self.dfs(i, adj, quiet, output)

        return output

    def dfs(self, vertex, adj, quiet, memory):
        if memory[vertex] != - 1:
            return memory[vertex]

        neighbors = adj[vertex]
        # By default, the least quiet person is the one represented by the current vertex
        # If the vertex doesn't have incoming edges, it means there is no one richer than
        # the person represented by it, and then this person is the least quiet
        least_quiet_person = vertex

        for neighbor in neighbors:
            least_quiet_person_of_neighbor = self.dfs(neighbor, adj, quiet, memory)
            # If the least quiet person of the neighbor is someone quieter than the person represented
            # by least_quiet_person, update the variable least_quiet_person
            if quiet[least_quiet_person_of_neighbor] < quiet[least_quiet_person]:
                least_quiet_person = least_quiet_person_of_neighbor
        # Memoization to avoid redundant computations
        memory[vertex] = least_quiet_person
        return least_quiet_person

    def get_adjacency_list(self, n, richer):
        adj = [set() for _ in range(n)]

        for pair in richer:
            a, b = pair
            # a is richer than b = vertex b points to vertex a
            adj[b].add(a)

        return adj


solution = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(solution.loudAndRich(richer, quiet))
