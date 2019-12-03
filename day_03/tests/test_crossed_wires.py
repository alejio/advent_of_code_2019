from day_03.src.crossed_wires import load_input, move, manhattan_distance, find_intersections, single_move_map


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


def test_single_move_map():
    assert single_move_map((0, 1), (0, 5)) == [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
    assert single_move_map((0, 5), (0, 1)) == [(0, 5), (0, 4), (0, 3), (0, 2), (0, 1)]
    assert single_move_map((1, 0), (5, 0)) == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
    assert single_move_map((5, 0), (1, 0)) == [(5, 0), (4, 0), (3, 0), (2, 0), (1, 0)]
    assert single_move_map((0, 0), (0, 0)) == [(0, 0)]


def test_manhattan_distance():
    assert manhattan_distance((4, 2), (7, 1)) == 4
    movements = ['R75','D30','R83','U83','L12','D49','R71','U7','L72', 'U62','R66','U55','R34','D71','R55','D58','R83']
    position = (0, 0)
    for movement in movements:
        position = move(movement, position)
    assert manhattan_distance(position, (0, 0)) == 159

# def test_map_path():
#     movements = ['R10', 'U11', 'D1', 'L10']
#     assert map_path(movements) == {(0, 10), (11, 10), (10, 10), (10, 0)}


def test_find_intersections():
    path_1 = {(1, 3), (2, 4), (16, 6)}
    path_2 = {(1, 3), (1, 4), (6, 16)}
    find_intersections(path_1, path_2) == {(1, 3)}