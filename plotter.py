# library imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# project imports
from epi_state import EpiState
from simulator import Simulator
from population import Population


class Plotter:
    """
    A class to generate graphs from the simulation's data
    """

    COLORS = ["#4285F4", "#a83489", "#111111", "#34A853", "#FBBC05", "#EA4335", "#7a150d"]
    STYLES = ["-o", "-s", "-^", "--^", "-P", "--P", "-D"]
    LABELS = ["S", "E", "$I^a$", "$I^s$", "$R^f$", "$R^p$", "D"]
    DPI = 600

    epi_colors = {
        EpiState.S: COLORS[0],
        EpiState.E: COLORS[1],
        EpiState.I: COLORS[2],
        EpiState.R: COLORS[3],
        EpiState.D: COLORS[4]
    }
    epi_symbols = {
        EpiState.S: "o",
        EpiState.E: "^",
        EpiState.I: "P",
        EpiState.R: "*",
        EpiState.D: ">"
    }

    def __init__(self):
        pass

    @staticmethod
    def plot_2d_state(population: Population):
        pass
        #TODO: finish later

    @staticmethod
    def plot_sim_economy(sim: Simulator,
                         save_path: str):
        plt.plot(range(len(sim.economy_history)),
                 sim.economy_history,
                 "--o",
                 markersize=2,
                 color="blue")
        plt.xlabel("Steps")
        plt.ylabel("Economic output")
        plt.grid(alpha=0.5,
                 color="black")
        plt.tight_layout()
        plt.savefig(save_path, dpi=400)
        plt.close()

    @staticmethod
    def plot_sim_pandemic(sim: Simulator,
                          save_path: str):
        states = {name: [] for name, val in sim.pandemic_history[0].items()}
        for state in sim.pandemic_history:
            for key, val in state.items():
                states[key].append(val)
        for name, epi in states.items():
            plt.plot(range(len(states[name])),
                     states[name],
                     "--{}".format(Plotter.epi_symbols[name]),
                     color=Plotter.epi_colors[name],
                     label="{}".format(name))
        plt.xlabel("Steps")
        plt.ylabel("Normalized epidemiological state")
        plt.grid(alpha=0.5,
                 color="black")
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path, dpi=400)
        plt.close()
