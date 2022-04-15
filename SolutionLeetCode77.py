from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.get_combination(n, k, 0, [], [])

    def get_combination(self, n, k, current_number, combination, combinations):
        # If the "combination" list has the required length, append it to "combinations"
        if len(combination) == k:
            combinations.append(combination)
            return combinations
        # Add the next numbers to the "combination" list
        for i in range(current_number+1, n+1):
            # Verifies if the number of remaining numbers is enough to complete the "combination" list. If it is not,
            # it is not worthy to continue
            if n - current_number < k - len(combination):
                break
            self.get_combination(n, k, i, combination+[i], combinations)

        return combinations


o1 = Solution()
print(o1.combine(5, 1))
