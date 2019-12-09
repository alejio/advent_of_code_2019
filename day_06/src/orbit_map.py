import csv
import os
from typing import List, Dict

import click


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [i[0] for i in list(reader)]


def create_graph() -> Dict[str, List[str]]:
    all_orbits = load_input()
    graph = {}
    for orbit in all_orbits:
        pair = orbit.split(')')
        assert len(pair) == 2, 'Failed graph creation: corrupt data!'
        if pair[0] in graph:
            value = graph[pair[0]]
            graph[pair[0]] = value.append(pair[1])
        else:
            graph[pair[0]] = pair[1:]
    return graph


def find_all_paths(graph: Dict[str, List[str]], start: str, end: str, path: List=[]) -> List:
    # Adapted from https://www.python.org/doc/essays/graphs/
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def max_distance(paths: List) -> int:
    for path in paths:
        if len(path) > 0:
            return len(path) - 1
        else:
            return 0


@click.command()
def total_orbits():
    graph = create_graph(load_input())
    total_distance = 0
    for node in graph:
        paths = find_all_paths(graph, 'COM', node)
        total_distance += max_distance(paths)
    print(total_distance)
    return total_distance


if __name__ == '__main__':
    total_orbits()