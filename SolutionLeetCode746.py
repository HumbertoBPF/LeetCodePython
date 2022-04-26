class Solution(object):
    """
    :type cost: List[int]
    :rtype: int
    """
    def minCostClimbingStairs(self, cost):
        # The trick here is to know that min_cost[i] = min(min_cost[i-1] + cost[i-1],min_cost[i-2] + cost[i-2]) where
        # min_cost[i] is the minimum cost to arrive at the ith position.
        min_cost = [0, 0]           # No cost to arrive at the position 0 and 1 since they are the initial positions
        n = len(cost)
        # Compute the minimal cost associated to all positions of the stair
        for i in range(2, n):
            min_cost.append(min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2]))
        # Compute the minimal cost needed to reach the end of the input array
        return min(min_cost[-1]+cost[-1], min_cost[-2]+cost[-2])

    """
        :type cost: List[int]
        :rtype: int
        """

    def minCostClimbingStairs_Memory_Opt(self, cost):
        # The trick here is to know that min_cost[i] = min(min_cost[i-1] + cost[i-1],min_cost[i-2] + cost[i-2]) where
        # min_cost[i] is the minimum cost to arrive at the ith position.

        # To optimize space, we only store the two last minimal costs since they are the unique used to compute the next
        # minimal cost
        last_min_cost = 0
        penultimate_min_cost = 0
        n = len(cost)
        # Compute the minimal cost associated to all positions of the stair
        for i in range(2, n):
            temp = min(last_min_cost + cost[i - 1], penultimate_min_cost + cost[i - 2])
            penultimate_min_cost = last_min_cost
            last_min_cost = temp
        # Compute the minimal cost needed to reach the end of the input array
        return min(last_min_cost + cost[-1], penultimate_min_cost + cost[-2])


o1 = Solution()
print(o1.minCostClimbingStairs_Memory_Opt([10,15,20]))
