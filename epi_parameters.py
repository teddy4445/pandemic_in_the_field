from enum import Enum


class EpiParm(Enum):
    basic_beta = 5
    e_to_i = 3
    i_to_r_d = 7
    recovery_rate = 0.8
