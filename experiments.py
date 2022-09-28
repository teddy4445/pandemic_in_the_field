# library imports
import os
import numpy as np

# project imports
from agent import Agent
from plotter import Plotter
from economy import Economy
from simulator import Simulator
from population import Population


class Experiments:
    """
    Single entry point
    """

    # CONSTS #
    RESULTS = "results"
    INFECTION_COUNT = 1
    # END - CONSTS #

    def __init__(self):
        pass

    @staticmethod
    def run_all():
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), Experiments.RESULTS))
        except:
            pass
        Experiments.baseline()
        Experiments.sensitivity()

    @staticmethod
    def baseline():
        max_repeat = 20
        # small field
        for size_name, size in {"small": (100, 100), "meduim": (500, 500), "large": (2500, 2500)}.items():
            economy_signals = []
            r_zero_signals = []
            for repeat in range(max_repeat):
                print("Experiments.baseline: {} #{}/{}".format(size_name, repeat+1, max_repeat))

                sim = Simulator(population=Population.initialize_grid(height=size[0],
                                                                      width=size[1],
                                                                      d_x=25,
                                                                      d_y=5,
                                                                      infected_count=Experiments.INFECTION_COUNT),
                                economy=Economy())
                sim.run(duration=90)
                economy_signals.append(sim.economy_history)
                r_zero_signals.append(sim.r_zero_history)
            economy_signals = np.asarray(economy_signals)
            r_zero_signals = np.asarray(r_zero_signals)
            Plotter.sim_multi_run(economic=economy_signals,
                                  r_zero=r_zero_signals,
                                  save_path=os.path.join(os.path.dirname(__file__), Experiments.RESULTS, "baseline_{}.pdf".format(size_name)))

    @staticmethod
    def sensitivity():
        max_repeat = 5
        # small field
        economic_mean = []
        pandemic_mean = []
        economic_std = []
        pandemic_std = []
        field_sizes = [100 * (1+i) for i in range(11)]
        for field_size in field_sizes:
            economy_signals = []
            r_zero_signals = []
            for repeat in range(max_repeat):
                print("Experiments.sensitivity: field size - {} #{}/{}".format(field_size, repeat+1, max_repeat))

                sim = Simulator(population=Population.initialize_grid(height=field_size,
                                                                      width=field_size,
                                                                      d_x=25,
                                                                      d_y=5,
                                                                      infected_count=Experiments.INFECTION_COUNT),
                                economy=Economy())
                sim.run(duration=90)
                economy_signals.append(sim.economy_history[-1])
                r_zero_signals.append(np.mean(sim.r_zero_history))
            economic_mean.append(np.mean(economy_signals))
            economic_std.append(np.std(economy_signals))
            pandemic_mean.append(np.mean(r_zero_signals))
            pandemic_std.append(np.std(r_zero_signals))
        Plotter.sensitivity(x=field_sizes,
                            economic_mean=economic_mean,
                            economic_std=economic_std,
                            pandemic_mean=pandemic_mean,
                            pandemic_std=pandemic_std,
                            label="Field size",
                            save_path=os.path.join(os.path.dirname(__file__), Experiments.RESULTS, "sens_fieldsize.pdf"))


if __name__ == '__main__':
    Experiments.run_all()
