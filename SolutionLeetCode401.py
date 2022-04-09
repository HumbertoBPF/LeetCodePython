from collections import deque
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Base cases
        if turnedOn >= 9:
            return []
        elif turnedOn == 0:
            return ["0:00"]

        # First position indicates the hours and the second one indicates the minutes
        time_list = [0, 0]
        # Bits to be used
        stack_bits = deque([("M", 32), ("M", 16), ("M", 8), ("M", 4), ("M", 2), ("M", 1), ("H", 8), ("H", 4),
                            ("H", 2), ("H", 1)])

        return self.turn_bit_on(turnedOn, time_list, stack_bits, 0, [])

    def turn_bit_on(self, turned_on, time_list, stack_bits, number_leds_turned_on, time_strings):
        # Checks if we turned on the required number of LEDs
        if number_leds_turned_on == turned_on:
            minutes = str(time_list[1])
            # Checking if it is necessary to add a leading zero to the minutes
            if time_list[1] < 10:
                minutes = "0"+minutes

            time_strings.append(str(time_list[0]) + ":" + minutes)
            return time_strings
        # Get all the combinations that have this bit(and all the bits that were added in the upper level calls of this function)
        while len(stack_bits) != 0:
            bit = stack_bits.pop()
            # Check if the hours and the minutes can be incremented by the number corresponding to this bit
            if bit[0] == "H":
                if time_list[0] + bit[1] < 12:
                    time_list_copy = time_list.copy()
                    time_list_copy[0] += bit[1]
                    self.turn_bit_on(turned_on, time_list_copy, stack_bits.copy(), number_leds_turned_on+1, time_strings)
            elif time_list[1] + bit[1] < 60:
                time_list_copy = time_list.copy()
                time_list_copy[1] += bit[1]
                self.turn_bit_on(turned_on, time_list_copy, stack_bits.copy(), number_leds_turned_on+1, time_strings)

        return time_strings


o1 = Solution()
print(o1.readBinaryWatch(1))
