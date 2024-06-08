from typing import List


class Solution:
    def is_operation(self, token):
        return (token == "+") or (token == "-") or (token == "*") or (token == "/")

    def do_operation(self, token1, token2, operation_token):
        int_token1 = int(token1)
        int_token2 = int(token2)

        if operation_token == "+":
            return int_token1 + int_token2

        if operation_token == "-":
            return int_token1 - int_token2

        if operation_token == "*":
            return int_token1 * int_token2

        return int(int_token1 / int_token2)

    def eval_current_token(self, token, pending_tokens, tokens):
        if len(pending_tokens) == 0:
            return token

        pending_token = pending_tokens[-1]

        if self.is_operation(token) or self.is_operation(pending_token):
            pending_tokens.append(token)
            next_token = tokens.pop()
            return self.eval_current_token(next_token, pending_tokens, tokens)

        operation_token = pending_tokens[-2]

        result = self.do_operation(token, pending_token, operation_token)

        pending_tokens.pop()
        pending_tokens.pop()

        return self.eval_current_token(result, pending_tokens, tokens)


    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        token1 = tokens.pop()
        token2 = tokens.pop()
        token3 = tokens.pop()
        pending_tokens = [token1, token2]
        return self.eval_current_token(token3, pending_tokens, tokens)


# ["2","1","+","3","*"]
#
# pending_tokens = ["*", "3"]
# First iteration: token = "+"
# pending_tokens = ["*", "3", "+"]
# Second_iteration: token = "1"
# pending_tokens = ["*", "3", "+", "1"]
# Third iteration: token = "2"
# result = 1 + 2 = 3
# pending_tokens = ["*", "3"]
# Fourth iteration: token = result = "3"
# result = 3 * 3 = 9
# pending_tokens = []

# ["4","13","5","/","+"]
#
# pending_tokens = ["+", "/"]
# First iteration: token = "5"
# pending_tokens = ["+", "/", "5"]
# Second_iteration: token = "13"
# result = 13 / 5 = 2
# pending_tokens = ["+"]
# Third iteration: token = result = "2"
# pending_tokens = ["+", "2"]
# Fourth iteration: token = "4"
# result = 4 + 2 = 6
# pending_tokens = []
# Fifth iteration: token = result = "6"

# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#
# pending_tokens = ["+", "5"]
# First iteration: token = "+"
# pending_tokens = ["+", "5", "+"]
# Second_iteration: token = "17"
# pending_tokens = ["+", "5", "+", "17"]
# Third iteration: token = "*"
# pending_tokens = ["+", "5", "+", "17", "*"]
# Fourth iteration: token = "/"
# pending_tokens = ["+", "5", "+", "17", "*", "/"]
# Fifth iteration: token = "*"
# pending_tokens = ["+", "5", "+", "17", "*", "/", "*"]
# Sixth iteration: token = "-11"
# pending_tokens = ["+", "5", "+", "17", "*", "/", "*", "-11"]
# Seventh iteration: token = "+"
# pending_tokens = ["+", "5", "+", "17", "*", "/", "*", "-11", "+"]
# Eighth iteration: token = "3"
# pending_tokens = ["+", "5", "+", "17", "*", "/", "*", "-11", "+", "3"]
# Ninth iteration: token = "9"
# result = 9 + 3 = 12
# pending_tokens = ["+", "5", "+", "17", "*", "/", "*", "-11"]
# Tenth iteration: token = "12"
# result = 12 * -11 = -132
# pending_tokens = ["+", "5", "+", "17", "*", "/"]
# Eleventh iteration: token = "-132"
# pending_tokens = ["+", "5", "+", "17", "*", "/", "-132"]
# Twelfth iteration: token = "6"
# result = 6 / -132 = 0
# pending_tokens = ["+", "5", "+", "17", "*"]
# Thirteenth iteration: token = "0"
# pending_tokens = ["+", "5", "+", "17", "*", "0"]
# Fourteenth iteration: token = "10"
# result = 10 * 0 = 0
# pending_tokens = ["+", "5", "+", "17"]
# 15th iteration: token = 0
# result = 0 + 17 = 17
# pending_tokens = ["+", "5"]
# 16th iteration: token 17
# result = 17 + 5 = 22
# pending_tokens = []
solution = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(solution.evalRPN(tokens))
