from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.get_combinations(candidates, 0, 0, target, [], [])

    def get_combinations(self, candidates, index, current_sum, target, combination, combinations):
        # If the current sum of the items of the array "combinations" is greater or equal than the target one, stop this recursion
        if current_sum >= target:
            # If the target value is attained, append this combination to the list of combinations
            if current_sum == target:
                combinations.append(combination)
            return combinations
        # Find the combinations containing the items that still are after combinations[index](included).
        # Remark: the number of combinations is always lower then 150
        while index != len(candidates) and len(combinations) < 150:
            # Pick the item currently being pointed and add it to the current combination and to the current sum
            current_number = candidates[index]
            # Call recursion to keep trying to reach the target sum(notice that we have not skipped the item being currently
            # pointed since repetitions are allowed)
            self.get_combinations(candidates, index, current_sum + current_number, target, combination+[current_number], combinations)
            # Go to the next item
            index += 1

        return combinations


o1 = Solution()
print(o1.combinationSum([2,3,6,7], 7))
