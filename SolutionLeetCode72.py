class Solution:
    # Time complexity: O(n*m)
    # Space complexity: O(n*m)
    def minDistance(self, word1: str, word2: str) -> int:
        self.word_1 = word1
        self.word_2 = word2

        self.n = len(self.word_1)
        self.m = len(self.word_2)

        self.cache = [[None for _ in range(self.m + 1)] for _ in range(self.n + 1)]

        return self.edit_distance(0, 0, 0)

    def edit_distance(self, i, j, num_operations):
        if self.cache[i][j] is not None:
            return num_operations + self.cache[i][j]
        # If we reached the end of both strings, there is no additional operation to be done
        if (i == self.n) and (j == self.m):
            return num_operations
        # If we reached the end of word_1, but not of word_2, we need to add the remaining letter of word_2
        if i == self.n:
            return num_operations + (self.m - j)
        # If we reached the end of word_2, but not of word_1, we need to add the remaining letter of word_1
        if j == self.m:
            return num_operations + (self.n - i)
        # If the letters match, go to the next letters of word_1 and of word_2
        if self.word_1[i] == self.word_2[j]:
            ans = self.edit_distance(i + 1, j + 1, num_operations)
        else:
            # Insert in word_1: "i" remains the same and go to the next letter of word_2 (word_2[j] was resolved)
            insert_ans = self.edit_distance(i, j + 1, num_operations + 1)
            # Delete in word_1: "j" remains the same and go to the next letter of word_1 (word_1[i] doesn't exist anymore)
            delete_ans = self.edit_distance(i + 1, j, num_operations + 1)
            # Replace word_1[i] with word_2[j]: go to the next letters of word_1 and word_2 with the cost of one operation
            replace_ans = self.edit_distance(i + 1, j + 1, num_operations + 1)
            ans = min(insert_ans, delete_ans, replace_ans)
        # We cache the number of additional operations that it took to convert word_1 into word_2 from this point
        self.cache[i][j] = ans - num_operations
        return ans
