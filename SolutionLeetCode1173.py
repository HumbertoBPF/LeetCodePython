class Solution:
    def tribonacci(self, n):
        # Variables to store the terms that are going to be used to compute the next one
        last_number = 1
        penultimate_number = 1
        anti_penultimate_number = 0
        # Base cases
        if n == 0:
            return anti_penultimate_number
        elif n == 1:
            return penultimate_number
        # Compute the next term
        for i in range(2, n):
            temp = last_number + penultimate_number + anti_penultimate_number
            anti_penultimate_number = penultimate_number
            penultimate_number = last_number
            last_number = temp

        return last_number


o1 = Solution()
print(o1.tribonacci(25))
