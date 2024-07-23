import heapq
from typing import List


class Solution:
    # Time complexity: O((candidates + k)*log candidates)
    # Space complexity: O(candidates)
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        greatest_initial_item = candidates - 1
        lowest_end_item = n - candidates
        # Min heap
        heap_eligible_workers = []
        # If we have a number of candidates greater than 2*candidates,
        # we select the first "candidates" and the last "candidates"
        if greatest_initial_item < lowest_end_item:
            # O(candidates*log candidates)
            for i in range(greatest_initial_item + 1):
                heapq.heappush(heap_eligible_workers, (costs[i], i))
            # O(candidates*log candidates)
            for i in range(lowest_end_item, n):
                heapq.heappush(heap_eligible_workers, (costs[i], i))
        # If we have a number of candidates lower than 2*candidates,
        # all of them are eligible
        else:
            # O(candidates*log candidates)
            for i in range(n):
                heapq.heappush(heap_eligible_workers, (costs[i], i))

        total_cost = 0
        # O(k*log candidates)
        for _ in range(k):
            cheapest_eligible_worker, i = heapq.heappop(heap_eligible_workers)
            total_cost += cheapest_eligible_worker
            # We can't add more candidates, so go to the next iteration
            if greatest_initial_item >= lowest_end_item - 1:
                continue
            # If we popped a candidate from the first half, we have to add a new one
            if i <= greatest_initial_item:
                greatest_initial_item += 1
                heapq.heappush(heap_eligible_workers, (costs[greatest_initial_item], greatest_initial_item))
            # If we popped a candidate from the second half, we have to add a new one
            if i >= lowest_end_item:
                lowest_end_item -= 1
                heapq.heappush(heap_eligible_workers, (costs[lowest_end_item], lowest_end_item))

        return total_cost


solution = Solution()
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4
print(solution.totalCost(costs, k, candidates))
