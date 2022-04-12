from collections import deque
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.get_combinations(deque(candidates), 0, target, [], [])

    def get_combinations(self, numbers_to_use, current_sum, target, combination, combinations):
        # Stop recursion if the sum has been reached
        if current_sum >= target:
            # If the sum of the combination's items is equal to the target, add the combination to the list of combinations
            if current_sum == target:
                combinations.append(combination)
            return combinations
        # Try to use all the numbers of the input queue without repeating the same number
        last_number = -1
        while len(numbers_to_use) != 0:
            # Pop the number from the queue when it is added to the current combination
            current_number = numbers_to_use.popleft()
            # If a repetition is identified, skip this number
            if current_number == last_number:
                continue
            # Create a copy to avoid some kind of "persistence effect" through the multiple recursion
            combination_copy = combination.copy()
            combination_copy.append(current_number)
            self.get_combinations(numbers_to_use.copy(), current_sum + current_number, target, combination_copy, combinations)
            last_number = current_number

        return combinations


o1 = Solution()
print(o1.combinationSum2([2, 5, 2, 1, 2], 5))
