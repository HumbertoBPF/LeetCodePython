HEX_MAP = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
NUM_HEX = 8

class Solution:
    def toHex(self, num: int) -> str:
        # Explicitly print a 0 for this case even though it is a leading zero
        if num == 0:
            return "0"

        shifted_num = num
        hex_list = [None] * NUM_HEX

        for i in range(8):
            # Capture the last 4 bits
            hex_list[NUM_HEX - i - 1] = HEX_MAP[shifted_num & 0xf]
            # We shift the number to capture the next 4 bits
            shifted_num = shifted_num >> 4

        return self.from_hex_list_to_str(hex_list)

    def from_hex_list_to_str(self, hex_list):
        hex_repr = ""
        is_leading_zero = True

        for i in range(NUM_HEX):
            if hex_list[i] != "0":
                is_leading_zero = False

            if not is_leading_zero:
                hex_repr += hex_list[i]

        return hex_repr


solution = Solution()
print(solution.toHex(0))
