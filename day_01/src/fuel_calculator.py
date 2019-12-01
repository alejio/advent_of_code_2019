from typing import List, Optional
import csv
import os
import math
import click


def module_fuel_calculator(mass: int, complex: Optional) -> int:

    def simple_calculation(x: int) -> int:
        return max(0, math.trunc(x/3) - 2)

    fuel = list()
    fuel.append(simple_calculation(mass))
    if complex is not None:
        while fuel[-1] > 0:
            fuel_for_fuel = simple_calculation(fuel[-1])
            fuel.append(fuel_for_fuel)
    return sum(fuel)


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        out = list(reader)
        return [int(i[0]) for i in out]


@click.command()
@click.option('--complex', default=None)
def calculate_total_fuel(complex: Optional) -> int:
    module_masses = load_input()
    individual_modules_fuel = [module_fuel_calculator(mass, complex) for mass in module_masses]
    print(f"Total fuel required: {sum(individual_modules_fuel)}")


if __name__ == "__main__":
    calculate_total_fuel()