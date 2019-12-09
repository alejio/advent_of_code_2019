from day_06.src.orbit_map import load_input, create_graph


def test_load_input():
    assert len(load_input()) == 2603


def test_create_graph():
    graph = create_graph()
    assert len(graph.keys()) == 2349