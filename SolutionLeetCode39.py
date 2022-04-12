from collections import deque
from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.get_combinations(deque(candidates), 0, target, [], [])

    # Remark: the numbers_to_use argument is used to specify to the function the candidates that must participate of the
    # combination list that is being built
    def get_combinations(self, numbers_to_use, current_sum, target, combination, combinations):
        # If the current sum of the items of the array "combinations" is greater or equal than the target one, stop this recursion
        if current_sum >= target:
            # If the target value is attained, append this combination to the list of combinations
            if current_sum == target:
                combinations.append(combination)
            return combinations
        # Find the combinations containing the items that still are in the queue. Remark: the number of combinations is
        # always lower then 150
        while len(numbers_to_use) != 0 and len(combinations) < 150:
            # Before removing the first item from the queue, create a copy of the queue, which is going to be used in the
            # next call of the recursion
            numbers_to_use_copy = numbers_to_use.copy()
            # Remove the first item of the queue and add it to the current combination and to the current sum
            current_number = numbers_to_use.popleft()
            combination_copy = combination.copy()
            combination_copy.append(current_number)
            # Call recursion to keep trying to reach the target sum
            self.get_combinations(numbers_to_use_copy, current_sum + current_number, target, combination_copy, combinations)

        return combinations


o1 = Solution()
print(o1.combinationSum([2,3,5], 8))
