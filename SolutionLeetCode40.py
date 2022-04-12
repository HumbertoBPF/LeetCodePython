from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.get_combinations(candidates, 0, 0, target, [], [])

    def get_combinations(self, candidates, index, current_sum, target, combination, combinations):
        # Stop recursion if the sum has been reached
        if current_sum >= target:
            # If the sum of the combination's items is equal to the target, add the combination to the list of combinations
            if current_sum == target:
                combinations.append(combination)
            return combinations
        # Try to use all the numbers of candidates without repeating the same number
        last_number = -1
        while index != len(candidates):
            # Point to the next item of candidates when the item currently being pointed is added to the current combination
            current_number = candidates[index]
            index += 1
            # If a repetition is identified, skip this number
            if current_number == last_number:
                continue
            self.get_combinations(candidates, index, current_sum + current_number, target, combination + [current_number], combinations)
            last_number = current_number

        return combinations


o1 = Solution()
print(o1.combinationSum2([10,1,2,7,6,1,5], 8))
