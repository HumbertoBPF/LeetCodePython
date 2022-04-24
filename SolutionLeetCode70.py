class Solution(object):
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n):
        factorial_dict = {}
        # Compute all the factorials that are going to be used
        for i in range(n):
            if i < 2:
                factorial_dict[i] = 1
            else:
                factorial_dict[i] = i*factorial_dict[i-1]
        # Start by considering the case where all the steps are "1"
        nb_unitary_steps = n
        nb_double_steps = 0
        # Take into account this case
        nb_possibilities = 1
        # Every time we replace 2 unitary steps with a double step, we increment nb_possibilities with the number of combinations having
        # with nb_unitary_steps "1" and  nb_double_steps "2"(i.e. (nb_unitary_steps+nb_double_steps)!/(nb_unitary_steps!*nb_double_steps!))
        while nb_unitary_steps > 1:
            nb_unitary_steps -= 2
            nb_double_steps += 1
            nb_possibilities += factorial_dict[(nb_unitary_steps+nb_double_steps)]/(factorial_dict[nb_unitary_steps]*factorial_dict[nb_double_steps])

        return int(nb_possibilities)


o1 = Solution()
print(o1.climbStairs(6))
