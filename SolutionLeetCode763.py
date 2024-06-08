from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        letter_partitions = {}

        for i in range(n):
            letter = s[i]
            if letter in letter_partitions:
                # Index where the partition containing this letter starts
                letter_interval = letter_partitions[letter]
                letter_partitions[letter] = (letter_interval[0], i)
            else:
                letter_partitions[letter] = (i, i)
        # Merge intervals
        intervals = list(letter_partitions.values())
        nb_intervals = len(intervals)

        merged_intervals = [intervals[0]]

        for i in range(1, nb_intervals):
            lower_bound_previous, upper_bound_previous = merged_intervals[-1]
            lower_bound_current, upper_bound_current = intervals[i]

            if lower_bound_current < upper_bound_previous:
                merged_intervals[-1] = (
                    min(lower_bound_previous, lower_bound_current),
                    max(upper_bound_previous, upper_bound_current)
                )
            else:
                merged_intervals.append((lower_bound_current, upper_bound_current))
        # Getting list with the interval lengths
        return [(interval[1] - interval[0] + 1) for interval in merged_intervals]


solution = Solution()
s = "ababcbacadefegdehijhklij"
print(solution.partitionLabels(s))
