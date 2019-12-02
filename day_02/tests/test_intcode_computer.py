from day_02.src.intcode_computer import load_input, add, multiply, halt, intcode_processor


def test_load_input():
    out = load_input()
    assert len(out) == 137
    assert out[0] == 1
    assert out[-1] == 0


def test_add():
    integer_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    sequence = integer_list[0:4]
    assert add(sequence, integer_list) == [1, 1, 1, 4, 2, 5, 6, 0, 99]


def test_multiply():
    integer_list = [2, 4, 4, 5, 99, 0]
    sequence = integer_list[0:4]
    assert multiply(sequence, integer_list) == [2, 4, 4, 5, 99, 9801]


def test_halt():
    integer_list = [99, 4, 4, 5, 99, 0]
    sequence = integer_list[0:1]
    assert halt(sequence, integer_list) == integer_list


def test_intcode_processor():
    case_1 = [[1, 0, 0, 0, 99], [2, 0, 0, 0, 99]]
    case_2 = [[2, 3, 0, 3, 99], [2, 3, 0, 6, 99]]
    case_3 = [[2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]]
    case_4 = [[1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]]
    assert intcode_processor(case_1[0]) == case_1[1]
    assert intcode_processor(case_2[0]) == case_2[1]
    assert intcode_processor(case_3[0]) == case_3[1]
    assert intcode_processor(case_4[0]) == case_4[1]