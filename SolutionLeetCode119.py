class Solution(object):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    def getRow(self, rowIndex):
        # Initialize the Pascal triangle with the first row(differently from the last problem, we do not need to retain
        # the whole triangle, but only the row computed lastly)
        last_row = [1]
        # Index of the row that is being currently built
        current_index = 2

        while current_index <= rowIndex+1:
            # List of numbers of the current level
            current_level_list = []

            while len(current_level_list) < current_index:
                len_current_level_list = len(current_level_list)
                # The first and the last item are always 1
                if (len_current_level_list == 0) or (len_current_level_list == current_index - 1):
                    current_level_list.append(1)
                # If we are computing any item between the first and the last ones, we use a recurrence formula wrt to
                # the last level
                else:
                    current_level_list.append(last_row[len_current_level_list - 1] + last_row[len_current_level_list])

            last_row = current_level_list
            current_index += 1

        return last_row


o1 = Solution()
print(o1.getRow(0))
