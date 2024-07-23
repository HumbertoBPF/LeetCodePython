import math


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(1) if we neglect the space of the output
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        gdc = math.gcd(n, m)
        str_gdc = ""

        for i in range(gdc):
            if str1[i] != str2[i]:
                return ""
            str_gdc += str1[i]

        if self.is_divisible(str1, str_gdc) and self.is_divisible(str2, str_gdc):
            return str_gdc

        return ""

    def is_divisible(self, s, t):
        n = len(s)
        m = len(t)

        for i in range(n//m):
            for j in range(m):
                if t[j] != s[i*m + j]:
                    return False

        return True
