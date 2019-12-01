from typing import List
import csv
import os
import math


def module_fuel_calculator(mass: int) -> int:
    return math.trunc(mass/3) - 2


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        out = list(reader)
        return [int(i[0]) for i in out]


def calculate_total_fuel() -> int:
    module_masses = load_input()
    return sum([module_fuel_calculator(mass) for mass in module_masses])


if __name__ == "__main__":
    print(calculate_total_fuel())