from day_03.src.crossed_wires import load_input, move, manhattan_distance, \
    map_path


def test_load_input():
    out = load_input()
    assert len(out) == 2
    assert len(out[0]) == 301
    assert len(out[1]) == 301
    assert out[0][0] == 'R1003'
    assert out[1][-1] == 'R261'


def test_move():
    starting_position = (0, 1)
    assert move('U42', starting_position) == (42, 1)
    assert move('D42', starting_position) == (-42, 1)
    assert move('R42', starting_position) == (0, 43)
    assert move('L42', starting_position) == (0, -41)


def test_manhattan_distance():
    assert manhattan_distance((4, 2), (7, 1)) == 4


def test_map_path():
    movements = ['R10', 'U11', 'D1', 'L10']
    assert map_path(movements) == {(0,0), (0, 10), (11, 10), (10, 10), (10, 0)}