from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.get_adjacency_list(numCourses, prerequisites)
        courses_with_prerequisite = self.get_courses_without_prerequisites(prerequisites)
        # If all courses hava a prerequisite, it's impossible to find an initial course that will lead to the conclusion of all
        if len(courses_with_prerequisite) == numCourses:
            return False

        visited_nodes = set()

        for i in range(numCourses):
            if i not in courses_with_prerequisite:
                # If a cycle is found, it's impossible to complete all courses in the concerned subgraph
                if self.has_cycle(i, adj, visited_nodes, set()):
                    return False

        return len(visited_nodes) == numCourses

    def get_adjacency_list(self, n, prerequisites):
        adj = [[] for _ in range(n)]

        for item in prerequisites:
            course = item[0]
            prerequisite = item[1]
            adj[prerequisite].append(course)

        return adj

    def get_courses_without_prerequisites(self, prerequisites):
        courses_with_prerequisite = set()

        for item in prerequisites:
            course = item[0]
            courses_with_prerequisite.add(course)

        return courses_with_prerequisite

    def has_cycle(self, current_node, adj, visited_nodes, path):
        """Check for cycles using DFS."""
        # If we visit a node for the second time in a given DFS path, we have found a cycle
        if current_node in path:
            return True
        # If we have already checked a node, and we didn't exit the recursion, it's because this node doesn't lead to cycle
        if current_node in visited_nodes:
            return False

        neighbors = adj[current_node]
        visited_nodes.add(current_node)

        for neighbor in neighbors:
            path.add(current_node)
            if self.has_cycle(neighbor, adj, visited_nodes, path):
                return True
            path.remove(current_node)

        return False


numCourses = 8
prerequisites = [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))