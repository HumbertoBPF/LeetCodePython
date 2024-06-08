from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        self.get_palindrome_partitions(s, [], partitions)
        return partitions

    def get_palindrome_partitions(self, substr, partition, partitions):
        if len(substr) == 0:
            partitions.append(partition.copy())
            return

        n = len(substr)

        for i in range(1, n + 1):
            # Merge other letters to try form new palindromes
            merged_substr = substr[:i]
            remaining_substr = substr[i:]
            # Only continue if the recently merged letters form a palindrome
            if self.is_palindrome(merged_substr):
                partition.append(merged_substr)
                self.get_palindrome_partitions(remaining_substr, partition, partitions)
                partition.pop()

    def is_palindrome(self, s):
        n = len(s)

        for i in range(n // 2):
            if s[n - 1 - i] != s[i]:
                return False

        return True

solution = Solution()
print(solution.partition("humberto"))
