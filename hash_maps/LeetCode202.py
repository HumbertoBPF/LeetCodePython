class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()

        number = n

        while number != 1:
            # If we enter a loop, the number is not happy
            if number in seen_numbers:
                return False
            # Track seen numbers to be able to identify potential loops
            seen_numbers.add(number)
            number = self.sum_square_of_digits(number)

        return True

    def sum_square_of_digits(self, n):
        sum_squares = 0
        number = n

        while number > 0:
            quotient = number // 10
            remainder = number % 10

            sum_squares += remainder**2

            number = quotient

        return sum_squares
