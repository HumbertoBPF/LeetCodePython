from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = self.get_adjacency_list(n, flights)
        min_prices = self.get_prices(n, src)
        # We are allowed to have k stops (we will check a nb_stops from 0 to k)
        for nb_stops in range(k + 1):
            # Copy of min_prices
            previous_prices = [min_prices[city] for city in range(n)]

            for city in range(n):
                # Check the best price that we got so far for this city
                current_price = previous_prices[city]
                # Ignore cities that we haven't visited yet
                if current_price == float("inf"):
                    continue
                # Check if we can arrive to a neighbor city for a better price
                for neighbor_city, price in adj[city]:
                    updated_price = current_price + price

                    if updated_price < min_prices[neighbor_city]:
                        min_prices[neighbor_city] = updated_price

        return min_prices[dst] if min_prices[dst] != float("inf") else -1

    def get_adjacency_list(self, n, flights):
        adj = [set() for _ in range(n)]

        for flight in flights:
            src, dst, price = flight
            adj[src].add((dst, price))

        return adj

    def get_prices(self, n, src):
        # Keep track of the price for all the cities
        prices = [float("inf") for _ in range(n)]
        # Because we leave from src, the minimum price to it is 0
        prices[src] = 0
        return prices

n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
solution = Solution()
print(solution.findCheapestPrice(n, flights, src, dst, k))