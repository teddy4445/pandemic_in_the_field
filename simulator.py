# library imports
import os

# project imports
from economy import Economy
from epi_state import EpiState
from population import Population


class Simulator:

    def __init__(self,
                 population: Population,
                 economy: Economy):
        self.population = population
        self.economy = economy

        # states
        self.pandemic_history = []
        self.r_zero_history = []
        self.economy_history = []
        self.n_history = [len(self.population.agents)]
        self._initial_pip_size = population.count_n()

    def run(self, duration: int):
        [self.run_step(step=step,
                       duration=duration)
         for step in range(duration)]

    def run_step(self,
                 step: int,
                 duration: int):
        print("Running step #{} ({:.3f}%) | N = {}".format(step+1,
                                                           100*(step+1)/duration,
                                                           self.n_history[step]))
        if step == 0:
            self.economy.seed(self.population.count_n())

        self.population.tick()
        self.population.pairwise_infect()
        self.population.update_spontaneous_epi_state()
        self.economy.grow(self.population.count_n())

        if step == duration-1:
            self.economy.harvest(self.population.count_n())
            self.economy.sell(self.population.count_n())

        self.gather_states()

    def gather_states(self):
        self.pandemic_history.append(self.population.epi_distribution())
        self.economy_history.append(self.economy.money)
        self.n_history.append(self.population.count_n())
        self.r_zero_history.append(self.r_zero() if len(self.pandemic_history) > 2 else 0)

    def r_zero(self):
        delta_i = abs(self.pandemic_history[-1][EpiState.I] - self.pandemic_history[-2][EpiState.I]) * self._initial_pip_size
        delta_r = abs(self.pandemic_history[-1][EpiState.R] - self.pandemic_history[-2][EpiState.R]) * self._initial_pip_size
        if delta_r > 0:
            return delta_i/delta_r
        return delta_i
