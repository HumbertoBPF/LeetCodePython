class Solution:
    def is_number(self, letter):
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        return letter in digits

    def decodeString(self, s: str) -> str:
        # stack to cache the decoded string while we process a new encoded expression
        stack = []
        decoded_string = ""
        # string to store a number whenever we see it
        current_number = ""

        for letter in s:
            if self.is_number(letter):
                # Push the decoded string processed so far
                if decoded_string is not None:
                    stack.append(decoded_string)
                # Set the decoded string temporarily to None
                decoded_string = None
                # Start building the number that comes before an opening bracket
                current_number += letter
                continue

            if letter == "[":
                # Push the number that comes before the opening bracket
                stack.append(int(current_number))
                # Reset the variables since we will process a new encoded expresision
                decoded_string = ""
                current_number = ""
                continue

            if letter == "]":
                # Pop the stack to regain the cached decoded string
                number = stack.pop()
                prefix = stack.pop()

                for i in range(number):
                    prefix += decoded_string

                decoded_string = prefix
                continue

            decoded_string += letter

        return decoded_string
