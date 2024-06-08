from typing import List

NUMBER_CELLS = 8

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        current_state = self.compute_next_state(cells)

        period = self.get_period(current_state)
        # Since the number of possible states are equal to the period, we don't have to iterate more than this
        # number of times
        for i in range(0, (n - 1) % period):
            current_state = self.compute_next_state(current_state)

        return current_state

    def get_period(self, initial_state):
        """
        Computes the period of the problem's state machine. The period is the number of iteration that it takes to get
        a repeated prison state.
        :param initial_state: initial state (it can be any prison state after the zeroes at the first and last position
        are set)
        :return: the period of the state machined defined by the problem input
        """
        current_state = initial_state
        computed_states = {tuple(initial_state): 0}
        number_combinations = 2 ** 6

        for i in range(1, number_combinations + 1):
            current_state = self.compute_next_state(current_state)
            # When we see a state for the second time, we compute the period
            if tuple(current_state) in computed_states:
                return i - computed_states[tuple(current_state)]

            computed_states[tuple(current_state)] = i

        return number_combinations

    def compute_next_state(self, current_state):
        next_state = [0] * NUMBER_CELLS
        # We only have to worry about the cells from 1 to 6 (the cell 0 and 7 are always vacant after the day 0)
        for j in range(1, NUMBER_CELLS - 1):
            next_state[j] = int(current_state[j - 1] == current_state[j + 1])
        return next_state
