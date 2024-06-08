from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = [None]*3

        for triplet in triplets:
            # Checking if we have candidates for all the items of the target triplet
            if (candidates[0] is not None) and (candidates[1] is not None) and (candidates[2] is not None):
                break
            # Getting candidates to obtain the item at the first position of the target triplet
            if candidates[0] is None:
                if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                    candidates[0] = triplet
            # Getting candidates to obtain the item at the second position of the target triplet
            if candidates[1] is None:
                if triplet[0] <= target[0] and triplet[1] == target[1] and triplet[2] <= target[2]:
                    candidates[1] = triplet
            # Getting candidates to obtain the item at the third position of the target triplet
            if candidates[2] is None:
                if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] == target[2]:
                    candidates[2] = triplet

        return (candidates[0] is not None) and (candidates[1] is not None) and (candidates[2] is not None)