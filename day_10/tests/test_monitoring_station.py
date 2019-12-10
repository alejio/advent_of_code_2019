from day_10.src.monitoring_station import load_input, get_dimensions, get_asteroid_positions


def test_load_input():
    data = load_input()
    assert len(data) == 36
    assert len(data[0]) == 36


def test_get_dimensions():
    data = ['.#..#',
            '.....',
            '#####',
            '....#',
            '...##']
    assert get_dimensions(data) == (5, 5)


def test_get_asteroid_positions():
    data = ['.#..#',
            '.....',
            '#####',
            '....#',
            '...##']
    assert get_asteroid_positions(data) == [(0, 1), (0, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 3), (4, 4)]
#
# def test_count_asteroids():