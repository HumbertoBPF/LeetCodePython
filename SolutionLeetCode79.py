from typing import List


class Solution:
    # Time complexity: O(m*n*4^l)
    # Space complexity: O(1)
    # m and n are the dimensions of the matrix and l is the length of the target word
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.find_word_from_coordinate(i, j, board, 0, word):
                    return True

        return False

    def find_word_from_coordinate(self, i, j, board, k, word):
        # If we have iterated over all the letters, we found the word
        if k == len(word):
            return True

        m = len(board)
        n = len(board[0])
        # Checking if the matrix boundaries are exceeded
        if (i < 0) or (i > m - 1) or (j < 0) or (j > n - 1):
            return False

        target_letter = word[k]
        # Checking if we got the letter we are looking for
        if board[i][j] != target_letter:
            return False
        # We set the visited item to -1 since we don't want to visit it again. Like that we don't need extra space to
        # store visited items.
        temp = board[i][j]
        board[i][j] = -1
        # Checking the position below
        if self.find_word_from_coordinate(i + 1, j, board, k + 1, word):
            return True
        # Checking the position above
        if self.find_word_from_coordinate(i - 1, j, board, k + 1, word):
            return True
        # Checking the right position
        if self.find_word_from_coordinate(i, j + 1, board, k + 1, word):
            return True
        # Checking the left position
        if self.find_word_from_coordinate(i, j - 1, board, k + 1, word):
            return True

        board[i][j] = temp

        return False
