# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Edge case: empty graph
        if node is None:
            return None
        return self.dfs(node, {})

    def dfs(self, node, visited_nodes):
        # If a graph node is visited twice, return the copy previously stored in the hash map
        if node.val in visited_nodes:
            return visited_nodes[node.val]

        copied_node = Node(node.val)
        # To avoid visiting the same graph node twice, we store the copy in a hash map
        visited_nodes[node.val] = copied_node

        neighbors = node.neighbors
        copied_neighbors = []

        for neighbor in neighbors:
            copied_neighbor = self.dfs(neighbor, visited_nodes)
            copied_neighbors.append(copied_neighbor)

        copied_node.neighbors = copied_neighbors

        return copied_node