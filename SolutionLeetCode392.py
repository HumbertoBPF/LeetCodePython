class Solution(object):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    def isSubsequence(self, s, t):
        length_s = len(s)
        # For s being an empty string, we return True since the empty string is the substring of any string
        if length_s == 0:
            return True

        length_t = len(t)
        index_s = 0

        for i in range(length_t):
            # If the letter of s that we are currently looking for is found in t, we skip to the next letter
            if t[i] == s[index_s]:
                index_s += 1
            # If we reached the end of the string s, it means that we found all its letters
            if index_s == length_s:
                return True
        # If we go out from the for loop, it means that we have not found all the letters of s in t
        return False


o1 = Solution()
print(o1.isSubsequence("abcx", "achbgcd"))
