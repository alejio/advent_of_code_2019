import click
import os
from typing import List, Tuple
import csv

operation_opcodes = {'addition': 1, 'multiplication': 2, 'halt': 99}


def load_input() -> List[int]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [int(i) for i in list(reader)[0]]


def add(sequence: List[int], integer_list: List[int]) -> List[int]:
    output_list = integer_list.copy()
    assert sequence[0] == operation_opcodes['addition']
    assert len(sequence) == 4
    output_list[sequence[3]] = output_list[sequence[1]] + output_list[sequence[2]]
    return output_list


def multiply(sequence: List[int], integer_list: List[int]) -> List[int]:
    output_list = integer_list.copy()
    assert sequence[0] == operation_opcodes['multiplication']
    assert len(sequence) == 4
    output_list[sequence[3]] = output_list[sequence[1]] * output_list[sequence[2]]
    return output_list


def halt(sequence: List[int], integer_list: List[int]) -> List[int]:
    assert sequence[0] == 99
    assert len(sequence) == 1
    return integer_list


def intcode_processor(integer_list: List[int]) -> List[int]:
    output_list = integer_list.copy()
    i = 0
    while i < len(output_list):
        if output_list[i] == operation_opcodes['addition']:
            output_list = add(output_list[i:i+4], output_list)
            i += 4
        elif output_list[i] == operation_opcodes['multiplication']:
            output_list = multiply(output_list[i:i+4], output_list)
            i += 4
        elif output_list[i] == operation_opcodes['halt']:
            output_list = halt(integer_list[i:i+1], output_list)
            return output_list
        else:
            raise Exception('Invalid opcode: ', i)
    return output_list


def alter_state(noun: int, verb: int, integer_list: List[int]) -> List[int]:
    output_list = integer_list.copy()
    output_list[1] = noun
    output_list[2] = verb
    return output_list


def noun_verb_search(integer_list: List[int], search_value: int) -> Tuple:
    for noun in range(0, 100):
        for verb in range(0, 100):
            output_list = alter_state(noun, verb, integer_list)
            if intcode_processor(output_list)[0] == search_value:
                return noun, verb


@click.command()
@click.option('--part', default=2)
def position_0_value(part: int):
    integer_list = load_input()
    print(part)
    if part == 1:
        integer_list = alter_state(12, 2, integer_list)
        print('Integer at position 0: ', intcode_processor(integer_list)[0])
    elif part == 2:
        noun, verb = noun_verb_search(integer_list, 19690720)
        print('Answer is: ', 100 * noun + verb)
    else:
        print('Wrong or no input argument!')


if __name__ == '__main__':
    position_0_value()