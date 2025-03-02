from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.neighbors: List[Optional[TrieNode]] = [None]*26
        self.end: bool = False

    def insert(self, word: str):
        current_node = self

        for letter in word:
            index = ord(letter) - ord("a")

            if current_node.neighbors[index] is None:
                current_node.neighbors[index] = TrieNode()

            current_node = current_node.neighbors[index]

        current_node.end = True


    def number_of_words_from_node(self, node: "TrieNode"):
        nb_words = 0

        for neighbor in node.neighbors:
            if neighbor is not None:
                nb_words += 1

        return nb_words


    def delete(self, word):
        current_node = self

        i = 0
        start_deletion_from = 0

        for letter in word:
            # Checking if the word is or shares a prefix with other words
            if current_node.end or (self.number_of_words_from_node(current_node) > 1):
                start_deletion_from = i

            index = ord(letter) - ord("a")
            # The word could not be found
            if current_node.neighbors[index] is None:
                return

            current_node = current_node.neighbors[index]
            i += 1
        # If the word is a prefix of another word, just set the flag "end" to False
        if self.number_of_words_from_node(current_node) > 0:
            current_node.end = False
            return

        current_node = self
        i = 0
        # Deleting everything that comes after the common prefix
        for letter in word:
            index = ord(letter) - ord("a")

            if i == start_deletion_from:
                current_node.neighbors[index] = None
                return

            current_node = current_node.neighbors[index]
            i += 1


class Solution:
    # n: number of rows of board
    # m: number of columns of board
    # k: length of the "words" list
    # p: maximum length of a word
    # Time complexity: O(m*n*p*k))
    # Space complexity: O(k*p) due to the trie data structure
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board

        self.n = len(board)
        self.m = len(board[0])

        self.visited = set()

        self.found_words = set()
        # O(k*p) is the time needed to initialize the Trie
        self.root = TrieNode()

        for word in words:
            self.root.insert(word)
        # O(n*m) due to the nested for loop
        for i in range(self.n):
            for j in range(self.m):
                self.visited = set()
                # O(p*k)
                self.dfs(i, j, self.root, "")

        return [word for word in self.found_words]

    def is_in_bounds(self, i: int , j: int):
        return (0 <= i <= self.n - 1) and (0 <= j <= self.m - 1)

    def dfs(self, i: int, j: int, current_node: TrieNode, current_word: str):
        if current_node.end:
            self.found_words.add(current_word)
            self.root.delete(current_word)

        if not self.is_in_bounds(i, j):
            return

        if (i, j) in self.visited:
            return

        letter = self.board[i][j]
        index = ord(letter) - ord("a")
        next_node = current_node.neighbors[index]

        if next_node is None:
            return

        self.visited.add((i, j))

        self.dfs(i - 1, j, next_node, current_word + letter)
        self.dfs(i + 1, j, next_node, current_word + letter)
        self.dfs(i, j - 1, next_node, current_word + letter)
        self.dfs(i, j + 1, next_node, current_word + letter)

        self.visited.remove((i, j))
