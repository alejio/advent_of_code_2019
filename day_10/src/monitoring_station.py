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


def vertical_block(point: Tuple, asteroid: Tuple, map_grid: Tuple) -> List:
    # Check vertical block
    if point[0] == asteroid[0]:
        # Asteroid is above
        if point[1] < asteroid[1]:
            return [(point[0], j) for j in range(asteroid[1] + 1, map_grid[1] + 1)]
        # Asteroid is below
        return [(point[0], j) for j in range(0, asteroid[1])]
    else:
        return []

def horizontal_block(point: Tuple, asteroid: Tuple, map_grid: Tuple) -> List:
    # Check horizontal block
    if point[1] == asteroid[1]:
        # Asteroid is to the right
        if point[0] < asteroid[0]:
            return [(i, point[1]) for i in range(asteroid[0] + 1, map_grid[0] + 1)]
        # Asteroid is to the left
        return [(i, point[1]) for i in range(0, asteroid[0])]
    return []

def other_block(point: Tuple, asteroid: Tuple, map_grid: Tuple) -> List:
    if (point[0] != asteroid[0]) and (point[1] != asteroid[1]):
        # Normal diagonal
        if (point[0] == point[1]) and (asteroid[0] == asteroid[1]):
            # Asteroid is down right
            if point[0] < asteroid[0]:
                return [(i, j) for i in range(asteroid[0] + 1, map_grid[0] + 1) for j in
                        range(asteroid[1] + 1, map_grid[1] + 1)]
            # Asteroid is up left
            return [(i, j) for i in range(0, asteroid[0]) for j in
                    range(0, asteroid[1])]
        # Reverse diagonal
        elif (point[0] + point[1]) == (asteroid[0] + asteroid[1]) == map_grid[0]:
            # Asteroid is up right
            if point[0] < asteroid[0]:
                return [(i, j) for i in range(asteroid[0] + 1, map_grid[0] + 1) for j in range(0, asteroid[1])]
            # Asteroid is down left
            return [(i, j) for i in range(0, asteroid[0]) for j in range(asteroid[1], map_grid[1] + 1)]
        else:
            # TODO
            return []


def blocked_view(point: Tuple, asteroid: Tuple, map_grid: Tuple) -> List:
    # assert point != asteroid, 'Wrong input - same points!'
    blocked_positions = []
    blocked_positions += vertical_block(point, asteroid, map_grid)
    blocked_positions += horizontal_block(point, asteroid, map_grid)
    blocked_positions += other_block(point, asteroid, map_grid)
    return blocked_positions


def count_visible_asteroids(idx: int, asteroids: List, map_grid: Tuple) -> int:
    station = asteroids[idx]
    n_detected_asteroids = 0
    for asteroid in asteroids:
        other_asteroids = [i for i in asteroids if (i != station) and (i != asteroid)]
        blocked_positions = blocked_view(station, asteroid)
        n_detected_asteroids += len(set(other_asteroids) - set(blocked_positions))



    visible_asteroids = 0
    return visible_asteroids
