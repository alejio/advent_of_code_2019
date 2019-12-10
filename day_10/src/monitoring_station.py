import csv
import os
from typing import List, Tuple
import re


def load_input() -> List:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [i[0] for i in list(reader)]


def get_dimensions(data: List) -> Tuple:
    return len(data), len(data[0])


def get_asteroid_positions(data: List) -> List:
    asteroid_positions = []
    for idx, row in enumerate(data):
        asteroid_positions += [(idx, asteroid.start()) for asteroid in re.finditer('#', row)]
    return asteroid_positions



def count_asteroids(map: List) -> int:
    return