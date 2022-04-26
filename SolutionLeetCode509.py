class Solution(object):
    """
    :type n: int
    :rtype: int
    """
    def fib(self, n):
        # First Fibonacci's number(F_0)
        penultimate_item = 0
        # Second Fibonacci's number(F_1)
        last_item = 1
        # If n = 0, return F_0
        if n == 0:
            return penultimate_item
        # Otherwise, compute all the Fibonacci's numbers until the specified n
        for i in range(2, n+1):
            # Computing the ith Fibonacci's
            temp = last_item + penultimate_item
            # Update the cache variables
            penultimate_item = last_item
            last_item = temp
        # Return the Fibonacci's number computed lastly
        return last_item


o1 = Solution()
for i in range(11):
    print(o1.fib(i))
