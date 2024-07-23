from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        length_compressed_list = 0

        group_length = 1
        last_char = chars[0]

        for i in range(1, n):
            current_char = chars[i]

            if current_char == last_char:
                group_length += 1
                continue

            number_added_items = self.modify_input_list_in_place(chars, last_char, group_length, length_compressed_list)
            length_compressed_list += number_added_items
            # Track the new character and reset the group length
            last_char = current_char
            group_length = 1
        # Take into account the last group of characters when leaving the above iteration
        number_added_items = self.modify_input_list_in_place(chars, last_char, group_length, length_compressed_list)
        length_compressed_list += number_added_items

        return length_compressed_list

    def modify_input_list_in_place(self, chars, char, group_size, last_in_place_index):
        # Take into account the character
        chars[last_in_place_index] = char
        number_of_added_items = 1
        # If the group size is greater than 1, take its digits into account
        if group_size > 1:
            str_group_length = str(group_size)

            for digit in str_group_length:
                chars[last_in_place_index + number_of_added_items] = digit
                number_of_added_items += 1

        return number_of_added_items
