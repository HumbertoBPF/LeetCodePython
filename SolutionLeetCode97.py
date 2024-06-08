class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Edge cases: empty strings
        if s1 == "":
            return s2 == s3

        if s2 == "":
            return s1 == s3

        n = len(s1)
        m = len(s2)
        # Checking if the length of s3 is the sum of the lengths of s1 and s2
        if len(s3) != n + m:
            return False
        # Matrix (n + 1) x (m + 1) to store the solutions of the sub-problems
        memory = []

        for i in range(n + 1):
            memory.append([False]*(m + 1))
        # IS(s1[0:0], s2[0:0]) = True
        memory[0][0] = True
        # IS(s1[0:i], s2[0:0]) = IS(s1[0:i - 1], s2[0:0]) and s1[i - 1] == s3[i - 1]
        for i in range(1, n + 1):
            memory[i][0] = memory[i - 1][0] and s1[i - 1] == s3[i - 1]
        # IS(s1[0:0], s2[0:i]) = IS(s1[0:0], s2[0:i - 1]) and s2[i - 1] == s3[i - 1]
        for j in range(1, m + 1):
            memory[0][j] = memory[0][j - 1] and s2[j - 1] == s3[j - 1]
        # s3[n + m - 1] is a letter of s1
        # IS(s1[0:n], s2[0:m]) = IS(s1[0:n - 1], s2[0:m]) and (s1[n - 1] == s3[n + m - 1])
        # s3[n + m - 1] is a letter of s2
        # IS(s1[0:n], s2[0:m]) = IS(s1[0:n], s2[0:m - 1]) and (s2[m - 1] == s3[n + m - 1])
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                is_letter_of_s1 = memory[i - 1][j] and (s1[i - 1] == s3[i + j - 1])
                is_letter_of_s2 = memory[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                memory[i][j] = is_letter_of_s1 or is_letter_of_s2

        return memory[n][m]

s1 = "ab"
s2 = "bc"
s3 = "bbac"
solution = Solution()
print(solution.isInterleave(s1, s2, s3))