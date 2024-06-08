import heapq


class StockPrice:
    def __init__(self):
        # key = timestamp, value = price
        self.stocks = {}
        self.last_timestamp = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.stocks[timestamp] = price
        # Tracks the maximum timestamp
        self.last_timestamp = max(self.last_timestamp, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.stocks[self.last_timestamp]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]
        # The stocks dictionary is the source of truth!
        while self.stocks[timestamp] != -price:
            heapq.heappop(self.max_heap)
            price, timestamp = self.max_heap[0]

        return -self.max_heap[0][0]

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]
        # The stocks dictionary is the source of truth!
        while self.stocks[timestamp] != price:
            heapq.heappop(self.min_heap)
            price, timestamp = self.min_heap[0]

        return self.min_heap[0][0]


stock_price = StockPrice()
stock_price.update(1, 10)
stock_price.update(2, 5)
print(stock_price.current())
print(stock_price.maximum())
stock_price.update(1, 3)
print(stock_price.maximum())
stock_price.update(4, 2)
print(stock_price.minimum())
