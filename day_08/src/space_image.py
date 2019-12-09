import csv
import os
from typing import List


def parser(input_text: str) -> List:
    return [int(i) for i in input_text]


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return parser(list(reader)[0][0])


def create_image(data: List, dim_x: int, dim_y: int) -> List:
    output = []
    n_layers = len(data) / (dim_x * dim_y)
    for n_layer in range(n_layers):
        layer = [data[0:(dim_x+1)], data[dim_x+1:dim_x+1+dim_y+1]]

    return output