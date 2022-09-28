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
        EpiState.I: COLORS[1],
        EpiState.R: COLORS[2],
    }
    epi_symbols = {
        EpiState.S: "o",
        EpiState.I: "^",
        EpiState.R: "*",
    }

    def __init__(self):
        pass

    @staticmethod
    def plot_2d_state(population: Population):
        pass
        # TODO: finish later

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

    @staticmethod
    def sim_multi_run_raw(mean_economic: np.ndarray,
                          std_economic: np.ndarray,
                          mean_pandemic: np.ndarray,
                          std_pandemic: np.ndarray,
                          save_path: str):
        fig, ax = plt.subplots(figsize=(10, 10))

        ax.plot(range(len(mean_pandemic)),
                mean_pandemic,
                "-x",
                color="red",
                label="Basic reproduction number")
        ax.fill_between(range(len(mean_pandemic)),
                        mean_pandemic - std_pandemic,
                        mean_pandemic + std_pandemic,
                        color="red",
                        alpha=0.25)
        ax.set_xlabel("Days [t]")
        ax.set_ylabel("Basic reproduction number", color="red")

        ax2 = ax.twinx()

        ax2.plot(range(len(mean_economic)),
                 mean_economic,
                 "-o",
                 color="blue",
                 label="Economic profit")
        ax2.fill_between(range(len(mean_economic)),
                         mean_economic - std_economic,
                         mean_economic + std_economic,
                         color="blue",
                         alpha=0.25)
        ax2.set_ylabel('Economic profit', color='blue')
        plt.grid(alpha=0.5,
                 color="black")
        # plt.legend()
        plt.tight_layout()
        plt.savefig(save_path, dpi=400)
        plt.close()

    @staticmethod
    def sim_multi_run(economic: np.ndarray,
                      r_zero: np.ndarray,
                      save_path: str):
        mean_economic = economic.mean(axis=0)
        std_economic = economic.std(axis=0)
        mean_pandemic = r_zero.mean(axis=0)
        std_pandemic = r_zero.std(axis=0)
        Plotter.sim_multi_run_raw(mean_pandemic=mean_pandemic,
                                  std_economic=std_economic,
                                  mean_economic=mean_economic,
                                  std_pandemic=std_pandemic,
                                  save_path=save_path)

    @staticmethod
    def sensitivity(x: list,
                    economic_mean: list,
                    economic_std: list,
                    pandemic_mean: list,
                    pandemic_std: list,
                    label: str,
                    save_path: str):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.errorbar(x=x,
                    y=pandemic_mean,
                    yerr=pandemic_std,
                    fmt="--o",
                    markersize=3,
                    ecolor="red",
                    color="red",
                    capsize=4)
        ax.set_xlabel("{}".format(label))
        ax.set_ylabel("Basic reproduction number", color="red")

        ax2 = ax.twinx()

        ax.errorbar(x=x,
                    y=economic_mean,
                    yerr=economic_std,
                    fmt="--x",
                    markersize=3,
                    ecolor="blue",
                    color="blue",
                    capsize=4)

        ax2.set_ylabel('Economic profit', color='blue')
        plt.grid(alpha=0.5,
                 color="black")
        # plt.legend()
        plt.tight_layout()
        plt.savefig(save_path, dpi=400)
        plt.close()
