class Solution:

    def digitSum(self, s: str, k: int) -> str:
        # Repeat round while the length of the string is greater than k
        while len(s) > k:
            s = self.execute_round(s, k)

        return s

    def execute_round(self, s, k):
        new_digits = ""
        length_digits = len(s)
        index = 0
        # Sum blocks of k digits
        while index < length_digits:
            # Adds the first digit
            new_digit = int(s[index])
            number_sums = 1
            # Adds the (k-1) next digits(or the maximum of digits that we can until going out of bounds)
            while number_sums != k and index+1 < length_digits:
                new_digit += int(s[index+1])
                index += 1
                number_sums += 1
            # Add the new digit to the string
            new_digits += str(new_digit)
            index += 1

        return new_digits


o1 = Solution()
print(o1.digitSum("27", 2))
