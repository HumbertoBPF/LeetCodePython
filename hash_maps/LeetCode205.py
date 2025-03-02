class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s, t) and self.transform(t, s)

    def transform(self, original, target):
        n = len(original)
        # Hash map translating letters from "original" to letters from "target"
        transform_dict = {}

        for i in range(n):
            original_letter = original[i]
            target_letter = target[i]
            # original_letter has not been seen yet, so we add it to the hash map
            if original_letter not in transform_dict:
                transform_dict[original_letter] = target_letter
                continue
            # If we have already a letter from target being mapped by original_letter, check if it maps target_letter
            if transform_dict[original_letter] != target_letter:
                return False

        return True
