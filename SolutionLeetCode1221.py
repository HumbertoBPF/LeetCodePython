class Solution(object):
    """
    :type s: str
    :rtype: int
    """
    def balancedStringSplit(self, s):
        n = len(s)
        number_l = 0
        number_r = 0
        max_balanced_str = 0
        for i in range(n):
            # Verify the current char and increment the corresponded counter
            if s[i] == "L":
                number_l += 1
            else:
                number_r += 1
            # If the amount of "l" and "r" is equal, the substring is balanced. Increment counter and restart the char counters
            if number_l == number_r:
                max_balanced_str += 1
                number_l = 0
                number_r = 0

        return max_balanced_str


o1 = Solution()
print(o1.balancedStringSplit("LLLLRRRR"))
