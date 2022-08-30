# library imports
import math
import itertools
from random import random

# project imports
from agent import Agent
from epi_state import EpiState
from epi_parameters import EpiParm


class Population:

    def __init__(self,
                 agents: list):
        self.agents = agents

    @staticmethod
    def initialize_grid(width: float,
                        height: float,
                        d_x: float,
                        d_y: float,
                        infected_portion: float):
        answer = [[Agent(x=x_val,
                         y=y_val,
                         state=EpiState.S if random() > infected_portion else EpiState.I,
                         clock=0)
                   for y_val in range(math.floor(height / d_y))]
                  for x_val in range(math.floor(width / d_x))]
        return Population(agents=list(itertools.chain.from_iterable(answer)))

    def tick(self):
        for agent in self.agents:
            agent.tick()

    def pairwise_infect(self):
        for i_index, i_agent in enumerate(self.agents):
            if i_agent.state == EpiState.I:
                for j_index, j_agent in enumerate(self.agents):
                    if j_agent.state == EpiState.S:
                        if random() < self.calc_beta(i_agent, j_agent):
                            j_agent.expose()

    @staticmethod
    def calc_beta(i_agent: Agent,
                  j_agent: Agent):
        try:
            return float(EpiParm.basic_beta) / math.sqrt(
                math.pow(i_agent.x - j_agent.x, 2) + math.pow(i_agent.y - j_agent.y, 2))
        except:
            return 0

    def update_spontaneous_epi_state(self):
        for agent in self.agents:
            if agent.state == EpiState.E and agent.clock >= int(EpiParm.e_to_i):
                agent.infect()
            elif agent.state == EpiState.I and agent.clock >= int(EpiParm.i_to_r_d):
                if random() < float(EpiParm.recovery_rate):
                    agent.recover()
                else:
                    agent.dead()

    def count_n(self):
        return len([True for agent in self.agents if agent.state != EpiState.D])

    def epi_distribution(self):
        answer = {EpiState.S: 0, EpiState.E: 0, EpiState.I: 0, EpiState.R: 0, EpiState.D: 0}
        for agent in self.agents:
            answer[agent.state] += 1
        for key, value in answer.items():
            answer[key] = value / len(self.agents)
        return answer

    def finish_pandemic(self):
        answer = self.epi_distribution()
        return (answer[EpiState.E] + answer[EpiState.I]) > 0
