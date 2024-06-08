from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        if n == 2:
            return [1, 2]

        p1 = 0
        p2 = n - 1

        while numbers[p1] + numbers[p2] != target:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1

        return [p1+1, p2+1]
