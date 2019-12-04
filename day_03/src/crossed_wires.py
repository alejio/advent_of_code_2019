import csv
import os
from typing import List, Tuple

import click


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


def single_move_map(starting_position: Tuple, ending_position: Tuple) -> List:
    diff_x = starting_position[0] - ending_position[0]
    diff_y = starting_position[1] - ending_position[1]
    path = list()
    if diff_x < 0:
        for i in range(-diff_x + 1):
            path.append((starting_position[0] + i, starting_position[1]))
    elif diff_x > 0:
        for i in range(diff_x + 1):
            path.append((starting_position[0] - i, starting_position[1]))
    else:
        if diff_y < 0:
            for i in range(-diff_y + 1):
                path.append((starting_position[0], starting_position[1] + i))
        elif diff_y > 0:
            for i in range(diff_y + 1):
                path.append((starting_position[0], starting_position[1] - i))
        else:
            path.append((starting_position[0], starting_position[1]))
    return path


def manhattan_distance(position_1: Tuple, position_2: Tuple) -> int:
    return abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1])


def map_full_path(movements: List[str], starting_position: Tuple=(0, 0)) -> List:
    path = list()
    position = starting_position
    for movement in movements:
        new_position = move(movement, position)
        single_path = single_move_map(position, new_position)
        position = new_position
        path = path + single_path
    return path


def find_intersections(first_path: List, second_path: List) -> set:
    intersections = set(first_path).intersection(set(second_path))
    intersections.discard((0, 0))
    return intersections


def n_steps_to_intersection(path: List, intersection: Tuple) -> int:
    return path.index(intersection)


def intersection_distances(movement_1: List, movement_2: List) -> List:
    path_1 = map_full_path(movement_1)
    path_2 = map_full_path(movement_2)
    intersections = find_intersections(path_1, path_2)
    return [manhattan_distance((0, 0), i) for i in list(intersections)]


def answers():
    wire_1, wire_2 = load_input()
    distances = intersection_distances(wire_1, wire_2)
    print('Closest crossing distance: ', min(distances))
    total_steps = []
    path_1 = map_full_path(wire_1)
    path_2 = map_full_path(wire_2)
    intersections = find_intersections(path_1, path_2)
    for intersection in intersections:
        total_steps.append(n_steps_to_intersection(path_1, intersection) + n_steps_to_intersection(path_2, intersection))
    print('Fewest combined steps: ', min(total_steps))


if __name__ == "__main__":
    answers()