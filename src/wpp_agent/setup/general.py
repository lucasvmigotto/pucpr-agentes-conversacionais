from numpy.random import seed as np_seed

from ..settings import Settings


def setup_general(settings: Settings) -> None:
    np_seed(settings.UTILS.SEED)
