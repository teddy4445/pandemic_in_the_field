# library imports
import os

# project imports
from agent import Agent
from plotter import Plotter
from economy import Economy
from simulator import Simulator
from population import Population


class Main:
    """
    Single entry point
    """

    def __init__(self):
        pass

    @staticmethod
    def run():
        sim = Simulator(population=Population.initialize_grid(height=100,
                                                              width=100,
                                                              d_x=25,
                                                              d_y=5,
                                                              infected_count=3),
                        economy=Economy())
        sim.run(duration=100)
        Plotter.plot_sim_economy(sim=sim,
                                 save_path=os.path.join(os.path.dirname(__file__), "economy.pdf"))
        Plotter.plot_sim_pandemic(sim=sim,
                                  save_path=os.path.join(os.path.dirname(__file__), "pandemic.pdf"))


if __name__ == '__main__':
    Main.run()
