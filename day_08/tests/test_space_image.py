from day_08.src.space_image import load_input, parser, create_image, find_fewest_zeros_layer


def test_parser():
    assert parser('123456789012') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]


def test_load_input():
    data = load_input()
    assert len(data) % (25 * 6) == 0


def test_create_image():
    raw_data = '123456789012'
    data = parser(raw_data)
    image = create_image(data, 3, 2)
    assert len(image) == 2
    assert image[0] == [[1, 2, 3], [4, 5, 6]]
    assert image[1] == [[7, 8, 9], [0, 1, 2]]


def test_find_fewest_zeros_layer():
    image = [[[1, 0, 3], [0, 0, 4], [0, 0, 0]], [[1, 0, 2], [2, 2, 2], [3, 3, 3]], [[1, 1, 2], [2, 2, 2], [3, 3, 3]]]
    layer_idx = find_fewest_zeros_layer(image)
    assert layer_idx == 2

# def test_find_fewest_zeros_layer_tie():
#     image = [[[1, 0, 2], [2, 2, 2], [3, 3, 3]], [[1, 1, 2], [2, 0, 2], [3, 3, 3]]]
#     layer_idx = find_fewest_zeros_layer(image)
#     assert layer_idx == 1