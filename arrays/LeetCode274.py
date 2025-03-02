from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def hIndexBruteForce(self, citations: List[int]) -> int:
        n  = len(citations)
        h_index = 0

        for i in range(1, n + 1):
            articles_with_more_than_i_citations  = 0

            for j in range(n):
                if citations[j] >= i:
                    articles_with_more_than_i_citations += 1

                if articles_with_more_than_i_citations == i:
                    h_index = i
                    break

        return h_index

    # Time complexity: O(n*log n)
    # Space complexity: O(1)
    def hIndexSorting(self, citations: List[int]) -> int:
        n = len(citations)

        h_index = 0

        citations.sort(reverse=True)

        for i in range(n):
            if citations[i] >= i + 1:
                h_index = i + 1

        return h_index
