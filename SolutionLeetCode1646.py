class Solution:
    def getMaximumGenerated(self, n):
        all_terms = [0, 1]
        max_term = 1
        # Case for which we consider only the first ter
        if n == 0:
            return 0
        # Compute all the terms from the second one until the nth one
        for i in range(2, n+1):
            if i % 2 == 0:
                all_terms.append(all_terms[int(i/2)])
            else:
                all_terms.append(all_terms[int((i-1)/2)] + all_terms[int((i-1)/2) + 1])
            # Check if the maximum needs to be updated
            if all_terms[-1] > max_term:
                max_term = all_terms[-1]

        return max_term


o1 = Solution()
print(o1.getMaximumGenerated(3))
