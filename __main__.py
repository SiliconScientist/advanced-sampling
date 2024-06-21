from config import Config
import toml
from ase import units
from ase.md.langevin import Langevin
from ase.io import read, write
from ase.constraints import FixAtoms
import numpy as np
import time
from mace.calculators import MACECalculator


def main():
    config = Config(**toml.load("config.toml"))

    print(f"Hello, world #{config.random_seed}")


if __name__ == "__main__":
    main()
