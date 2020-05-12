class Assets:
    def __init__(self, liquid_assets, invested_assets):
        self._liquid_assets = liquid_assets
        self._invested_assets = invested_assets
        self._asset_value = None

    def change_liquid_assets(self, amount, new_value = False):
        if new_value:
            self._liquid_assets = amount
        else:
            self._liquid_assets += amount

    def invest_assets(self, amount = None):
        if not amount:
            self._invested_assets += self._liquid_assets
        else:
            if self._liquid_assets < amount:
                print('Insufficient funds.')
            else:
                self._invested_assets -= amount

    def get_liquid_assets(self):
        return self._liquid_assets

    def get_invested_assets(self):
        return self._invested_assets

    def calculate_asset_value(self, percent_change):
        self._asset_value = self._invested_assets / 100 * percent_change
        print("Asset Value: " + str(self._asset_value))

    def sell_assets(self):
        increase_amount = self.get_increase_amount()
        self._liquid_assets = self._asset_value
        self._asset_value = 0
        self._invested_assets = 0
        print(str(self._liquid_assets) + " in assets sold")
        print(f'Value added: {str(increase_amount)}')

    def get_increase_amount(self):
        return self._asset_value - self._invested_assets


# FIND LOSS TOLERANCE PRICE
# decimal = loss_tolerance / 100
# loss_amount = decimal * initial_investment
# loss_tolerance_price = initial_investment - loss_amount

# FIND CURRENT INCREASE PERCENT
# Increase = current_price - initial_price
# increase_percent = increase / initial_price * 100

# FIND CURRENT DECREASE PERCENT
# Decrease = initial_price - current_price
# decrease_percent = decrease / initial_price * 100

# assets_value = invested_assets / 100 * gain




