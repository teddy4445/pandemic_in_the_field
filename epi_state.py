from enum import Enum


class EpiState(Enum):
    S = 1
    E = 2
    I = 3
    R = 4
    D = 5