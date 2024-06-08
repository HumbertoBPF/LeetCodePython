from typing import List


class Solution:
    # Time complexity: O(2^n) (O(2^n) invocations of the recursive function)
    # Space complexity: O(2^n) (O(2^n) due to the output array + O(n) due to the recursion stack)
    def grayCode(self, n: int) -> List[int]:
        output = [0]
        self.flip_bits_on_the_right(0, n - 1, output)
        return output

    def flip_bits_on_the_right(self, n, k, output):
        if k > 0:
            # Explore all the possibilities by flipping the bits on the right of the kth one
            n = self.flip_bits_on_the_right(n, k - 1, output)
        # Flip the bit at the position k
        n = self.flip_bit(n, k)
        output.append(n)

        if k > 0:
            # Explore all the possibilities by flipping the bits on the right of the kth one
            # (with the kth bit flipped now)
            n = self.flip_bits_on_the_right(n, k - 1, output)

        return n

    def flip_bit(self, n, k):
        """
        Flips the bit at position k (0 becomes 1 and vice-versa)
        :param n: number to have the bits flipped
        :param k: position (0-indexed) of the bit to be flipped
        :return: the number with the specified bit flipped
        """
        return n ^ (1 << k)


solution = Solution()
print(solution.grayCode(1))
