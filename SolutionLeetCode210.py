from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = self.get_adjacency_list(numCourses, prerequisites)
        prerequisites_map = self.get_prerequisites_map(numCourses, prerequisites)

        taken = set()
        courses_ordering = []

        for course in range(numCourses):
            # The starting point are courses with no prerequisites
            if len(prerequisites_map.get(course)) == 0:
                # If some cycle is detected, then it's not possible to take all courses and we return []
                if self.has_cycle(course, adj, prerequisites_map, taken, set(), courses_ordering):
                    return []
        # If some course has not been taken, it means that it's not possible to take all courses, and then we return []
        if len(taken) != numCourses:
            return []

        return courses_ordering

    def get_adjacency_list(self, n, prerequisites):
        adj = [[] for _ in range(n)]

        for item in prerequisites:
            course = item[0]
            prerequisite = item[1]
            adj[prerequisite].append(course)

        return adj

    def get_prerequisites_map(self, n, prerequisites):
        prerequisites_map = {}

        for i in range(n):
            prerequisites_map[i] = set()

        for item in prerequisites:
            course = item[0]
            prerequisite = item[1]
            prerequisites_map[course].add(prerequisite)

        return prerequisites_map

    def has_cycle(self, current_course, adj, prerequisites_map, taken, path, courses_ordering):
        # If the current node has already been visited in the DFS path, we have found a cycle
        if current_course in path:
            return True
        # If we have already visited the current node and the recursion didn't exit, there is no cycle from this node
        if current_course in taken:
            return False

        taken.add(current_course)
        courses_ordering.append(current_course)

        neighbors = adj[current_course]

        for neighbor in neighbors:
            # Remove the current course from the list of prerequisites of the current neighbor since it was just taken
            prerequisites_map[neighbor].remove(current_course)
            # We just move to a course if all prerequisites have already been taken
            if len(prerequisites_map[neighbor]) == 0:
                path.add(current_course)
                if self.has_cycle(neighbor, adj, prerequisites_map, taken, path, courses_ordering):
                    return True
                path.remove(current_course)

        return False


numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))
