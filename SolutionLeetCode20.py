class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
                continue

            if len(stack) == 0:
                return False

            last_item = stack[-1]

            if (
                    (bracket == ")" and last_item == "(") or
                    (bracket == "]" and last_item == "[") or
                    (bracket == "}" and last_item == "{")
            ):
                stack.pop()
                continue

            return False

        return len(stack) == 0

solution = Solution()
s = "(]"
print(solution.isValid(s))
