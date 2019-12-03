import csv
import os
from typing import List, Tuple


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


def move(movement: str, starting_position: Tuple=(0, 0)) -> Tuple:
    assert len(starting_position) == 2
    assert isinstance(starting_position[0], int)
    assert isinstance(starting_position[1], int)
    distance = int(movement[1:])
    direction = movement[0]
    if direction == 'R':
        return starting_position[0], starting_position[1] + distance
    elif direction == 'L':
        return starting_position[0], starting_position[1] - distance
    elif direction == 'U':
        return starting_position[0] + distance, starting_position[1]
    elif direction == 'D':
        return starting_position[0] - distance, starting_position[1]
    else:
        print('Wrong direction')


def manhattan_distance(vector_1: Tuple, vector_2: Tuple) -> int:
    return abs(vector_1[0] - vector_2[0]) + abs(vector_1[1] - vector_2[1])


def map_path(movements: List[str], starting_position: Tuple=(0, 0)) -> set:
    path = {starting_position}
    position = starting_position
    for movement in movements:
        position = move(movement, position)
        path.add(position)
    return path


def find_intersections(first_path: set, second_path: set) -> set:
    return first_path.intersection(second_path)
#
# @click.command()
# def find_closest_crossing():
#     lao