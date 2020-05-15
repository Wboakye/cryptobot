class Prices:
    def __init__(self):
        self.initial_price = None
        self.high_price = None
        self.current_price = None
        self.low_price = None
        self.percent_change = 0

    def set_initial_prices(self, initial_price):
        self.initial_price = initial_price
        self.current_price = initial_price
        self.high_price = initial_price
        self.low_price = initial_price
        print(f'Initial investment is at price {str(self.initial_price)}')

    def update_prices(self, current_price):
        if self.initial_price is None:
            self.set_initial_prices(current_price)
        else:
            self.current_price = current_price
            self.calculate_change()
            self.update_extremes()

    def update_extremes(self):
        if self.current_price > self.high_price:
            self.high_price = self.current_price
        if self.current_price < self.low_price:
            self.low_price = self.current_price

    def calculate_change(self):
        change = self.current_price - self.initial_price
        self.percent_change = change / self.initial_price * 100
        #print(f'PERCENT CHANGE RAW: {self.percent_change}')


