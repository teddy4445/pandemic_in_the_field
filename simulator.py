# library imports
import os

# project imports
from economy import Economy
from population import Population


class Simulator:

    def __init__(self,
                 population: Population,
                 economy: Economy):
        self.population = population
        self.economy = economy

        # states
        self.pandemic_history = []
        self.economy_history = []
        self.n_history = [len(self.population.agents)]

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

