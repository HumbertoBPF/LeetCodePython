class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        n = len(self.stocks)
        # This index will be used to browse the cached stocks, but, after the iteration, it will be equal to the number
        # of past days when the stock price was lower than or equal to today's price
        i = 0

        while i < n:
            stock_price, stock_span = self.stocks[n - 1 - i]
            if stock_price > price:
                break
            # We use the span of the current stock to skip some days
            i += stock_span
        # Add one to take into account today
        today_span = i + 1
        # Cache today's stock price and span for later
        self.stocks.append((price, i + 1))

        return today_span
