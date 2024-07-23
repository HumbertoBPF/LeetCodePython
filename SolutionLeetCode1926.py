from collections import deque
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) (due to the queue)
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()

        x0, y0 = entrance
        # Adding the initial cell to the queue and mark as visited
        queue.append((x0, y0, 0))
        maze[x0][y0] = "+"

        while len(queue) > 0:
            x, y, depth = queue.popleft()
            # Checking if we are at an exit cell (cell at the border of the maze and that is not the entrance)
            if self.is_at_border(x, y, depth, maze):
                return depth
            # Up neighbor
            self.add_to_queue_if_accessible(x - 1, y, depth, maze, queue)
            # Down neighbor
            self.add_to_queue_if_accessible(x + 1, y, depth, maze, queue)
            # Left neighbor
            self.add_to_queue_if_accessible(x, y - 1, depth, maze, queue)
            # Right neighbor
            self.add_to_queue_if_accessible(x, y + 1, depth, maze, queue,)

        return -1

    def is_at_border(self, x, y, depth, maze):
        n = len(maze)
        m = len(maze[0])
        return (x == 0 or x == n - 1 or y == 0 or y == m - 1) and (depth != 0)

    def add_to_queue_if_accessible(self, x, y, depth, maze, queue):
        n = len(maze)
        m = len(maze[0])
        # Adding the cell to the queue and mark it as visited if it is accessible
        # (it is not a wall and is in the bounds of the maze)
        if (0 <= x <= n - 1) and (0 <= y <= m - 1) and maze[x][y] == ".":
            queue.append((x, y, depth + 1))
            maze[x][y] = "+"
