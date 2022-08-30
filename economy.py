import math


class Economy:

    # CONSTS #
    SEED_A = 1
    SEED_B = 1
    GROW_A = 1
    GROW_B = 1
    HARVEST_A = 1
    HARVEST_B = 1
    SELL_A = 1
    SELL_B = 1
    # END - CONSTS #

    def __init__(self,
                 money: float):
        self.money = money

    def seed(self, n):
        self.money -= Economy.SEED_A * math.log(n, base=math.e) + Economy.SEED_B

    def grow(self, n):
        self.money -= Economy.GROW_A * math.log(n, base=math.e) + Economy.GROW_B

    def harvest(self, n):
        self.money -= Economy.HARVEST_A * math.log(n, base=math.e) + Economy.HARVEST_B

    def sell(self, n):
        self.money += Economy.SELL_A * n - Economy.SELL_B * math.log(n, base=math.e)
