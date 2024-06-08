class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = self.sub_problem(0, n - 1, s, {})
        return s[start:end + 1]

    def sub_problem(self, start, end, s, cache):
        # if s[0] != s[n - 1] then P(0, n - 1) = max(P(0, n - 2), P(1, n - 1))
        # if s[0] == s[n - 1] then P(0, n - 1) = ...

        # = 2 + P(1, n - 2) if P(1, n - 2) == n - 2
        # = P(0, n - 1) = max(P(0, n - 2), P(1, n - 1))
        if end - start <= 0:
            return start, end

        if (start, end) in cache:
            return cache[(start, end)]

        if s[start] != s[end]:
            left_sub_problem = self.sub_problem(start, end - 1, s, cache)
            right_sub_problem = self.sub_problem(start + 1, end, s, cache)
            answer = left_sub_problem if self.len_solution(left_sub_problem) > self.len_solution(right_sub_problem) else right_sub_problem
        else:
            sub_problem_middle = self.sub_problem(start + 1, end - 1, s, cache)

            if self.len_solution(sub_problem_middle) == end - start - 1:
                answer = (start, end)
            else:
                left_sub_problem = self.sub_problem(start, end - 1, s, cache)
                right_sub_problem = self.sub_problem(start + 1, end, s, cache)
                answer = left_sub_problem if self.len_solution(left_sub_problem) > self.len_solution(right_sub_problem) else right_sub_problem

        cache[(start, end)] = answer
        return answer

    def len_solution(self, solution):
        return solution[1] - solution[0] + 1


class IterativeSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        longest_palindrome = (0, 0)
        memory = [[None] * n for _ in range(n)]

        for diff in range(1, n):
            for i in range(diff, n):
                start = i - diff
                end = i

                if self.sub_problem(start, end, s, memory):
                    longest_palindrome = (start, end)

        start, end = longest_palindrome
        return s[start:end + 1]

    def sub_problem(self, start, end, s, memory):
        # P(s[a:b]) = (s[a] == s[b]) and P(s[a + 1:b - 1])
        # - If the chars at the extremities (at index a and b) don't match, then s[a:b] can't be a palindrome
        # - If the substring between the extremities elements is not a palindrome itself, then the string including s[a]
        # and s[b] can't be a palindrome neither, even if s[a] and s[b] match.
        #
        # One can think, what about the string s[a:b - 1] and s[a + 1:b]? They weren't verified here. Actually, we get
        # if they are palindromes on a previous DP step.
        a = start + 1
        b = end - 1

        sub_problem_middle = True
        # If a = b, then we are considering a string with one char, which is always a palindrome
        # If a > b, then we are considering an empty string, which is a palindrome as well
        if a < b:
            sub_problem_middle = memory[a][b]

        is_palindrome = s[start] == s[end] and sub_problem_middle
        memory[start][end] = is_palindrome

        return is_palindrome


solution = IterativeSolution()
s = "babad"
print(solution.longestPalindrome(s))
