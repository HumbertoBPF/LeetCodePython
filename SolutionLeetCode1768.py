class Solution:
    # Time complexity: O(k) where k = max(n, m)
    # Space complexity: O(n + m) or O(1) if we don't consider the space needed for the output
    # n = len(word1), m = len(word2)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        nb_iter = min(n, m)

        output = ""

        for i in range(nb_iter):
            output += word1[i]
            output += word2[i]
        # Appending the remaining letters if they come from word1
        if n > nb_iter:
            for i in range(nb_iter, n):
                output += word1[i]
        # Appending the remaining letters if they come from word2
        if m > nb_iter:
            for i in range(nb_iter, m):
                output += word2[i]

        return output
