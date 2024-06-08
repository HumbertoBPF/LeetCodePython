class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        unmatched_left, unmatched_right = self.get_unmatched_positions(s, 0, n - 1)

        if (unmatched_left == -1) and (unmatched_right == -1):
            return True

        if self.get_unmatched_positions(s, unmatched_left, unmatched_right - 1) == (-1, -1):
            return True

        return self.get_unmatched_positions(s, unmatched_left + 1, unmatched_right) == (-1, -1)

    def get_unmatched_positions(self, s, initial_left, initial_right):
        left = initial_left
        right = initial_right

        while left < right:
            if s[left] != s[right]:
                return left, right

            left += 1
            right -= 1

        return -1, -1