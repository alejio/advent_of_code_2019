from day_08.src.space_image import load_input


def test_load_input():
    data = load_input()
    assert len(data) % (25 * 6) == 0
