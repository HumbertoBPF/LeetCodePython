from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        self.dfs(0, rooms, visited)

        return len(visited) == n


    def dfs(self, room, rooms, visited):
        # Avoiding visiting a node twice in the same recursion stack
        if room in visited:
            return

        visited.add(room)

        neighbors = rooms[room]

        for neighbor in neighbors:
            self.dfs(neighbor, rooms, visited)
