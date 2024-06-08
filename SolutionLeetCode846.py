import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nb_cards = len(hand)
        # Some cards will remain if we try to group them in groups with the specified size
        if nb_cards % groupSize != 0:
            return False
        # Hash map with the number of occurrences of each card
        cards_frequency = self.get_frequency_map(hand)
        # Min heap to store the lowest cards that we have
        cards_heap = list(cards_frequency.keys())
        heapq.heapify(cards_heap)

        while len(cards_heap) > 0:
            first_card = cards_heap[0]

            for i in range(groupSize):
                frequency_needed_card = cards_frequency.get(first_card + i, 0)
                # It's not possible to mount a triplet if we don't have any occurrences of the needed cards
                if frequency_needed_card == 0:
                    return False

                cards_frequency[first_card + i] -= 1

                if cards_frequency[first_card + i] == 0:
                    heapq.heappop(cards_heap)

        return True

    def get_frequency_map(self, hand):
        """
        :param hand: list of cards
        :return: dictionary with the frequency of each card
        """
        frequency_map = {}

        for card in hand:
            if card not in frequency_map:
                frequency_map[card] = 0
            frequency_map[card] += 1

        return frequency_map


hand = [1,2,3,6,2,3,4,7,8]
group_size = 3
solution = Solution()
print(solution.isNStraightHand(hand, group_size))