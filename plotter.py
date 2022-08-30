# library imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# project imports
from population import Population


class Plotter:
    """
    A class to generate graphs from the simulation's data
    """

    COLORS = ["#4285F4", "#a83489", "#111111", "#34A853", "#FBBC05", "#EA4335", "#7a150d"]
    STYLES = ["-o", "-s", "-^", "--^", "-P", "--P", "-D"]
    LABELS = ["S", "E", "$I^a$", "$I^s$", "$R^f$", "$R^p$", "D"]
    DPI = 600

    def __init__(self):
        pass

    @staticmethod
    def plot_2d_state(population: Population):
        pass
        #TODO: finish later

    @staticmethod
    def plot_sim_economy(population: Population):
        pass
        #TODO: finish later

    @staticmethod
    def plot_sim_pandemic(population: Population):
        pass
        #TODO: finish later
