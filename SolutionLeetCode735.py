from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) if we consider the output, O(1) otherwise
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output_stack = []

        for current_asteroid in asteroids:
            if current_asteroid > 0:
                output_stack.append(current_asteroid)
                continue
            # Current asteroid is  going left
            while True:
                # If the stack gets empty, we don't have other option than adding the current asteroid to it
                if len(output_stack) == 0:
                    output_stack.append(current_asteroid)
                    break
                top_asteroid = output_stack[-1]
                # If the top asteroid is going left, then all the stack asteroids are also going left.
                # Hence, we must add the current asteroid to the stack since it can't be destroyed
                if top_asteroid < 0:
                    output_stack.append(current_asteroid)
                    break
                # Asteroid going left is destroyed (return to the outer iteration)
                if top_asteroid > abs(current_asteroid):
                    break
                # Asteroid going right is destroyed (keep checking the stack)
                if top_asteroid < abs(current_asteroid):
                    output_stack.pop()
                    continue
                # Both asteroids are destroyed (pop the stack and return to the outer iteration)
                output_stack.pop()
                break

        return output_stack
