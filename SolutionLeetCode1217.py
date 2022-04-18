from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        two_first_positions = [0, 0]
        # Put the items in the two first positions since moving the chips of a pair number of positions is free cost
        for i in position:
            # Two possibilities :
            #   - Even position, then move the chip to the first position(index 0)
            #   - Odd position, then move it to the second position(index 1)
            two_first_positions[i % 2] += 1
        # Return the cheapest option between moving the chips from index 0 to index 1 or the opposite move
        return min(two_first_positions[0], two_first_positions[1])


o1 = Solution()
print(o1.minCostToMoveChips([2,2,2,3,3]))
