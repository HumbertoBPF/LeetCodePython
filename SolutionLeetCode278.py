# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n - 1

        if self.is_bad_version_zero_indexed(start):
            return 1

        is_end_item_the_first_bad_version = self.is_first_bad_version(end)[0]

        if is_end_item_the_first_bad_version:
            return end + 1

        while end - start > 1:
            middle = (start + end) // 2

            is_middle_item_the_first_bad_version, is_middle_item_a_bad_version = self.is_first_bad_version(middle)

            if is_middle_item_the_first_bad_version:
                return middle + 1

            if is_middle_item_a_bad_version:
                end = middle
                continue

            start = middle

        return -1

    def is_bad_version_zero_indexed(self, index):
        return isBadVersion(index + 1)

    def is_first_bad_version(self, index):
        is_bad_version = self.is_bad_version_zero_indexed(index)

        if not is_bad_version:
            return False, False

        return not self.is_bad_version_zero_indexed(index - 1) and is_bad_version, is_bad_version

# [0, 1, 2, 3, 4]
# function output = [false false false true true]
# start = 0
# end = 4
# middle = 2
# isBadVersion(middle) = false
# isBadVersion(middle - 1) = false
# start = 2
# end = 4
# middle = 3
# isBadVersion(middle) = true
# isBadVersion(middle - 1) = false
# Then 4 is the first bad version.