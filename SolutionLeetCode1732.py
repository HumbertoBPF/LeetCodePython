from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        current_altitude = 0
        max_altitude = 0

        for i in range(n):
            current_altitude += gain[i]
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
