class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        memory = []
        # Initializing memory matrix
        for i in range(n):
            memory.append([None] * n)
        # We initialize the counter at n since at least one-length substrings are palindromes
        count = n

        # diff is the substring length of the current iteration
        for diff in range(1, n):
            # Checking if the substring from i - diff to i is a palindrome
            for i in range(diff, n):
                # A given string is a palindrome when:
                # - The chars at the end and at the beginning match
                # - The substring in between these chars is a palindrome itself
                is_palindrome = s[i - diff] == s[i] and self.is_palindrome(i - diff + 1, i - 1, memory)
                if is_palindrome:
                    count += 1
                memory[i - diff][i] = is_palindrome

        return count

    def is_palindrome(self, start, end, memory):
        # start > end maps an empty substring and start == end maps a one-length substring, which are all palindromes
        if start >= end:
            return True

        return memory[start][end]


solution = Solution()
print(solution.countSubstrings("aaaaa"))