from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = self.get_adjacency_list(numCourses, prerequisites)
        # The set at the ith position corresponds to the prerequisites of the course i
        memory = [set() for _ in range(numCourses)]

        for course in range(numCourses):
            # Can use DFS or BFS here
            self.dfs(course, adj, memory)

        output = []

        for query in queries:
            u, v = query
            output.append(u in memory[v])

        return output

    def bfs(self, src, adj, memory):
        queue = deque()
        to_visit = set()

        queue.append(src)
        to_visit.add(src)

        while len(queue) > 0:
            vertex = queue.popleft()

            neighbors = adj[vertex]

            for neighbor in neighbors:
                if neighbor not in to_visit:
                    memory[src].add(neighbor)
                    queue.append(neighbor)
                    to_visit.add(neighbor)

    def dfs(self, vertex, adj, memory):
        if len(memory[vertex]) != 0:
            return memory[vertex]

        neighbors = adj[vertex]
        prerequisites = set()

        for neighbor in neighbors:
            prerequisites.add(neighbor)
            prerequisites_of_neighbor = self.dfs(neighbor, adj, memory)
            prerequisites.update(prerequisites_of_neighbor)

        memory[vertex] = prerequisites
        return prerequisites

    def get_adjacency_list(self, n, prerequisites):
        adj = [set() for _ in range(n)]

        for prerequisite in prerequisites:
            # b has a as a prerequisite
            a, b = prerequisite
            adj[b].add(a)

        return adj


solution = Solution()
numCourses = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))
