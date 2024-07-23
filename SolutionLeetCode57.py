from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) if we consider the output, O(1) otherwise
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        merged_interval = newInterval

        for interval in intervals:
            # For the non-overlapping intervals, we add them to the list
            if not self.overlap(interval, merged_interval):
                output.append(interval)
                continue
            # While the intervals overlap, we merge them
            merged_interval = self.merge(interval, merged_interval)

        tmp = merged_interval
        n = len(output)
        # Shifting the output list to add the overlapping interval
        for i in range(n):
            output_interval = output[i]

            if tmp[0] < output_interval[0]:
                output[i] = tmp
                tmp = output_interval

        output.append(tmp)

        return output

    def merge(self, interval_1, interval_2):
        # Let [a, b] and [c, d] be two overlapping interval. Merging them results in [min(a, c), max(b, d)]
        return [min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1])]

    def overlap(self, interval_1, interval_2):
        # Let [a, b] and [c, d] be two intervals. They overlap if a <= c <= b or c <= b <= d.
        return (interval_1[0] <= interval_2[0] <= interval_1[1]) or (interval_2[0] <= interval_1[0] <= interval_2[1])