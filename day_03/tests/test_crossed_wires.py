from day_03.src.crossed_wires import load_input, move, manhattan_distance, \
    find_intersections, single_move_map, map_full_path, intersection_distances


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

# def test_map_path():
#     movements = ['R10', 'U11', 'D1', 'L10']
#     assert map_path(movements) == {(0, 10), (11, 10), (10, 10), (10, 0)}


def test_find_intersections():
    path_1 = {(1, 3), (2, 4), (16, 6)}
    path_2 = {(1, 3), (1, 4), (6, 16)}
    assert find_intersections(path_1, path_2) == {(1, 3)}


def test_nearest_crossing():
    movements_1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7',
                   'L72'], ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58',
                            'R83']
    distances = intersection_distances(movements_1[0], movements_1[1])
    assert min(distances) == 159
    movements_2 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20','R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    distances = intersection_distances(movements_2[0], movements_2[1])
    assert min(distances) == 135



    # position_1 = (0, 0)
    # movements_2 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20',
    #                'R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67',
    #                                       'R40', 'U7', 'R15', 'U6', 'R7']
    # position_2 = (0, 0)
    # for movement in movements_1[0]:
    #     position_1 = move(movement, position_1)
    # for movement in movements_1[1]:
    #     position_2 = move(movement, position_2)
    # position_3 = (0, 0)
    # position_4 = (0, 0)
    # for movement in movements_2[0]:
    #     position_3 = move(movement, position_3)
    # for movement in movements_2[1]:
    #     position_4 = move(movement, position_4)
    #
    # print('Closest crossing distance: ', )
    #
    # assert manhattan_distance(position_1, position_2) == 159