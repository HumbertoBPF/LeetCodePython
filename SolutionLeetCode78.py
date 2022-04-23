class Solution(object):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def subsets(self, nums):
        return self.get_subset(nums, [], [[]], 0)

    # Function that get all the subsets of nums containing the specified subset. The parameter index is the index of the
    # element that comes right after the item added lastly
    def get_subset(self, nums, subset, subsets, index):
        for i in range(index, len(nums)):
            # Each iteration adds nums[i] to the current subset and add it to the list of subsets
            subsets.append(subset+[nums[i]])
            # Get all the subsets containing subset+[nums[i]]
            self.get_subset(nums, subset+[nums[i]], subsets, i + 1)

        return subsets


o1 = Solution()
print(o1.subsets([1, 2, 3, 4]))
print(len(o1.subsets([1, 2, 3, 4])))
