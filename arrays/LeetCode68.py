from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.max_width = maxWidth

        words_per_line = [[]]

        current_line = 0
        current_line_nb_non_spaces = 0

        for word in words:
            if current_line_nb_non_spaces + len(words_per_line[current_line]) + len(word) > maxWidth:
                current_line += 1
                words_per_line.append([])
                current_line_nb_non_spaces = 0

            current_line_nb_non_spaces += len(word)
            words_per_line[current_line].append(word)

        str_lines = []
        nb_lines = len(words_per_line)

        for i in range(nb_lines):
            line = words_per_line[i]

            nb_words = len(line)

            if i == nb_lines - 1:
                str_line = self.build_last_line(line)
            else:
                if nb_words == 1:
                    str_line = self.build_line_with_one_word(line)
                else:
                    str_line = self.build_line_with_multiple_words(line)

            str_lines.append(str_line)

        return str_lines

    def build_last_line(self, words):
        str_line = ""

        for word in words:
            if len(str_line) > 0:
                str_line += " "

            str_line += word

        return self.fill_line_with_spaces(str_line)

    def build_line_with_one_word(self, words):
        str_line = ""

        for word in words:
            str_line += word

        return self.fill_line_with_spaces(str_line)

    def build_line_with_multiple_words(self, words):
        nb_words = len(words)

        nb_non_space_chars = 0

        for word in words:
            nb_non_space_chars += len(word)

        nb_spaces = (self.max_width - nb_non_space_chars) // (nb_words - 1)
        nb_extra_spaces = (self.max_width - nb_non_space_chars) % (nb_words - 1)

        str_line = ""

        for word in words:
            if len(str_line) > 0:
                for j in range(nb_spaces):
                    str_line += " "

                if nb_extra_spaces > 0:
                    str_line += " "
                    nb_extra_spaces -= 1

            str_line += word

        return str_line

    def fill_line_with_spaces(self, str_line):
        str_line_filled_with_spaces = str_line

        while len(str_line_filled_with_spaces) != self.max_width:
            str_line_filled_with_spaces += " "

        return str_line_filled_with_spaces
