class Solution:
    def checkValidString(self, s: str) -> bool:
        # List with the position of symbols that have already been used
        to_ignore = set()

        if not self.validate_closing_parenthesis(s, to_ignore):
            return False

        return self.validate_opening_parenthesis(s, to_ignore)

    def validate_closing_parenthesis(self, s, to_ignore):
        n = len(s)
        # Dictionary with indices of symbols that are available for use (to close parenthesis)
        occurrences = {"(": [], "*": []}

        for i in range(n):
            symbol = s[i]

            if (symbol == "(") or (symbol == "*"):
                occurrences[symbol].append(i)
                continue
            # We need to find an opening parenthesis to cancel the closing one
            if len(occurrences["("]) > 0:
                closing_index = occurrences["("].pop()

                to_ignore.add(i)
                to_ignore.add(closing_index)
                continue
            # Use an asterisk as an opening parenthesis if we don’t have any left
            if len(occurrences["*"]) > 0:
                closing_index = occurrences["*"].pop()

                to_ignore.add(i)
                to_ignore.add(closing_index)
                continue
            # Return False if we don’t have any opening parenthesis or asterisk left
            return False

        return True

    def validate_opening_parenthesis(self, s, to_ignore):
        n = len(s)
        # Dictionary with indices of asterisks that are available for use (to close parenthesis)
        occurrences = {"*": []}

        for i in range(n):
            if (n - i - 1) not in to_ignore:
                symbol = s[n - i - 1]
                # Store occurrence of an asterisk to possibly use it after to close a parenthesis
                if symbol == "*":
                    occurrences[symbol].append(i)
                    continue
                # If we have asterisks available, use it to close a "("
                if len(occurrences["*"]) > 0:
                    occurrences["*"].pop()
                    continue

                return False

        return True