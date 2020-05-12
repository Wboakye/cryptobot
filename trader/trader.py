from price_watcher import PriceWatcher
from assets import Assets
from prices import Prices


class Trader:
    def __init__(self, loss_tolerance, liquid_assets = 0, invested_assets = 0):
        self.assets = Assets(liquid_assets, invested_assets)
        self.price = Prices()
        self.price_watcher = PriceWatcher(self)

        self.initial_investment = None
        self.loss_tolerance = loss_tolerance
        self.loss_tolerance_price = None
        self.gain_threshold_met = False
        self.assets_are_liquid = True
        self.is_trading = True


    def start(self):
        self.price_watcher.start()

    def assess_prices(self, current_price):
        if not self.is_trading:
            print("NOT TRADING: " + str(current_price))
        else:
            print("TRADING: " + str(current_price))

            self.price.update_prices(current_price)

            self.assets.calculate_asset_value(self.price.percent_change)
            print(str(self.assets.get_increase_amount()) + " in total value added")

            if self.loss_tolerance_price is None:
                self.calculate_loss_tolerance_price()

            if self.price.percent_change > 5:
                self.gain_threshold_met = True

            if self.gain_threshold_met:
                self.threshold_met_strategy()
            else:
                self.threshold_not_met_strategy()



    def calculate_loss_tolerance_price(self):
        decimal = self.loss_tolerance / 100
        loss_amount = decimal * self.price.initial_price
        self.loss_tolerance_price = self.price.initial_price - loss_amount

    def threshold_met_strategy(self):
        sell_price = self.price.high_price - self.price.initial_price / 2
        if sell_price > self.price.current_price:
            #sell, record
            pass

    def threshold_not_met_strategy(self):
        if self.loss_tolerance_price > self.price.current_price:
            #sell, record
            pass

    def reset(self):
        self.initial_investment = None
        self.loss_tolerance_price = None
        self.gain_threshold_met = False
        self.assets_are_liquid = True


