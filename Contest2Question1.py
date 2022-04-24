class Solution(object):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    def intersection(self, nums):
        n = len(nums)
        # If nums has only one item, we return this item(intersection of the nums[0] with itself)
        if n == 1:
            intersection_list = nums[0]
            # Sort the intersection list
            intersection_list.sort()
            return intersection_list
        # Dictionary to store the intersection
        intersection = {}
        for i in nums[0]:
            intersection[i] = True

        for i in range(1, n):
            # This set will be used to determine the intersection between the intersection dict and nums[i]
            aux_dict = {}
            for j in nums[i]:
                # If the current item of nums[i] is in the intersection, it must be kept
                if intersection.get(j) is not None:
                    aux_dict[j] = True
            intersection = aux_dict.copy()

        intersection_list = list(intersection.keys())
        # Sort the intersection list
        intersection_list.sort()

        return intersection_list


o1 = Solution()
print(o1.intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))
