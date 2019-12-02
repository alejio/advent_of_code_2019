import click
import os
from typing import List
import csv

operation_opcodes = {'addition': 1, 'multiplication': 2, 'halt': 99}


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [int(i) for i in list(reader)[0]]


def add(sequence: List[int], integer_list: List[int]) -> List[int]:
    assert sequence[0] == operation_opcodes['addition']
    assert len(sequence) == 4
    integer_list[sequence[3]] = integer_list[sequence[1]] + integer_list[sequence[2]]
    return integer_list


def multiply(sequence: List[int], integer_list: List[int]) -> List[int]:
    assert sequence[0] == operation_opcodes['multiplication']
    assert len(sequence) == 4
    integer_list[sequence[3]] = integer_list[sequence[1]] * integer_list[sequence[2]]
    return integer_list


def halt(sequence: List[int], integer_list: List[int]) -> List[int]:
    assert sequence[0] == 99
    assert len(sequence) == 1
    return integer_list


def intcode_processor(integer_list: List[int]) -> List[int]:
    i = 0
    while i < len(integer_list):
        if integer_list[i] == operation_opcodes['addition']:
            integer_list = add(integer_list[i:i+4], integer_list)
            i += 4
        elif integer_list[i] == operation_opcodes['multiplication']:
            integer_list = multiply(integer_list[i:i+4], integer_list)
            i += 4
        elif integer_list[i] == operation_opcodes['halt']:
            integer_list = halt(integer_list[i:i+1], integer_list)
            return integer_list
        else:
            raise Exception('Invalid opcode: ', i)
    return integer_list


def restore_1202_state():
    return

if __name__ == '__main__':
    restore_1202_state()