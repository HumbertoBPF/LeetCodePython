from collections import deque
from typing import List


class Solution:
    # Time complexity: O(n^2*m)
    # Space complexity: O(n) due to the queue and the hash set
    # n = len(wordList) and m = len(beginWord)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}

        for word1 in wordList:
            graph[word1] = []

            for word2 in wordList:
                if self.are_neighbors(word1, word2):
                    graph[word1].append(word2)
        # If the end word is not in the graph, then it cannot be obtained from beginWord through transformations
        if endWord not in graph:
            return 0

        queue = deque()
        visited = {endWord}

        queue.append((endWord, 1))

        while len(queue) > 0:
            current_word, nb_transformations = queue.popleft()
            # If we can obtain beginWord from the current word, then we add the current number of transformation plus
            # the additional transformation needed
            if self.are_neighbors(current_word, beginWord):
                return nb_transformations + 1
            # Add the words from the list that are neighbors of the current word and that were not visited
            for word in graph[current_word]:
                if word not in visited:
                    queue.append((word, nb_transformations + 1))
                    visited.add(word)

        return 0

    def are_neighbors(self, word_1, word_2):
        n = len(word_1)
        nb_diffs = 0

        for i in range(n):
            if word_1[i] != word_2[i]:
                nb_diffs += 1

            if nb_diffs > 1:
                break
        # Neighbor words = words that can be obtained from each other through one transformation = words that differ by
        # only one character
        return nb_diffs == 1
