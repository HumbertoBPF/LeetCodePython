class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)

        pending_parenthesis = 0
        output = ""

        for letter in s:
            if letter == "(":
                pending_parenthesis += 1
                # Outer opening parenthesis
                if pending_parenthesis == 1:
                    continue
                output += letter
                continue

            pending_parenthesis -= 1
            # Outer closing parenthesis
            if pending_parenthesis == 0:
                continue
            output += letter

        return output
