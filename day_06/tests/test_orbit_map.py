from day_06.src.orbit_map import load_input, create_graph, find_all_paths, max_distance, \
    find_shortest_path_len


def test_load_input():
    assert len(load_input()) == 2603


def test_create_graph():
    data = load_input()
    graph = create_graph(data)
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


def test_max_distance_case1():
    paths = [['A', 'D', 'E'], ['A', 'B']]
    assert max_distance(paths) == 2


def test_max_distance_case2():
    paths = []
    assert max_distance(paths) == 0


def test_integration_part_1():
    data = load_input()
    graph = create_graph(data)
    paths = find_all_paths(graph, 'COM', '62T')
    assert len(paths) == 1
    assert max_distance(paths) == 3


def test_integration_part_2():
    # data = [['COM', 'B'], ['B', 'C'],
    #         ['C', 'D'], ['D', 'E'],
    #         ['E', 'F'], ['B', 'G'],
    #          ['G', 'H'], ['D', 'I'],
    #         ['E', 'J'], ['J', 'K'],
    #         ['K', 'L'], ['K', 'YOU'],
    #         ['I', 'SAN']]
    data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
    graph = create_graph(data)
    shortest_path = find_shortest_path_len(graph, 'YOU', 'SAN')
    assert shortest_path == 4