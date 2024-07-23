from typing import List


class BruteForceSolution:
    # Time complexity: O(n*m)
    # Space complexity: O(n) if we consider the space needed for the output, otherwise O(1)
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = []

        for spell in spells:
            output.append(0)
            for potion in potions:
                if spell*potion >= success:
                    output[-1] += 1

        return output


class Solution:
    # Time complexity: O((n + m)*log m)
    # Space complexity: O(n) if we consider the space needed for the output, otherwise O(1)
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = []

        m = len(potions)
        # Because we will perform binary search on potions, we need to sort it
        potions.sort()

        for spell in spells:
            start = 0
            end = m - 1
            # If the first potion and the current spell form a successful pair, all potions form a successful pair
            # with this spell.
            if potions[start]*spell >= success:
                output.append(m)
                continue
            # If the last potion and the current spell don't form a successful pair, no potion form a successful pair
            # with this spell.
            if potions[end]*spell < success:
                output.append(0)
                continue
            # At the end of binary search, the pointer end will store the first potion that form a successful pair with
            # the current spell.
            while end - start > 1:
                mid = (start + end) // 2

                if potions[mid]*spell >= success:
                    end = mid
                    continue

                start = mid

            output.append(m - end)

        return output
