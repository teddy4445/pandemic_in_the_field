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

    def expose(self):
        self.state = EpiState.E

    def infect(self):
        self.state = EpiState.I

    def recover(self):
        self.state = EpiState.R

    def dead(self):
        self.state = EpiState.D

