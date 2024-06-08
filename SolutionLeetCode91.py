class Solution:
    def numDecodings(self, s: str) -> int:
        s = self.get_decodable_str(s)

        if s is None:
            return 0

        n = len(s)
        memory = [0] * n
        return self.sub_problem(0, s, memory)

    def get_decodable_str(self, s):
        decodable_str = []

        n = len(s)
        # A zero has to combine with "1" and "2" to form "10" and "20" respectively in order to be decoded
        for i in range(n):
            char = s[i]
            if char == "0":
                # Since the first digit doesn't have a left neighbor, if it is 0, the string is not decodable
                # For other positions, if the digit is 0, we need 1 or 2 on the left to assure that the string is decodable
                if (i == 0) or (s[i - 1] != "1" and s[i - 1] != "2"):
                    return None
                continue

            if i < n - 1:
                next_char = s[i + 1]
                if next_char == "0":
                    decodable_str.append(char + next_char)
                    continue

            decodable_str.append(char)

        return decodable_str

    def sub_problem(self, i, s, memory):
        # P(s[i:n]) = P(s[i+1:n]) + P([i+2:n])
        # if s[i] = 1 and s[i + 1] in [1, 2, 3, 4, 5, 6, 7, 8, 9] or s[i] = 2 and s[i + 1] in [1, 2, 3, 4, 5, 6]
        # P(s[i:n]) = P(s[i+1:n]) otherwise
        n = len(s)
        # Fundamental case: string with one character (one decoding possible)
        if i >= n - 1:
            return 1

        if memory[i] != 0:
            return memory[i]

        left_most_char = s[i]
        right_neighbor = s[i + 1]

        num_decodings = self.sub_problem(i + 1, s, memory)
        # We can only combine a digit with its right neighbor if it is "1" or "2"
        # (for "2", the neighbor must be "1", "2", "3", "4", "5" or "6")
        if (
                (
                        left_most_char == "1" and
                        right_neighbor in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
                ) or
                (
                        left_most_char == "2" and
                        right_neighbor in {"1", "2", "3", "4", "5", "6"}
                )
        ):
            num_decodings += self.sub_problem(i + 2, s, memory)

        memory[i] = num_decodings
        return num_decodings


solution = Solution()
print(solution.numDecodings("1201234"))
