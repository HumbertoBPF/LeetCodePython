from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def trap(self, height: List[int]) -> int:
        self.height = height
        self.n = len(height)

        peaks = self.get_reservoir_peaks()

        nb_peaks = len(peaks)
        total_volume = 0

        for i in range(1, nb_peaks):
            total_volume += self.compute_volume_sub_reservoir(peaks[i - 1], peaks[i])

        return total_volume

    def get_reservoir_peaks(self):
        start_reservoir = self.get_start_of_the_reservoir()
        end_reservoir = self.get_end_of_the_reservoir()

        peaks_start = [start_reservoir]
        peaks_end = [end_reservoir]

        p1 = start_reservoir
        p2 = end_reservoir
        # The peaks inside the reservoir are points for which the height is higher than its extremities
        while p1 < p2:
            if self.height[start_reservoir] < self.height[end_reservoir]:
                if self.height[p1] > self.height[start_reservoir]:
                    peaks_start.append(p1)
                    start_reservoir = p1
                    continue
                p1 += 1
                continue

            if self.height[p2] > self.height[end_reservoir]:
                peaks_end.append(p2)
                end_reservoir = p2
                continue
            p2 -= 1
        # Merge all the peaks in only one array
        while len(peaks_end) > 0:
            peaks_start.append(peaks_end.pop())

        return peaks_start

    def get_start_of_the_reservoir(self):
        start = 0

        for i in range(1, self.n):
            # Wait for a decrement
            if self.height[i - 1] > self.height[i]:
                return i - 1

        return start

    def get_end_of_the_reservoir(self):
        end = self.n - 1

        for i in range(1, self.n):
            j = self.n - 1 - i
            # Wait for a decrement
            if self.height[j + 1] > self.height[j]:
                return j + 1

        return end

    def compute_volume_sub_reservoir(self, p1, p2):
        volume = 0
        # The shorter extremity is the height of the reservoir
        height_reservoir = min(self.height[p1], self.height[p2])

        for i in range(p1 + 1, p2):
            # Use the max operator here since the water is trapped only for heights lower than the reservoir height
            volume += max(0, height_reservoir - self.height[i])

        return volume