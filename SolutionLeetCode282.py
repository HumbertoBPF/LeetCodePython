from typing import List


class Solution:
    # Time complexity: O(n*4^n)
    # Space complexity: O(4^n)
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        # O(n)
        digits = [int(digit) for digit in num]
        valid_operator_seqs = []
        # O(n*4^n)
        self.get_valid_operators(1, digits, target, [], valid_operator_seqs)

        expressions = []
        # O(n*4^n)
        for operator_seq in valid_operator_seqs:
            expression = num[0]

            for i in range(1, n):
                expression += operator_seq[i - 1]
                expression += num[i]

            expressions.append(expression)

        return expressions

    def get_valid_operators(self, i, digits, target, operator_seq, valid_operator_seqs):
        n = len(digits)

        if i > n - 1:
            if self.is_valid_operator_seq(digits, operator_seq, target):
                valid_operator_seqs.append(operator_seq.copy())
            return

        for operator in ["+", "-", "*", ""]:
            operator_seq.append(operator)
            self.get_valid_operators(i + 1, digits, target, operator_seq, valid_operator_seqs)
            operator_seq.pop()

    def merge_digits(self, digits, operators):
        n = len(digits)
        nums = [digits[0]]
        math_operators = []

        for i in range(1, n):
            operator = operators[i - 1]
            num = digits[i]

            if operator == "":
                # We should not allow leading zeroes
                if nums[-1] == 0:
                    return None, None
                nums[-1] = int(str(nums[-1]) + str(num))
                continue

            nums.append(num)
            math_operators.append(operator)

        return nums, math_operators

    def solve_products(self, nums, operators):
        n = len(nums)
        nums_with_product_solved = [nums[0]]
        operators_without_product = []

        for i in range(1, n):
            operator = operators[i - 1]
            num = nums[i]

            if operator == "*":
                nums_with_product_solved[-1] *= num
                continue

            nums_with_product_solved.append(num)
            operators_without_product.append(operator)

        return nums_with_product_solved, operators_without_product

    def solve_addition_and_subtraction(self, nums, operators):
        n = len(nums)
        result = nums[0]

        for i in range(1, n):
            operator = operators[i - 1]
            num = nums[i]

            if operator == "+":
                result += num
            else:
                result -= num

        return result

    def is_valid_operator_seq(self, digits, operators, target):
        nums, math_operators = self.merge_digits(digits, operators)

        if nums is None:
            return False

        nums_with_product_solved, operators_without_product = self.solve_products(nums, math_operators)
        result = self.solve_addition_and_subtraction(nums_with_product_solved, operators_without_product)
        return result == target
