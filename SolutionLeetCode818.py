import sys


class Solution:
    def racecar(self, target: int) -> int:
        memory = {}

        position = 0
        speed = 1

        nb_instructions = 0

        fundamental_cases = []

        while position < 10000:
            nb_instructions += 1
            position += speed
            speed *= 2
            fundamental_cases.append(position)
            memory[position] = nb_instructions
        print(memory)
        min_instructions = self.sub_problem(target, fundamental_cases, memory)
        return min_instructions

    def sub_problem(self, target, fundamental_cases, memory):
        if target in memory:
            return memory[target]

        min_instructions = sys.maxsize
        i = 0

        while abs(target - fundamental_cases[i]) < target:
            fundamental_case = fundamental_cases[i]

            if target - fundamental_case > 0:
                nb_instructions = (
                        2 +
                        self.sub_problem(fundamental_case, fundamental_cases, memory) +
                        self.sub_problem(target - fundamental_case, fundamental_cases, memory)
                )
            else:
                nb_instructions = (
                        1 +
                        self.sub_problem(fundamental_case, fundamental_cases, memory) +
                        self.sub_problem(fundamental_case - target, fundamental_cases, memory)
                )

            if nb_instructions < min_instructions:
                min_instructions = nb_instructions

            i += 1

        memory[target] = min_instructions
        return min_instructions



target = 5
solution = Solution()
print(solution.racecar(target))
