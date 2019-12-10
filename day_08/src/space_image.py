import csv
import os
from typing import List, Dict
import collections

import click


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
    layer_size = dim_x * dim_y
    n_layers = int(len(data) / (dim_x * dim_y))
    for n_layer in range(n_layers):
        layer_data = data[n_layer*layer_size:n_layer*layer_size + layer_size]
        layer = []
        for j in range(dim_y):
            layer.append(layer_data[j * dim_x: j * dim_x + dim_x])
        output.append(layer)
    return output


def count_digits_in_layer(layer: List, digit: int) -> Dict:
    flat_layer = sum(layer, [])
    counter = collections.Counter(flat_layer)
    return counter[digit]


def find_fewest_zeros_layer(image: List) -> List:
    zeros = {}
    for idx, layer in enumerate(image):
        zeros[idx] = count_digits_in_layer(layer, 0)
    return min(zeros, key=zeros.get)


def layer_stack(image: List) -> List:
    dim_x = len(image[0][0])
    dim_y = len(image[0])
    n_layers = len(image)
    final_image = []
    for j in range(dim_y):
        final_image.append([])
        for i in range(dim_x):
            for n in range(n_layers):
                pixel = image[n][j][i]
                if pixel != 2:
                    final_image[j].append(pixel)
                    break
    return final_image


def print_image(image: List):
    for line in image:
        stringy_line = ''
        for digit in line:
            if digit == 0:
                stringy_line += ' '
            else:
                stringy_line += str(digit)
        print(stringy_line)

@click.command()
def calculation(part: int=2):
    data = load_input()
    image = create_image(data, 25, 6)
    if part == 1:
        layer_idx = find_fewest_zeros_layer(image)
        number_of_1s = count_digits_in_layer(image[layer_idx], 1)
        number_of_2s = count_digits_in_layer(image[layer_idx], 2)
        print(number_of_1s * number_of_2s)
    else:
        final_image = layer_stack(image)
        print_image(final_image)


if __name__ == '__main__':
    calculation()