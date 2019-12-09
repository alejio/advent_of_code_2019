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


def all_nodes(data: List) -> List:
    nodes = set()
    for item in data:
        pair = item.split(')')
        for node in pair:
            nodes.add(node)
    return nodes


def create_graph(data: List) -> Dict[str, List[str]]:
    graph = {}
    for orbit in data:
        pair = orbit.split(')')
        assert len(pair) == 2, 'Failed graph creation: corrupt data!'
        if pair[0] in graph.keys():
            value = graph[pair[0]]
            value.append(pair[1])
            graph[pair[0]] = value
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
    if len(paths) > 0:
        for path in paths:
            if len(path) > 0:
                return len(path) - 1
            else:
                return 0
    return 0


def find_shortest_path(graph: Dict, node_1: str, node_2: str) -> set:
    node_1_path = find_all_paths(graph, 'COM', node_1)[0]
    node_2_path = find_all_paths(graph, 'COM', node_2)[0]
    common_path = [i for i, j in zip(node_1_path, node_2_path) if i == j]
    steps_1 = set(node_1_path) - set(common_path)
    return steps_1


@click.command()
def total_orbits(part: int=2):
    data = load_input()
    nodes = list(all_nodes(data))
    graph = create_graph(data)
    if part == 1:
        total_distance = 0
        for node_1 in nodes:
            if node_1 != 'COM':
                paths = find_all_paths(graph, 'COM', node_1)
                total_distance += max_distance(paths)
        print(total_distance)
    else:
        shortest_path = find_shortest_path(graph, 'SAN', 'YOU')
        print(len(shortest_path))


if __name__ == '__main__':
    total_orbits()