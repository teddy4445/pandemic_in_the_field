import math


class Economy:

    # CONSTS #
    SEED_A = 2
    SEED_B = 0.25
    GROW_A = 0.25
    GROW_B = 0.05
    HARVEST_A = 2
    HARVEST_B = 0.25
    SELL_A = 2
    SELL_B = 1.5
    # END - CONSTS #

    def __init__(self,
                 money: float = 0):
        self.money = money

    def seed(self, n):
        self.money -= Economy.SEED_A * math.log(n, math.e) + Economy.SEED_B

    def grow(self, n):
        try:
            self.money -= Economy.GROW_A * math.log(n, math.e) + Economy.GROW_B
        except:
            pass

    def harvest(self, n):
        try:
            self.money -= Economy.HARVEST_A * math.log(n, math.e) + Economy.HARVEST_B
        except:
            pass

    def sell(self, n):
        try:
            self.money += Economy.SELL_A * n - Economy.SELL_B * math.log(n, math.e)
        except:
            pass


    def __str__(self):
        return str(self.money)

    def __repr__(self):
        return str(self.money)
