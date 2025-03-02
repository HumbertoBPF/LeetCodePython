parenthesis = {"(", ")"}
operators = {"+", "-"}
non_digits = parenthesis.union(operators)


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) due to the extra space needed to store the string without spaces
    def calculate(self, s: str) -> int:
        s_without_spaces = self.remove_spaces(s)
        stack = []

        for char in s_without_spaces:
            if char != ")":
                stack.append(char)
                continue

            result = 0

            while stack[-1] != "(":
                number = self.pop_number(stack)
                result = self.perform_operation(result, number, "+")

            stack.pop()

            for digit in str(result):
                stack.append(digit)

        return self.evaluate_simple_expr(stack)

    def evaluate_simple_expr(self, stack):
        result = 0

        while len(stack) > 0:
            number = self.pop_number(stack)
            result = self.perform_operation(result, number, "+")

        return result

    def pop_number(self, stack):
        reversed_number = ""

        while (len(stack) > 0) and (stack[-1] not in non_digits):
            reversed_number += stack.pop()

        number = int(self.reverse_str(reversed_number))

        while len(stack) > 0 and (stack[-1] in operators):
            operation = stack.pop()
            number = self.perform_operation(0, number, operation)

        return number

    def perform_operation(self, x, y, operation):
        if operation == "+":
            return x + y

        return x - y

    def reverse_str(self, s):
        n = len(s)
        reversed_str = ""

        for i in range(n):
            reversed_str += s[n - 1 - i]

        return reversed_str

    def remove_spaces(self, s):
        s_without_spaces = ""

        for char in s:
            if char != " ":
                s_without_spaces += char

        return s_without_spaces


s = "1-(     -2)"
solution = Solution()
print(solution.calculate(s))
