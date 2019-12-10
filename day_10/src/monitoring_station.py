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


def blocked_view(point: Tuple, asteroid: Tuple, map_grid: Tuple) -> List:
    assert point != asteroid, 'Wrong input - same points!'
    if point[0] == asteroid[0]:
        if point[1] < asteroid[1]:
            return [(point[0], j) for j in range(asteroid[1] + 1, map_grid[1] + 1)]
        return [(point[0], j) for j in range(0, asteroid[1])]
    if point[1] == asteroid[1]:
        if point[0] < asteroid[0]:
            return [(i, point[1]) for i in range(asteroid[0] + 1, map_grid[0] + 1)]
        return [(i, point[1]) for i in range(0, asteroid[0])]
    if (point[0] != asteroid[0]) and (point[1] != asteroid[1]):
        midpoint = (point[0] + asteroid[0]) / 2, (point[1] + asteroid[1]) / 2
    interval_x = midpoin
    return


def count_visible_asteroids(idx: int, asteroids: List, map_grid: Tuple) -> int:
    station = asteroids[idx]
    for asteroid in asteroids:
        if asteroid != station:

    visible_asteroids = 0
    return visible_asteroids
