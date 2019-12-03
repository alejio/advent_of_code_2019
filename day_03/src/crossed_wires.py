import csv
import os
from typing import List


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


def move(movement: str, starting_position: List=[0, 0]) -> List:
    assert len(starting_position) == 2
    assert isinstance(starting_position[0], int)
    assert isinstance(starting_position[1], int)
    distance = int(movement[1:])
    direction = movement[0]
    if direction == 'R':
        return [starting_position[0], starting_position[1] + distance]
    elif direction == 'L':
        return [starting_position[0], starting_position[1] - distance]
    elif direction == 'U':
        return [starting_position[0] + distance, starting_position[1]]
    elif direction == 'D':
        return [starting_position[0] - distance, starting_position[1]]
    else:
        print('Wrong direction')

