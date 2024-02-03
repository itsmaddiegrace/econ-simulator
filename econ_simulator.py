# econ_simulator.py

import pandas as pd
import numpy as np

class EconSimulator:
    def __init__(self, initial_balance=100000, num_periods=12):
        self.balance = initial_balance
        self.num_periods = num_periods
        self.market_data = self.generate_market_data()

    def generate_market_data(self):
        np.random.seed(42)
        market_data = pd.DataFrame({
            'Period': np.arange(1, self.num_periods + 1),
            'Price': np.random.randint(80, 120, self.num_periods)
        })
        return market_data

    def run_simulation(self):
        for period in range(1, self.num_periods + 1):
            price = self.market_data.loc[period - 1, 'Price']
            quantity = self.make_trading_decision(price)
            self.execute_trade(price, quantity)
            self.display_balance(period)

    def make_trading_decision(self, current_price):
        return np.random.randint(1, 10)

    def execute_trade(self, price, quantity):
        cost = price * quantity
        self.balance -= cost

    def display_balance(self, period):
        print(f"Economic Simulator - Period {period}: Balance - ${self.balance}")
