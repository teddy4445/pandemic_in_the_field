# library imports

# project imports
from epi_state import EpiState


class Agent:

    def __init__(self,
                 x: int,
                 y: int,
                 state: EpiState,
                 clock: int = 0):
        self.x = x
        self.y = y
        self.state = state
        self.clock = clock

    def tick(self):
        self.clock += 1

    def infect(self):
        self.state = EpiState.I

    def removed(self):
        self.state = EpiState.R

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{} (c={})".format(self.state, self.clock)

