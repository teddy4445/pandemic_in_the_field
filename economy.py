import math


class Economy:

    # CONSTS #
    SEED_A = 1
    SEED_B = 1
    GROW_A = 0.1
    GROW_B = 0.75
    HARVEST_A = 1
    HARVEST_B = 1
    SELL_A = 5
    SELL_B = 0.5
    # END - CONSTS #

    def __init__(self,
                 money: float = 0):
        self.money = money

    def seed(self, n):
        self.money -= Economy.SEED_A * math.log(n, math.e) + Economy.SEED_B

    def grow(self, n):
        self.money -= Economy.GROW_A * math.log(n, math.e) + Economy.GROW_B

    def harvest(self, n):
        self.money -= Economy.HARVEST_A * math.log(n, math.e) + Economy.HARVEST_B

    def sell(self, n):
        self.money += Economy.SELL_A * n - Economy.SELL_B * math.log(n, math.e)

    def __str__(self):
        return str(self.money)

    def __repr__(self):
        return str(self.money)
