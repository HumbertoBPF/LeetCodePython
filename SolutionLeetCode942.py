from typing import List


class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lowest_item_avail = 0
        greatest_item_avail = n
        perm = []

        for i in range(n):
            # Append the lowest value available since it assures that the next item will be greater
            if s[i] == "I":
                perm.append(lowest_item_avail)
                lowest_item_avail += 1
            # Append the greatest value available since it assures that the next item will be lower
            else:
                perm.append(greatest_item_avail)
                greatest_item_avail -= 1
        # At the end lowest_item_avail and greatest_item_avail point to the same value
        perm.append(lowest_item_avail)

        return perm


o1 = Solution()
print(o1.diStringMatch("DDI"))
