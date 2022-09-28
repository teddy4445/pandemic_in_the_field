# library imports
import os
import math

# project imports
from plotter import Plotter


def run():
    mean_economic = [-0.13 - 0.05 * i + math.log() for i in range(89)]

    Plotter.sim_multi_run_raw(mean_economic=mean_economic,
                              mean_pandemic=mean_pandemic,
                              std_pandemic=std_pandemic,
                              std_economic=std_economic,
                              save_path=os.path.join(os.path.dirname(__file__), "results", "baseline_{}.pdf".format("small")))

    Plotter.sim_multi_run_raw(mean_economic=mean_economic,
                              mean_pandemic=mean_pandemic,
                              std_pandemic=std_pandemic,
                              std_economic=std_economic,
                              save_path=os.path.join(os.path.dirname(__file__), "results", "baseline_{}.pdf".format("meduim")))

    Plotter.sim_multi_run_raw(mean_economic=mean_economic,
                              mean_pandemic=mean_pandemic,
                              std_pandemic=std_pandemic,
                              std_economic=std_economic,
                              save_path=os.path.join(os.path.dirname(__file__), "results", "baseline_{}.pdf".format("large")))

    Plotter.sensitivity(x=field_sizes,
                        economic_mean=economic_mean,
                        economic_std=economic_std,
                        pandemic_mean=pandemic_mean,
                        pandemic_std=pandemic_std,
                        label="Field size",
                        save_path=os.path.join(os.path.dirname(__file__), Experiments.RESULTS,
                                               "sens_fieldsize.pdf"))


if __name__ == '__main__':
    run()
