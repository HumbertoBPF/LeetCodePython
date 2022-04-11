from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        return self.add_parenthesis(n, 0, 0, "", [])

    def add_parenthesis(self, n, n_parenthesis_opened, n_parenthesis_closed, parenthesis_string, combinations):
        # If we have closed n parenthesis so far, add the current string to the list of combinations
        if n_parenthesis_closed == n:
            combinations.append(parenthesis_string)
            return combinations
        # If we are allowed to open a parenthesis(i.e. if we have not opened n parenthesis yet), do it
        if n_parenthesis_opened < n:
            self.add_parenthesis(n, n_parenthesis_opened+1, n_parenthesis_closed, parenthesis_string+"(", combinations)
        # If we are allowed to close a parenthesis(i.e. if there is at least one parenthesis opened), do it
        if n_parenthesis_closed < n_parenthesis_opened:
            self.add_parenthesis(n, n_parenthesis_opened, n_parenthesis_closed+1, parenthesis_string+")", combinations)

        return combinations


o1 = Solution()
print(o1.generateParenthesis(3))
