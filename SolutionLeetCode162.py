from typing import List


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        start = 0
        end = n - 1
        # Checking if the first item is a peak
        if nums[start] > nums[start + 1]:
            return start
        # Checking if the last item is a peak
        if nums[end] > nums[end - 1]:
            return end
        # If the cases above are excluded, we have an increase from 0 to 1 and a decrease from end - 1 to end
        # At some moment the numbers must go from increasing to decreasing. The item where it happens is the peak
        while end - start > 1:
            mid = (start + end) // 2
            # We have an increase from mid - 1 to mid and a decrease from mid to mid + 1, so mid is a peak
            if (nums[mid] > nums[mid - 1]) and (nums[mid] > nums[mid + 1]):
                return mid
            # If "mid" increases on the right side, there is a peak on the right side of it
            if nums[mid] < nums[mid + 1]:
                start = mid
            # If "mid" decreases on the left side, there is a peak on the left side of it
            if (nums[mid] < nums[mid - 1]) and (nums[mid] > nums[mid + 1]):
                end = mid
        # This line of code should never be reached given the problem constraints
        return -1


solution = Solution()
nums = [1, 2, 1, 2, 1]
print(solution.findPeakElement(nums))
