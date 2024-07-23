from typing import List


class Solution:
    # Time complexity: O(n*log n)
    # Space complexity: O(1)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # We need the intervals sorted by the lower bound in order to do the rest of the work in linear time
        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]

        for i in range(1, n):
            interval = intervals[i]
            last_output_interval = output[-1]
            # If the intervals overlap, merge them and replace in the output list
            if self.overlap(interval, last_output_interval):
                output[-1] = self.merge_intervals(interval, last_output_interval)
                continue
            # If they don't overlap, we just append the current interval from the input to the output
            output.append(interval)

        return output

    def merge_intervals(self, interval_1, interval_2):
        # The result of merging two intervals [a, b] and [c, d] is [min(a, c), max(b, d)].
        return [min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1])]

    def overlap(self, interval_1, interval_2):
        # Two intervals [a, b] and [c, d] overlap if a <= c < b or c <= b < d.
        return (
            interval_1[0] <= interval_2[0] <= interval_1[1]
        ) or (
            interval_2[0] <= interval_1[0] <= interval_2[1]
        )
