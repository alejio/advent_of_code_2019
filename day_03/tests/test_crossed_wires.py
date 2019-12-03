from day_03.src.crossed_wires import load_input


def test_load_input():
    out = load_input()
    assert len(out) == 2
    assert len(out[0]) == 301
    assert len(out[1]) == 301
    assert out[0][0] == 'R1003'
    assert out[1][-1] == 'R261'