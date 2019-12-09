import csv
import os
from typing import List, Dict


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
