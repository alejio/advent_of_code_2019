import click
import os
from typing import List
import csv


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [int(i) for i in list(reader)[0]]


def restore_1202_state():
    return

if __name__ == '__main__':
    restore_1202_state()