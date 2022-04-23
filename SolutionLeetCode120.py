class Solution(object):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    def minimumTotal(self, triangle):
        nodes_best_sum = {}
        # Dictionary for memoization
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == len(triangle) - 1:
                    nodes_best_sum[(i, j)] = triangle[i][j]
                else:
                    nodes_best_sum[(i, j)] = None

        return self.best_path_to_node(triangle, 0, 0, nodes_best_sum)

    def best_path_to_node(self, triangle, row, index, nodes_best_sum):
        # If this sub-problem has already been solved, no need to do it again
        if nodes_best_sum[(row, index)] is not None:
            return nodes_best_sum[(row, index)]
        # Check the left and right best paths
        left = self.best_path_to_node(triangle, row+1, index, nodes_best_sum)
        right = self.best_path_to_node(triangle, row+1, index+1, nodes_best_sum)
        # Pick the path with the lower sum
        nodes_best_sum[(row, index)] = min(left, right) + triangle[row][index]

        return nodes_best_sum[(row, index)]


o1 = Solution()
triangle = [[-10]]
print(o1.minimumTotal(triangle))
