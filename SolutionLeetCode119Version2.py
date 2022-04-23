class Solution(object):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    def getRow(self, rowIndex):
        # Initialize the Pascal triangle with the top level
        pascal_triangle = [[1]]
        # Level that is being currently built
        current_level = 2

        while current_level <= rowIndex+1:
            # List of numbers of the current level
            current_level_list = []

            while len(current_level_list) < current_level:
                len_current_level_list = len(current_level_list)
                # The first and the last item are always 1
                if (len_current_level_list == 0) or (len_current_level_list == current_level - 1):
                    current_level_list.append(1)
                # If we are computing any item between the first and the last ones, we use a recurrence formula wrt to
                # the last level
                else:
                    current_level_list.append(
                        pascal_triangle[-1][len_current_level_list - 1] + pascal_triangle[-1][len_current_level_list])

            pascal_triangle.append(current_level_list)
            current_level += 1

        return pascal_triangle[-1]


o1 = Solution()
print(o1.getRow(1))
