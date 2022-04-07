from typing import List


class Solution:

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum1 = arr[0]
        sum2 = sum(arr) - arr[0]
        i = 1
        n = len(arr)
        # Looking for the first partition
        while (i < n) and (sum2 != 2*sum1):
            sum1 += arr[i]
            sum2 -= arr[i]
            i += 1
        # If we reached the end of the array, it is not possible to do what the problem wants
        if i == n:
            return False

        sum3 = sum2 - arr[i]
        sum2 = arr[i]
        i += 1
        #  Looking for the second and the third partitions
        while (i < n) and (sum2 != sum3):
            sum2 += arr[i]
            sum3 -= arr[i]
            i += 1
        # i cannot be n because it implies that the last partition is empty
        if i == n:
            return False
        # Checking if the sum of the three partitions is the same
        if (sum1 == sum2) and (sum2 == sum3):
            return True

        return False


o1 = Solution()
print(o1.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
