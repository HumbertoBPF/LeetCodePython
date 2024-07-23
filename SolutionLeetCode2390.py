class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) (due to the stack and the output)
    def removeStars(self, s: str) -> str:
        n = len(s)
        # Stack storing non-asterisk characters
        stack = []

        for i in range(n):
            # If we see an asterisk, pop the stack to remove the closest non-star character to its left
            if s[i] == "*":
                stack.pop()
                continue

            stack.append(s[i])

        output = ""

        for item in stack:
            output += item

        return output
