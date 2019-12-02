from day_02.src.intcode_computer import load_input


def test_load_input():
    out = load_input()
    assert len(out) == 137
    assert out[0] == 1
    assert out[-1] == 0