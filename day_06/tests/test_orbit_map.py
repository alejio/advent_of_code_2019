from day_06.src.orbit_map import load_input, create_graph, find_all_paths, max_distance


def test_load_input():
    assert len(load_input()) == 2603


def test_create_graph():
    graph = create_graph()
    assert len(graph.keys()) == 2349


def test_find_all_paths_case1():
    graph = {'A': ['B', 'C']}
    paths = find_all_paths(graph, 'A', 'B')
    assert len(paths) == 1
    assert len(paths[0]) == 2


def test_find_all_paths_case2():
    graph = {'A': ['B', 'C'], 'C': ['E']}
    paths = find_all_paths(graph, 'A', 'E')
    assert len(paths) == 1
    assert len(paths[0]) == 3


def test_find_all_paths_case3():
    graph = {'A': ['B', 'C', 'D'], 'C': ['E'], 'D': ['E']}
    paths = find_all_paths(graph, 'A', 'E')
    assert len(paths) == 2
    assert len(paths[0]) == 3


def test_max_distance():
    paths = [['A', 'D', 'E'], ['A', 'B']]
    assert max_distance(paths) == 2


def test_integration():
    graph = create_graph()
    paths = find_all_paths(graph, 'COM', '62T')
    assert len(paths) == 1
