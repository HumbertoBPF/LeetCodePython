from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0 for _ in range(n)]
        stack = []

        for i in range(n):
            temperature = temperatures[i]

            while len(stack) != 0 and temperatures[stack[-1]] < temperature:
                index = stack.pop()
                answer[index] = i - index

            stack.append(i)

        return answer
