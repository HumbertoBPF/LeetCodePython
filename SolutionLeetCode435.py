from typing import List


class Solution:
    # Time complexity: O(n*log n) due to the initial sorting
    # Space complexity: O(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        previous_interval = intervals[0]
        min_erased_intervals = 0

        for i in range(1, n):
            interval = intervals[i]
            # In case of overlap, delete the interval with the greater upper bound
            if self.overlap(interval, previous_interval):
                min_erased_intervals += 1
                # If the interval pointed by previous_interval is deleted, set previous_interval to the kept interval
                if previous_interval[1] > interval[1]:
                    previous_interval = interval
                continue
            # If the intervals don't overlap, cache the interval seen last
            previous_interval = interval

        return min_erased_intervals

    def overlap(self, interval_1, interval_2):
        # Two intervals [a, b] and [c, d] overlap if a <= c < b or c <= a < d
        return (
            (interval_1[0] <= interval_2[0] < interval_1[1]) or
            (interval_2[0] <= interval_1[0] < interval_2[1])
        )
