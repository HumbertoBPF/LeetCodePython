from collections import deque
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        queue = deque()
        visited = set()

        queue.append((0, 0))
        visited.add(0)

        while len(queue) > 0:
            pos, depth = queue.popleft()

            max_pos = min(pos + 6, n ** 2 - 1)

            for i in range(pos + 1, max_pos + 1):
                shortcut_dest = self.get_shortcut_dest(i, board)

                next_pos = i if (shortcut_dest == -1) else shortcut_dest - 1
                # Avoiding getting stuck in a loop
                if next_pos in visited:
                    continue
                # Checking if the next position is the end of the board
                if next_pos == n ** 2 - 1:
                    return depth + 1

                queue.append((next_pos, depth + 1))
                visited.add(next_pos)

        return -1

    def get_shortcut_dest(self, i: int, board: List[List[int]]):
        n = len(board)

        j = i // n
        k = i % n

        if j % 2 == 0:
            return board[n - 1 - j][k]

        return board[n - 1 - j][n - 1 - k]
