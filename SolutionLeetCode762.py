import math


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        memory_prime_nums = {}
        memory_nb_bits = {}
        counter = 0

        for i in range(left, right + 1):
            nb_set_bits = self.get_number_set_bits(i, memory_nb_bits)

            if self.is_prime(nb_set_bits, memory_prime_nums):
                counter += 1

        return counter

    def get_number_set_bits(self, n, memory):
        n_shifted = n

        if n_shifted == 0:
            return 0

        if n_shifted in memory:
            return memory[n_shifted]

        nb_set_bits = n_shifted & 1

        n_shifted = n_shifted >> 1
        nb_set_bits +=  self.get_number_set_bits(n_shifted, memory)

        memory[n] = nb_set_bits
        return nb_set_bits

    def is_prime(self, n, memory):
        if n == 1:
            return False

        if (n > 2) and (n % 2 == 0):
            return False

        if n in memory:
            return memory[n]

        is_prime = True

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break

        memory[n] = is_prime
        return is_prime
